#!/usr/bin/env bash

# Self directory
SELF_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

script_version=1.0.0

PROFILE="${PROFILE:=dev}"

YRN=$(which yarn)
PY=$(which python3)

DJANGO_ADMIN="../../manage.py"
DJANGO_ADMIN=$(cd "$(dirname "$DJANGO_ADMIN")" || exit 1; pwd -P)/$(basename "$DJANGO_ADMIN")

MYSQL_CNF="../env/$PROFILE/.my.cnf"
MYSQL_CNF=$(cd "$(dirname "$MYSQL_CNF")" || exit 1; pwd -P)/$(basename "$MYSQL_CNF")

DATABASE_DIR="../database"
DATABASE_DIR=$(cd "$(dirname "$DATABASE_DIR")" || exit 1; pwd -P)/$(basename "$DATABASE_DIR")

WEBAPP_DIR="../../resources/static"

setup()
{
  cd "$SELF_DIR" || {
    log "Unable to change directory to $SELF_DIR"
    exit 1
  }



}


log()
{
  GET_DATE=$(date "+%Y-%m-%d %H:%M:%S")
  echo "[$GET_DATE] - migrate.sh - $$ - $1"
}


build()
{
  CURRENT=$(pwd)

  cd "${WEBAPP_DIR:?}" || {
    log "$WEBAPP_DIR does not exist, unable to build project!"
    cd "$CURRENT" || exit 1
    exit 1
  }

  log "Cleaning dir $WEBAPP_DIR"
  if [[ -d "${WEBAPP_DIR:?}/lib" ]]; then
    rm -dr "${WEBAPP_DIR:?}/lib"
  fi
  if [[ -d "${WEBAPP_DIR:?}/node_modules" ]]; then
    rm -dr "${WEBAPP_DIR:?}/node_modules"
  fi
  if [[ -f "${WEBAPP_DIR:?}/yarn.lock" ]]; then
    rm -f "${WEBAPP_DIR:?}/yarn.lock"
  fi

  log "Executing yarn install on webapp: $WEBAPP_DIR"
  $YRN install || {
    log "Unable to build project, yarn install failed!"
    exit 1
  }

  log "Executing yarn run build for building the statics..."
  $YRN run build || {
    log "Unable to build project, yarn run build failed!"
    exit 1
  }

  cd "$CURRENT" || {
    log "Unable to change directory to $CURRENT"
    exit 1
  }

  log "Webapp was successfully built!"

}


#######################################
# Executes django to create migrations for the application.
#
# Globals:
#   DJANGO_ADMIN
# Arguments:
#   None
#######################################
make_migrations()
{

  log "Running django to create the migrations:"
  $PY "$DJANGO_ADMIN" makemigrations || {
    log "Creation of migrations has failed.!"
    log "Django is unable to create migrations."
    exit 1
  }
  log "Migrations created!"
}


#######################################
# Executes django to migrate all the migrations to the database.
# If given a version, the migration will execute that one, otherwise the latest version will be executed.
#
# Globals:
#   DJANGO_ADMIN
# Arguments:
#   version to migrate
#######################################
migrate()
{
  target_version="$1"

  log "Running django to migrate into the database $target_version"

  if [ "$target_version" = "latest" ]; then
    log "Executing migration to latest version"
    $PY "$DJANGO_ADMIN" migrate || {
      log "Migration has failed for latest version"
      log "Unable to migrate!"
      exit 1
    }
  else
    log "Executing migration to version $target_version"
    $PY "$DJANGO_ADMIN" migrate "$target_version" || {
      log "Migration has failed for version $target_version"
      log "Unable to migrate!"
      exit 1
    }
  fi

  $PY "$DJANGO_ADMIN" makemigrations

  log "Migration finished!"
}


apply_patch()
{
  target_version="$1"
  if ! [[ "$target_version" == *"v"* ]]; then
    target_version="v$target_version"
  fi

  target_version_dir="$DATABASE_DIR/$target_version"

  has_scripts=$(find "$target_version_dir" -type f -name "*.sql" | wc -l | xargs)
  if [[ "$has_scripts" != "0" ]]; then
    log "Reading sql scripts from: $target_version_dir"
    for sql_script in "$target_version_dir"/*.sql "$target_version_dir"/"$PROFILE"/*.sql;
    do
      script_name=$(basename "$sql_script")
      log "Executing sql script $target_version/$script_name for environment: $PROFILE"
      mysql < "$sql_script" || {
        log "Error while executing script $target_version/$script_name"
        log "Unable to continue, versions execution failed!"
        exit 1
      }
    done
  fi
}


#######################################
# Executes baseline for the first deploy.
#
# Globals:
#   DATABASE_DIR
# Arguments:
#   None
#######################################
baseline()
{
  log "Running baseline to prepare database..."
  for sql_file in "$DATABASE_DIR"/baseline/*.sql;
  do
    filename=$(basename "$sql_file")
    log "Executing sql script baseline/$filename"
    mysql < "$sql_file" || {
      log "Error while executing $sql_file"
      log "Unable to continue, baseline execution failed!"
      exit 1
    }
  done
  log "Baseline execution finished."
}


#######################################
# Run release for application in database.
#
# Globals:
#   MYSQL_CNF
# Arguments:
#   None
#######################################
release()
{
  cp "$MYSQL_CNF" ~ || {
    log "$MYSQL_CNF file does not exist!"
    exit 1
  }

  has_versions=$(mysql -e 'show tables' | awk '{print $1}' | grep -c 'versions$')
  if [[ $has_versions -eq 0 ]]; then
    log "This is the first release, it needs to execute baseline."
    baseline
  fi

  make_migrations
  migrate "latest"

  latest_version=$(find "$DATABASE_DIR" -depth -type d | xargs -I{} basename {} | sort -V | tail -n 1)
  log "Running versions and populating database up to version: $latest_version"

  apply_patch "$latest_version"

}


#######################################
# Drops all tables in the database.
#
# Globals:
#   MYSQL_CNF
# Arguments:
#   None
#######################################
drop_db()
{
  cp "$MYSQL_CNF" ~ || {
    log "$MYSQL_CNF file does not exist!"
    exit 1
  }

  tables=$(mysql -e 'show tables' | awk '{print $1}' | grep --invert-match '^Tables')

  deletion_query="SET FOREIGN_KEY_CHECKS = 0"
  for t in $tables
  do
    log "Deleting $t table from database..."
    deletion_query="$deletion_query; drop table $t"
  done
  deletion_query="$deletion_query;SET FOREIGN_KEY_CHECKS = 1;"

  log "Executing deletion query: $deletion_query"

  mysql -e "$deletion_query" || {
    log "Unable to execute $deletion_query"
    log "Unable to drop database."
    exit 1
  }

  log "Removing .my.cnf file from $HOME"
  rm -f ~/.my.cnf
}


rollback()
{
  target_version="$1"

  cp "$MYSQL_CNF" ~ || {
    log "$MYSQL_CNF file does not exist!"
    exit 1
  }

  log "Rolling back to version: $target_version"

  migrate "$target_version"
  apply_patch "$target_version"

  log "Removing .my.cnf file from $HOME"
  rm -f ~/.my.cnf
}


if [[ $# -eq 0 ]]; then
  echo "usage: migrate [-k|--makemigrations] [-m|--migrate] [-b|--baseline]"
  exit 1
fi

run_release=0
run_drop=0
run_rollback=0
run_build=0

positional=()
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --build)
      run_build=1
      break
      ;;
    --release)
      run_release=1
      version="${2}"
      break
      ;;
    --rollback)
      run_rollback=1
      version="${2}"
      break
      ;;
    --drop)
      run_drop=1
      break
      ;;
    --dbr)
      run_drop=1
      run_build=1
      run_release=1
      break
      ;;
    *)
      positional+=("$1")
      break
      ;;
  esac
done

set -- "${positional[@]}"
version="${version:=0001}"

log "Version: $script_version"
log "Profile: $PROFILE"
log "=================================================="
log "+ -----------------------------------------------+"
log "|                                                |"
log "|              Wishmakers 2021(c)                |"
log "|       Delivery Pipeline script execution       |"
log "|                                                |"
log "|                         by: kevin.encinas      |"
log "|                                                |"
log "+ -----------------------------------------------+"
log "=================================================="

if [[ "$run_build" -eq 1 ]]; then
  log "Building project: "
  build
fi

if [[ "$run_drop" -eq 1 ]]; then
  log "Dropping database: "
  drop_db
fi

if [[ "$run_release" -eq 1 ]]; then
  log "Running release of latest version"
  release
fi

if [[ "$run_rollback" -eq 1 ]]; then
  log "Executing rollback to version $version"
  rollback $version
fi
