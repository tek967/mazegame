#!/bin/sh

if [ $1 == "--interpreter" ]; then
    $2 src/main.py
else
    python3 src/main.py
fi