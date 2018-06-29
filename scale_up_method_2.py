#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 18:33:47 2018

@author: kazoo


    https://arc022.contest.atcoder.jp/tasks/arc022_2


"""

N = 7
ary = [1,2,1,3,1,4,4]


def scaleUp(N,ary):
    
    right = 0
    left = 0
    longest = 0
    
    temp = []

    while right < N:
        
        
        if not (ary[right] in temp):
            
            right +=1
            gap = right - left
            
            if gap > longest:
                longest = gap 
            
        elif right == left:
            
            right += 1
            left  += 1 
        else:
            
            left += 1
            
        temp = (ary[left:right])
        print("left: {}, right: {}, temp: {}".format(left,right,temp))
        temp.clear
        
    print(longest)   
        
        
        
scaleUp(N,ary)     
        
        
        
        
        
            
            