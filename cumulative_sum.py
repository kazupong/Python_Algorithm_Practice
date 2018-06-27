#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:16:56 2018

@author: kazoo
"""

'''
例題：

一列に並んでいるコマから、指定された区間の長さで区間の中に含まれるコマの合計点数が最大だと思う
区間を考え、区間を指定します。 この指定した区間のコマの合計点数を、敵ウナギにダメージとして与える
ことが出来ます。この時、合計点数の値が指定できる各区間の中で最大だった場合、敵ウナギにクリティカルヒット
を与えることが出来ます。
1行目に区間の長さ t と コマの総数 n がスペース区切り 
2行目以降に n 個のコマの点数 m_i が改行区切りで与えられます。 
区間合計点数の最大値(クリティカルヒットが出る区間の合計点数)を出力するプログラムを作成してください。
'''


'''
    try:
        
        userIn = (input("区間の長さ and コマの総数 n").split())
        t = int(userIn[0])
        n = int(userIn[1])
        
        m_i = []
        
        for x in range(n):
             m_i.append(int(input()))   
            
    except:
        print("error in user input")
'''

n = 5
t = 2
m_i = [99,6,23,7,45,77,4,3,5,6,7]

cumsum = [0]
count = 0

while count < len(m_i):
      temp = m_i[count] + cumsum[count]
      cumsum.append(temp)
      count += 1
    
print("m_i:    {}".format(m_i))
print("cumsum: {}".format(cumsum))
    
    
s_index = t
biggest = cumsum[s_index] - t
big_index =  0
while s_index != len(cumsum):
     temp = (cumsum[s_index] - cumsum[s_index - t])
     if temp > biggest:
           biggest = temp
           big_index = s_index - 1
     s_index += 1
    
returnList = []
for x in m_i[big_index-1:big_index+1]:
    returnList.append(x)
    
print("The critical hit would be {},".format(biggest))
print("its elements are... {}".format(returnList))
   
   
   
 