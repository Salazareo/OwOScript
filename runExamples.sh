#!/bin/bash
errFolder="Errors"
for dirName in Example/*/; do
    if [[ "$dirName" != *"$errFolder"* ]]; then
        echo "Running examples in $dirName"
        echo "----------------------------------------------------"
        for fileName in $dirName/*.owo; do

            ./wow.sh $fileName
            echo '================================================'
        done
        echo ""
    fi
done
echo "Running Error cases in Errors folder, each line should be an error"
python test_parser.py
sourceCode=$1

defaultVer=$(python --version 2>/dev/null)
v3=" 3."
if [[ "$defaultVer" == *"$v3"* ]]; then
    python test_parser.py
else
    pythonVer=$(which python3 2>/dev/null)
    v3="python3"
    if [[ "$pythonVer" == *"$v3"* ]]; then
        python3 test_parser.py
    else
        echo "Requires python3"
    fi
fi
