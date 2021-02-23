#!/bin/bash
for filename in ./Examples/*.owo; do
    python3 ./parser.py ./Examples/$filename
done
