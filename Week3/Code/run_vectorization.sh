#!/bin/bash
echo "The runtime for four vectorization scripts:"
echo "-----------------------The Vectorize1.R-----------------------"
Rscript ../../../Code/Vectorize1.R
echo "-----------------------The Vectorize1.py-----------------------"
python3 Vectorize1.py
echo "-----------------------The Vectorize2.R-----------------------"
Rscript ../../../Code/Vectorize2.R
echo "-----------------------The Vectorize2.py-----------------------"
python3 Vectorize2.py
echo "Done!"