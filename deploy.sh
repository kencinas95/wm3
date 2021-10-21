#!/bin/bash

PYTHON=$(which python3)

$PYTHON build.py app run --job build
$PYTHON build.py web run --job build
$PYTHON build.py db run --job drop
$PYTHON build.py db run --job baseline
$PYTHON build.py db run --job migrate
