#!/bin/bash
for filename in Example/*.owo; do
    ./wow.sh $filename
    echo '================================================'
done
