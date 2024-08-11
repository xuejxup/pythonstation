# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 08:02:02 2024

@author: xuejxup
"""

import random

ans1=set()

while len(ans1)<10: 
        ans2=random.randint(1, 100) 
        ans1.add(ans2)
        
ans3=sorted(ans1,reverse=False)
print("隨機生成的數字為:",ans3)    
print("值數為:")
for a in ans3:
    ispren=True
    for x in range(2,a):
       if a % x == 0:
           ispren=False
           break
    if ispren:
          print(a,end=" ")

        


 