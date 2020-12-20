#!/bin/bash
echo "Run get_TreeHeight.R and get_TreeHeight.py with an argument 'Trees.csv'"
Rscript get_TreeHeight.R Trees.csv
python3 get_TreeHeight.py Trees.csv
echo "Finished!"