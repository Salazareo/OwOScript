#!/bin/bash

# This is the official Weeb OwOScript Wompiler :3 (wow)
noWhite=""

while getopts ":w" opt; do
    case ${opt} in
    w)
        noWhite="-w"
        ;;
    \?) ;;

    esac
done
shift $((OPTIND - 1))
sourceCode=$1

defaultVer=$(python --version 2>/dev/null)
v3=" 3."
if [[ "$defaultVer" == *"$v3"* ]]; then
    python ./parser.py $sourceCode && (python ./toJS.py $noWhite "$sourceCode.json") && rm "$sourceCode.json"
else
    pythonVer=$(which python3 2>/dev/null)
    v3="python3"
    if [[ "$pythonVer" == *"$v3"* ]]; then
        python3 ./parser.py $sourceCode && (python3 ./toJS.py $noWhite "$sourceCode.json") && rm "$sourceCode.json"
    else
        echo "Requires python3"
    fi
fi
sleep 100
