#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 00:14:40 2018

@author: shawon
uva : 10340 - All in All
#=====================================================
"""

def main():
    while True:
        try:
            
            substring,string = map(str,input().split())
            n,m=len(substring),len(string)
            # n = substring len 
            # m = string len
            if m<n:
                print("No")
            else:
                i=0
                for j in range(0,m):
                    if i == n:
                        break
                    if substring[i]==string[j]:
                        i+=1
                if i==n:
                    print("Yes")
                else:
                    print("No")
                    
                
        except EOFError:
            break
            
    
    
 
if __name__=="__main__":
    main()    