#!/bin/bash

# This is the official Weeb OwOScript Wompiler :3 (wow)

sourceCode=$1
python ./parser.py $sourceCode || python3 ./parser.py $sourceCode
python ./toJS.py "$sourceCode.json" || python3 ./toJS.py "$sourceCode.json"
