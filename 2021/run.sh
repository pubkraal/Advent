#!/usr/bin/env bash

FILES=$(echo input/*.txt | egrep -o '[0-9]+' | uniq)

for NUM in $FILES; do
    python3 "$NUM.py"
done
