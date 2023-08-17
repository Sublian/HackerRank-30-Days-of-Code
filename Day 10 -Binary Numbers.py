#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #usin bin() transform the numbx10 to numbx2
    b = str(bin(n))[2:]
    total = 0
    temp = 0
    #print(b)
    for i in b :
        if i == '1' :
            temp += 1
        else :
            total = max(total,temp)
            temp = 0
    total = max(total,temp)
    print(total)
    
    """
    Other way
    binn = ""
    while(1) :
        if n > 0 :
            binn += str(n%2)
            n //= 2
        else :
            break
    binn = "".join(reversed(binn))
    print(len(max(binn.split("0"))))
    """
