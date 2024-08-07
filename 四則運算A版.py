# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:33:03 2024

@author: xuejxup
"""

import random
ans1=random.randint(1, 100)
ans2=random.randint(1, 100)
guess=0

q=input("請選擇模式:1:加法 2:減法 3:乘法 4:除法")
    
if q == "1":
        ex=ans1+ans2    
        print("加法題目:")
        print(ans1,"+",ans2,"=")
       
        
elif q == "2": 
    ex=ans1-ans2        
    print("減法題目:")
    print(ans1,"-",ans2,"=")    
    
    
elif q == "3":  
    ex=ans1*ans2 
    print("乘法題目:")
    print(ans1,"*",ans2,"=")

    
elif q=="4":
    while True:
        ans1 = random.randint(1, 100)
        ans2 = random.randint(1, 100)
        if ans2 != 0 and ans1 % ans2 == 0:
            ex = ans1 // ans2
            print("除法題目:")
            print(ans1, "/", ans2, "=")
            break
        elif ans1 != 0 and ans2 % ans1 == 0:
            ex = ans2 // ans1
            print("除法題目:")
            print(ans2, "/", ans1, "=")
            break

    
guess=int(input("請輸入答案:"))   

if guess == ex:
   print("答對囉")
else:
   print("答錯囉")
   print("答案是",ex)