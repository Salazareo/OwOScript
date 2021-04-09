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
