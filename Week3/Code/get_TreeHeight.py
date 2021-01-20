#!/usr/bin/env python3

""" Groupwork: to do TreeHeight Calculation using Python """
# Script Name: get_TreeHeight.py
# Author: Jingkai Sun (ks3020@ic.ac.uk)

import sys
import pandas as pd
import numpy as np
import re

def TreesHeight(degrees, dist):
    radians = degrees * np.pi / 180
    height = dist * np.tan(radians)
    print(height)

    return(height)

def main(argv):
    default_path = "../Data/"
    if len(sys.argv) == 1:
        filename = "trees.csv"
    else:
        filename = argv[1]
    filename_noExt = re.search(r"\w+", filename).group()
    save_name = "../Results/%s_treeheights_python.csv" % filename_noExt
    filepath = default_path + filename
    trees_data = pd.DataFrame(pd.read_csv(filepath))
    
    trees_data["Height"] = TreesHeight(trees_data["Angle.degrees"], trees_data["Distance.m"])
    
    # Save to csv
    trees_data.to_csv(save_name, sep=",", index = False)
    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


