#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    count = 0
    for i in s:
        if(i == "U"):
            height=height+1
        if(i == "D"):
            height=height-1

        if(i == "U" and height==0):
            #exit a valley
            count=count+1

    return count