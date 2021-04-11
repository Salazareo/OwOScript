#!/bin/bash
for dirName in Example/*/; do
    echo "Running examples in $dirName"
    echo "----------------------------------------------------"
    for fileName in $dirName/*.owo; do
        ./wow.sh $fileName
        echo '================================================'
    done
    echo ""
done
echo "Running Error cases in Errors folder, each line should be an error"
python test_parser.py

sleep 100
