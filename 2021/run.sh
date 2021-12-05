#!/usr/bin/env zsh

IFS=$'\n' FILES=($(echo input/*.txt | egrep -o '[0-9]+' | uniq))

for NUM in $FILES; do
    time python3 "$NUM.py"
done
