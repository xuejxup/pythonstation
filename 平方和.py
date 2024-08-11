# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 10:01:22 2024

@author: xuejxup
"""

number1=[]

print("最大數字為:50")
print("大於50將會離開程式")

while True:       
      number2=int(input("請輸入數字:"))
      if number2 > 50  :
         break
      number3=number2*number2
      number1.append(number3)
      print(number2,"的平方數為:",number1)
           
total=sum(number1)
print("平方和為:",total)