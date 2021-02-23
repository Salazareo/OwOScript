#!/bin/bash
for filename in Example/*.owo; do
    python parser.py $filename
done
python test_parser.py
