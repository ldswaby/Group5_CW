#!/usr/bin/env python3

"""Calculate tree heights using Python"""

## Variables ##

__author__ = 'Luke Swaby (lds20@ic.ac.uk), ' \
             'Jinkai Sun (jingkai.sun20@imperial.ac.uk), ' \
             'Acacia Tang (t.tang20@imperial.ac.uk), ' \
             'Dengku Tang (dengkui.tang20@imperial.ac.uk)'
__version__ = '0.0.1'

## Imports ##

import sys
import pandas as pd
import numpy as np
import re

## Functions ##

def TreesHeight(degrees, dist):
    """This function calculates heights of trees given distance of each tree
    from its base and angle to its top, using  the trigonometric formula
    height = distance * tan(radians)

    Arguments:
     - degrees:   The angle of elevation of tree
     - dist:  The distance from base of tree (e.g., meters)

    Output:
     - The heights of the tree, same units as "distance"
    """
    radians = degrees * np.pi / 180
    height = dist * np.tan(radians)
    print(height)

    return height

def main(argv):
    default_path = "../Data/"
    filename = argv[1]
    filename_noExt = re.search(r"\w+", filename).group()
    save_name = "../Results/%s_treeheights_python.csv" % filename_noExt
    filepath = default_path + filename
    trees_data = pd.DataFrame(pd.read_csv(filepath))
    
    trees_data["Height"] = TreesHeight(trees_data["Angle.degrees"],
                                       trees_data["Distance.m"])
    
    # Save to csv
    trees_data.to_csv(save_name, sep=",", index = False)

    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)


