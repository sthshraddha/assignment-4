#!/usr/bin/en python
"""
Note to self: Need flake8 to save script as .py file in Atom.
To download: Go to cmd in Windows. Type conda install flake8
flake8 should be installed and we can then save scripts in .py
Task 1:
Write a complete program, formatted in the way that we discussed,
that prints the range of numbers, 0 to 50, by 5. Have the program output each
of these numbers, separated by commas, on the same line. Do not do this
in a function.

Created by Shraddha Shrestha on 26 Jan 2016.
Copyright 2016 Shraddha Shrestha. All rights reserved.

"""

for number in range (0,51):
    if number % 5 ==0:
        print(number, end=',')
