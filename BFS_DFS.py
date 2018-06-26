#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:28:44 2018

@author: kazoo
"""



from random import randint
import queue


class node:
    def __init__(self, value = None):
        self.value = value
        self.left  = None
        self.right = None
        self.visit = False

class stack():
    def __init__(self):
        self._stack__list = []
    def push(self,value):
        self._stack__list.append(value)
    def pop(self):
        return self._stack__list.pop()
    def peek(self):
         return self._stack__list[len(self.items)-1]
    def size(self):
         return len(self._stack__list)
    def isEmpty(self):
        return self.items == []

class binary_search:
    
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        if self.root == None:
             self.root = node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, current):
        if value < current.value:
            if current.left == None:
                current.left = node(value)
            else:
                self._insert(value, current.left)
        else:
            if value > current.value:
                if current.right == None:
                     current.right = node(value)
                else:
                    self._insert(value,current.right)
    
    def BFS(self, value):
        if self.root != None:
            self._BFS(value, self.root)
        else:
            return "B_Tree does not hold a root..."
           
    def _BFS(self, value, cur_node):
         que = queue.Queue()
         #cur_node.visit = True
         que.put(cur_node)

         while que:
             temp = que.get()
             if temp.value is not None:
                print(temp.value, end = " ")
             
             if  temp.value == value:
                 print()
                 print("The target [{}] has found".format(temp.value))
                 break
             else:
                 if temp.left is not None:
                      #temp.visit = True
                      que.put(temp.left)
                 if temp.right is not None:
                      #temp.visit = True
                      que.put(temp.right)
         
          
    
    def DFS(self,value):
        if  self.root != None:
            self._DFS(value,self.root)
        else:
            return "B_Tree does not hold a root..."
   
    def _DFS(self, value, cur_node):
        stk = stack()
        stk.push(cur_node)
        
        while stk:
            temp = stk.pop()
            if temp.value is not None:
                print(temp.value, end =" ")
            
            if temp.value == value:
                print()
                print("The target [{}] has found".format(temp.value))
                break
            else:
                if temp.left is not None:
                      stk.push(temp.left)
                if temp.right is not None:
                      stk.push(temp.right)
        
        
        
    def print_tree(self):
        if  self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self, nord):
        
        if nord != None:
             print(nord.value)
             self._print_tree(nord.left)
             self._print_tree(nord.right)
        
            


tree = binary_search ()
tree.insert(2)
for x in range(5):
    #num = randint(0,10)
    if(x != 2):
        tree.insert(x)

tree.print_tree()

print()
print(tree.BFS(4))
print()
print(tree.DFS(1))
