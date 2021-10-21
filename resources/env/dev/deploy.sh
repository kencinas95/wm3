#!/usr/bin/env bash

export PROFILE=dev

DELIVERY_SCRIPT="../../pipeline/delivery.sh"
DELIVERY_SCRIPT=$(cd "$(dirname "$DELIVERY_SCRIPT")"; pwd -P)/$(basename "$DELIVERY_SCRIPT")

log()
{
  GET_DATE=$(date "+%Y-%m-%d %H:%M:%S")
  echo "[$GET_DATE] - deploy.sh - $$ - $1"
}


cd $(dirname "$DELIVERY_SCRIPT") || {
  log "Error"
  exit 1
}

while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --deploy)
      exec "$DELIVERY_SCRIPT" --dbr
      ;;
    --rollback)
      exec "$DELIVERY_SCRIPT" --rollback "$2"
      ;;
    --drop)
      exec "$DELIVERY_SCRIPT" --drop
      ;;
    *)
      break
      ;;
  esac
done


