#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 01:37:28 2018
uva: cost cutting
@author: shawon
"""

def main():
    n = int(input())
    for i in range(1,n+1):
        L = list(map(int,input().split()))
        L.sort()
        print("Case {:,}:".format(i),L[1])



if __name__=="__main__":
    main()