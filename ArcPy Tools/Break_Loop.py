#Name: Philip Carr
#Date: Feburary 12, 2023
#Description: This script demonstrates how to break a loop
from math import sqrt
for i in list (range(1000,0,-1)):
    root=sqrt(i)
    if root == int(root):    #This evaluates wheather the root is an integer.
        print(i)
        break
       
