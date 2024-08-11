# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 06:15:40 2024

@author: xuejxup
"""

number1=[]

for i in range(3):
           
      number2=input("請輸入數字:")
      number3=int(number2)
      number1.append(number3)
      
      
     
number1.sort(reverse=True)   
print(number1)