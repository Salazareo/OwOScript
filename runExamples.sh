#!/bin/bash
for filename in Example/*.owo; do
    ./wow.sh $filename
done
python test_parser.py
