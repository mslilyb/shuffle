#!/bin/env python3
import sys
import json

if sys.argv[1] == 'help' or sys.argv[1] == 'h':
    print("usage: <# of models> <model 1> <model 2> ... <model n> <comparisons>")

n = sys.argv[1]
models = sys.argv[2:n]

comparisons = sys.argv[n:]

fps = []

for model in models:
    fps.append(open(model, 'r'))

jobjs = []

for fp in fps:
    jobj = json.load(fp)
    jobjs.append(jobj)

for comparison in comparisons:
    
