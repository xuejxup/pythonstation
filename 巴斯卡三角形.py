# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 05:00:42 2024

@author: xuejxup
"""

n = int(input("請輸入三角形階層: "))
ans = []

if n == 1:
    print(1)
else:
    for a in range(n):
        row = []
        for b in range(a + 1):
            
            c = 1
            for i in range(1, a + 1):
                c *= i
            d = 1
            for i in range(1, b + 1):
                d *= i
            e = 1
            for i in range(1, a - b + 1):
                e *= i
            num = int(c / (d * e))
            row.append(num)
        ans.append(row)
    

    
    for x in range(n):
        
        print(" " * (n - x), end="")
        for y in ans[x]:
            print(y, end=" ")
        print()
