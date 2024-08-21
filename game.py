# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:34:37 2024

@author: USER
"""

from role import swordman,navigator,doctor

import random



def showfight(role):
    print(role.getname(),"使出:",end="")
    role.fight()
    
def rolefight(frole,srole):
    print(frole.getname(),"使出",end="")    
    frole.fight()
    boold=random.randint(0, 10)
    srole.changboold(boold)
    print(srole.getname(),"血量剩下:",srole.gethp())
 
  
if __name__ == "__main__":
    
  man=swordman("索隆",100,500,80)
  Navigator=navigator("娜美",100,1000,80)
  Doctor=doctor("喬巴",100,1000,80)
  
  com=list()
  player=list()
  
  com.append(man)
  com.append(Doctor)
  com.append(Navigator)
  
  player.append(swordman("熾天使",100,50,1))
  player.append(navigator("黃猿",100,1500,2))
  player.append(doctor("朵拉",100,2000,5))
  k=random.randint(1, 100)
  print(k)
  if k % 2== 0 :
        comf=1
  else:
        comf=2
      
   
  while (len(com)>0 and len(player)>0):
          if comf == 1:
              
              
              c=random.choice(com)
              pboold=list()          
              for row in player:
                  pboold.append(row.gethp())
              
              pi=min(pboold)
              pc=player[pboold.index(pi)]
              rolefight(c,pc)
              
              if pc.gethp()<=0:
                 player.remove(pc)
              if isinstance(c, doctor):
                  print(c.getname(),"是醫生使用了",c.cure())
                  pass
              if len(player)==0:    
                  break
                  
              c=random.choice(player)
              pboold=list()          
              for row in player:
                  pboold.append(row.gethp())
              
              pi=min(pboold)
              pc=com[pboold.index(pi)]
              rolefight(c,pc)
              
              if pc.gethp()<=0:
                  com.remove(pc)
                  
          else:
              c=random.choice(player)
              pboold=list()          
              for row in com:
                  pboold.append(row.gethp())
              
              pi=min(pboold)
              pc=com[pboold.index(pi)]
              rolefight(c,pc)
              
              if pc.gethp()<=0:
                  com.remove(pc)
              if isinstance(c, doctor):
                  print(c.getname(),"是醫生")
                  pass
              if len(com)==0:    
                  break
                  
              c=random.choice(com)
              pboold=list()          
              for row in com:
                  pboold.append(row.gethp())
              
              pi=min(pboold)
              pc=com[pboold.index(pi)]
              rolefight(c,pc)
              
              if pc.gethp()<=0:
                  com.remove(pc)
                  
  if len(player) == 0 :
               print("電腦WIN")
  else:
               print("玩家WIN")
          
          
          
              
         
          
  
  
  