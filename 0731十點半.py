# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 20:06:09 2024

@author: USER
"""




import random

card=[]

c=int(input("請輸入您的籌碼:"))

for i in range(4):
    for n in range(1,14):
        
        if n >10:
            card.append(0.5) 
        else:   
            card.append(n)
#print(card)
#print(len(card))      

for a in range(200):
    start=random.randint(0,51)
    end=random.randint(0,51)
    card[start],card[end]=card[end],card[start]
print(card)

while c > 0 :
    
    q=input("是否要玩10點半?(y/n):")  
    if q=="n":
       break
    
    p=int(input("請投注:")) 
    c=c-p
    print("玩家目前籌碼:",c)

    com=[]
    player=[]

    com.append(card.pop())
    player.append(card.pop())
    count=1

    while True:
                
                print("玩家目前點數:",sum(player))
                if sum(player) >= 10.5 or count == 5: 
                    break
                q=input("要補牌嗎(y/n):")
                if q=='n':
                    break        
                number = card.pop()
                print("點數:",number) 
                player.append(number)
                count += 1
    if sum(player)>10.5:
            print("玩家爆了")
    elif sum(player)==10.5 or count==5:
            print("玩家WIN")
    else:
        
            while True:
                  
                    print("莊家目前點數:",sum(com))
                    if sum(com) >= 10.5 or sum(com)>= sum(player) or count==5:
                        break
                    if sum(com)>10.5:
                        print("莊家爆了")
                    else:
                        number = card.pop()
                        print("莊家補牌點數:",number) 
                        com.append(number)
    
    if sum(player) == 10.5:
                print("玩家10.5勝利")
                p=p*5
                c=c+p
                print("玩家贏的籌碼:",p)
                print("玩家目前籌碼:",c)
    elif count == 5 and sum(player)<= 10.5 :
                print("玩家過五關勝利")
                p=p*50
                c=c+p
                print("玩家贏的籌碼:",p)
                print("玩家目前籌碼:",c)
    elif sum(player) > sum(com) and sum(player) <= 10.5:
                print("player:", sum(player), "比", sum(com), "玩家勝利")
                p=p*2
                c=c+p
                print("玩家贏的籌碼:",p)
                print("玩家目前籌碼:",c)
    elif sum(player) > 10.5:
                print("玩家點數:", sum(player), "玩家輸了")               
                print("玩家輸的籌碼:",p)
                print("玩家目前籌碼:",c)
    elif sum(com) <= 10.5 and sum(com) > sum(player):
                print("莊家:", sum(com), "比", sum(player), "莊家勝利")              
                print("玩家輸的籌碼:",p)
                print("玩家目前籌碼:",c)
    elif sum(com)>10.5:
            print("莊家爆了,玩家贏了")
            p=p*2
            c=c+p        
            print("玩家目前籌碼:",c)
    elif count==5:
        print("莊家過五關勝利")  
        print("玩家輸的籌碼:",p)
    else:
            print("平局！")
            c=c+p
            print("玩家目前籌碼:",c)
            

    
    
    
    