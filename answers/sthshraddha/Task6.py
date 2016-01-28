#!/usr/bin/en python

"""
Task 6:
We talked a little bit about types. Write a program with a main function that
calls two separate functions to show the type of (1) a numpy array, and (2) a
sequence object (from biopython).

Note to self: Need to download Biopython using:
conda install Biopython
Numpy is already installed in Anaconda python prompt.
Created by Shraddha Shrestha on 27 Jan 2016 after 1 day of trying to make
it work.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

import numpy as np
import Bio
from Bio.Seq import Seq

A = np.array([2,3,4])
B = Seq('CGATA')


def numpy():
    print (type(A))


def Seq():
        print(type(B))


def main():
    numpy()
    Seq()

main()
