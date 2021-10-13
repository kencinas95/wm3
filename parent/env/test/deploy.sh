#!/usr/bin/env bash

export PROFILE=test

MIGRATION_SCRIPT="../../pipeline/migrate.sh"
MIGRATION_SCRIPT=$(cd "$(dirname "$MIGRATION_SCRIPT")"; pwd -P)/$(basename "$MIGRATION_SCRIPT")


log()
{
  GET_DATE=$(date "+%Y-%m-%d %H:%M:%S")
  echo "[$GET_DATE] - pipeline.sh - $$ - $1"
}


cd $(dirname "$MIGRATION_SCRIPT") || {
  log "Error"
  exit 1
}

while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    -r|--release)
      exec "$MIGRATION_SCRIPT" --release
      ;;
    -b|--rollback)
      exec "$MIGRATION_SCRIPT" --rollback "$2"
      ;;
    -d|--drop)
      exec "$MIGRATION_SCRIPT" --drop
      ;;
    *)
      break
      ;;
  esac
done


