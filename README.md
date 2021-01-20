# CMEE Groupwork Repository

This repository contains computing groupwork for the [MSc Computational Methods in Ecology and Evolution](https://www.imperial.ac.uk/study/pg/life-sciences/computational-methods-ecology-evolution/) at Imperial College London.

This repository is divided into weeks, with the directory for each week containing a combination of the following subdirectories:
* Data - contains data files used during the week.
* Code - contains all code scripts for the week.
* Results - empty directory for any results files to be pushed into if they exist.

Scripts in the *Code/* directory are typically run on files in the *Data/* directory, with results (if there are any) being pushed into the *Results/* directory.

E.g.

```
$ python3 Week2/Code/align_seqs_better.py Week2/Data/407228326.fasta Week2/Data/407228412.fasta
```

## Table of Contents
1. [Week 2: Python I](https://github.com/ldswaby/Group5_CW/tree/master/Week2)
2. [Week 3: R](https://github.com/ldswaby/Group5_CW/tree/master/Week3)
3. [Week 7: Python II](https://github.com/ldswaby/Group5_CW/tree/master/Week7)

### Week 2: Python I

Introduction to the Python programming language.

Topics covered:
* Basics of Python as a programming language.
* Basic Python data types and structures.
* How to write clean and well-annotated Python scripts for automating computing tasks. 
* How to write Python functions and programs.

Notes: [Biological Computing in Python I](https://mhasoba.github.io/TheMulQuaBio/notebooks/05-Python_I.html#)

### Week 3: R

Introduction to the R programming language.

Topics covered:
* How to use R for data exploration
* How to use R for data visualization and producing elegant, intuitive, and publication quality graphics.
* R data types & structures and control flows.
* How to write and debug efficient R scripts and functions.
* How to use R packages and applications in certain areas (e.g., Genomics, Population biology).

Notes: 
* [Biological Computing in R](https://mhasoba.github.io/TheMulQuaBio/notebooks/07-R.html)
* [Data Management and Visualization](https://mhasoba.github.io/TheMulQuaBio/notebooks/08-Data_R.html)

### Week 7: Python II

More advanced Python topics.

Topics covered:
* Python program testing, debugging and documentation.
* How to use Python for retrieving, managing, and analyzing data from local and remote databases. • to automate file handling, string manipulation, and run shell scripts.
* How to use Python for efficient numerical analyses.
* How to run analyses by patching together R or R + Python scripts and functions.

Notes: 
* [Biological Computing in Python II](https://mhasoba.github.io/TheMulQuaBio/notebooks/06-Python_II.html)
* [Introduction to Jupyter](https://mhasoba.github.io/TheMulQuaBio/notebooks/Appendix-JupyIntro.html)

## Prerequisites

This project was developed on a UNIX OS.

The following packages (with versions) are used in the project:
* Python (3.7.7)
* R (4.0.3)

## Dependencies

### Python 3.7
* `random` 
* `numpy` 
* `math` 
* `pandas` 
* `matplotlib`
 
### R 4.0.3
* `tools`
* `dplyr`

## Contact

Email: 
* <lds20@ic.ac.uk>
* <jingkai.sun20@imperial.ac.uk>
* <t.tang20@imperial.ac.uk>
* <dengkui.tang20@imperial.ac.uk>
