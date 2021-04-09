#!/bin/bash

# This is the official Weeb OwOScript Wompiler :3 (wow)

sourceCode=$1

(python3 --version 2>/dev/null) && (python3 ./parser.py $sourceCode && python3 ./toJS.py "$sourceCode.json")

defaultVer=$(python --version)

v3=" 3."

if [[ "$defaultVer" == *"$v3"* ]]; then
    python ./parser.py $sourceCode && python ./toJS.py "$sourceCode.json"
else
    echo "you need python3 for this"
fi
rm "$sourceCode.json"
