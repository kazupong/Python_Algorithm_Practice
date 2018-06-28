#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 20:49:52 2018

@author: kazoo
"""

#ary = [4,1,7,2]          # input 1
ary = [4,3,1,1,2,10,2]    # input 2
k = 6

# 尺取り法　
def scale_up(ary, k):
    
    # インデックスの初期値設定
    left  = 0
    right = 0
    
    if 0 in ary:
        return 0
    else:
        # index 
        left  = 0
        right = 0
        temp_mul = 1
        cur_list = []
        ans = 0
        while right < len(ary) :
            
            if (temp_mul * ary[right]) <= k:
                cur_list.append(ary[right])
                temp_mul *= ary[right]
                right += 1
            elif right == left:
                 right += 1
                 left  += 1
            else:
                cur_list.remove(ary[left])
                left += 1
                temp_mul = 1
                for i in range(left, right):
                    temp_mul *= ary[i]
            
            if len(cur_list) > ans :
                 ans = len(cur_list)   
            print("left = {}, right = {}, temp = {}".format(left,right,cur_list))
    return ans
    
   
scale_up(ary,k)


"""  
------------- output 1 --------------

left = 0, right = 1, temp = [4]
left = 0, right = 2, temp = [4, 1]
left = 1, right = 2, temp = [1]
left = 2, right = 2, temp = []
left = 3, right = 3, temp = []
left = 3, right = 4, temp = [2]

------------------------------------
-------------output 2 --------------

left = 0, right = 1, temp = [4]
left = 1, right = 1, temp = []
left = 1, right = 2, temp = [3]
left = 1, right = 3, temp = [3, 1]
left = 1, right = 4, temp = [3, 1, 1]
left = 1, right = 5, temp = [3, 1, 1, 2]
left = 2, right = 5, temp = [1, 1, 2]
left = 3, right = 5, temp = [1, 2]
left = 4, right = 5, temp = [2]
left = 5, right = 5, temp = []
left = 6, right = 6, temp = []
left = 6, right = 7, temp = [2]

------------------------------------

"""
