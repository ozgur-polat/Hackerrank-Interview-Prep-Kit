import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    nondupl = list(dict.fromkeys(ar))
    counts = []
    result = 0
    for i in nondupl:
        count = 0
        for j in ar:
            if(i==j):
                count=count+1
        counts.append(count)
    
    print(counts)
    for i in counts:
        result=result+int(i/2)
    
    return result