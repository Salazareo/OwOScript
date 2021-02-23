#!/bin/bash
for filename in Example/*.owo; do
    python parser.py $filename || python3 parser.py $filename
done
python test_parser.py
