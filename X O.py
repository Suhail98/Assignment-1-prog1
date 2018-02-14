import random
a=[[1,4,7] ,[2,5,8] ,[3,6,9]]
m=0
n=0
b=[]
for i in range(0,7,1):
    if i%2==0:
        for j in range(0,7,1):
                print("* ",end='')
    else:
        for j in range(0,7,1):
            if j%2==0:
                print("* ",end='')
            else:
                print(a[n][m],"",end='')
                if n==2:
                    m+=1
                    n=0
                else:
                    n+=1
    print()
s=''
g=int(input("Enter 1 for 2 player mode or 2 for playing against the computer(easy) or 3 for      the hard"))

while g<1 or g>3:
    g=int(input("Enter 1 for 2 player mode or 2 for playing against the computer(easy) or 3 for       the hard"))
for k in range(0,9,1):
    s=''
    r=0
    c=0
    if g==1 or g==2:  
     if k%2==0:
        x=int(input("X turn"))
        s='X'
        while x<1 or x>9:
            x=int(input("Index out of range,pls enter the correct index"))
     else:
       if g==1: 
         x=int(input("O turn"))
         s='O'
         while x<1 or x>9:
            x=int(input("Index out of range,pls enter the correct index"))
         
      
     if g==1 or k%2==0:
      if x>6:
            r=2
            c=x-7
      elif x>3:
            r=1
            c=x-4
      else:
            r=0
            c=x-1
     elif g==2:
        print("O turn")
        s='O'
        while x<1 or x>9:
            x=int(input("Index out of range,pls enter the correct index"))
        c=random.randrange(0,3,1)
        r=random.randrange(0,3,1)
        while a[c][r]=='X' or a[c][r]=='O':
            c=random.randrange(0,3,1)
            r=random.randrange(0,3,1)
            
     a[c][r]=s
    else :
      if k%2==1:
          x=int(input("O turn"))
          s='O'
          while x<1 or x>9:
            x=int(input("Index out of range,pls enter the correct index"))
          if x>6:
            r=2
            c=x-7
          elif x>3:
            r=1
            c=x-4
          else:
            r=0
            c=x-1
          a[c][r]='O'  
      else :
          print("X turn")
          s='X'
          if k==0:
              r=2
              c=0
          elif k==2:
              if a[2][2]=='O':
                  r=0
                  c=0
              elif a[1][1]=='O':
                  r=0
                  c=2
              else:
                  r=2
                  c=2
          elif k==4:
              f=0
              xx=0
              rr=0
              p=0
              s1='X'
              for h in range(0,3,1):
                  for r1 in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='O':
                          rr=r1
                      elif a[h][r1]=='O':
                          break
                      else :
                          f+=1
                  if f==2:
                      c=h
                      r=r1
                      p=1
                      break
                  f=0  
              f=0
              xx=0
              rr=0      
              for r1 in range(0,3,1):
                  for h in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='O':
                          xx=h
                      elif a[h][r1]=='O':
                          break    
                      else :
                          f+=1
                  if f==2:
                      r=r1
                      c=xx
                      p=1
                      break      
                  f=0   
              if p==0:
               f=0
               xx=0
               rr=0   
               s1='O'
               for r1 in range(0,3,1):
                  for h in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='X':
                          xx=h
                      elif a[h][r1]=='X':
                          break    
                      else :
                          f+=1
                  if f==2:
                      r=r1
                      c=xx
                      p=1
                      break
                  f=0  
               f=0
               xx=0
               rr=0     
               for h in range(0,3,1):
                  for r1 in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='X':
                          rr=r1
                      elif a[h][r1]=='X':
                          break     
                      else :
                          f+=1
                  if f==2:
                     c=h
                     r=rr
                     p=1
                     break
                  f=0  
              if p==0:
                  
                  if a[2][2]=='X' :
                      if a[0][0]!='O':
                          c=0
                          r=0
                      else:
                          c=2
                          r=0
                  elif a[0][0]=='X':
                      if a[2][0]!='O':
                          c=2
                          r=0
                      else:
                          c=2
                          r=2
                  else :
                      if a[0][0]!='O':
                          c=0
                          r=0
                      else:
                          c=2
                          r=2
                      
          else :
              s='X'
              f=0
              xx=0
              rr=0
              p=0
              s1='X'
              for h in range(0,3,1):
                  for r1 in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='O':
                          rr=r1
                      elif a[h][r1]=='O':
                          break    
                      else :
                          f+=1
                  if f==2:
                      c=h
                      r=rr
                      p=1
                      print(c,r)
                      break
                  f=0  
              f=0
              xx=0
              rr=0      
              for r1 in range(0,3,1):
                  for h in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='O':
                          xx=h
                      elif a[h][r1]=='O':
                          break     
                      else :
                          f+=1
                  if f==2:
                      r=r1
                      c=xx
                      p=1
                      break
                  f=0  
                     
              if p==0:
               s1='O'
               for r1 in range(0,3,1):
                  for h in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='X':
                          xx=h
                      elif a[h][r1]=='X':
                          break     
                      else :
                          f+=1
                  if f==2:
                      r=r1
                      c=xx
                      p=1
                      break
                  f=0  
               f=0
               xx=0
               rr=0     
               for h in range(0,3,1):
                  for r1 in range(0,3,1):
                      if a[h][r1]!=s1 and a[h][r1]!='X':
                          rr=r1
                      elif a[h][r1]=='X':
                          break     
                      else :
                          f+=1
                  if f==2:
                     c=h
                     r=rr
                     p=1
                     break
                  f=0  
                       
              if p==0:
                    c=random.randrange(0,3,1)
                    r=random.randrange(0,3,1)
                    while a[c][r]=='X' or a[c][r]=='O':
                     c=random.randrange(0,3,1)
                     r=random.randrange(0,3,1)
            
                    a[c][r]='X'             
              a[c][r]='X'         
                          
    a[c][r]=s          
    m=0
    n=0
    for i in range(0,7,1):
     if i%2==0:
        for j in range(0,7,1):
                print("* ",end='')
     else:
        for j in range(0,7,1):
            if j%2==0:
                print("* ",end='')
            else:
                print(a[n][m],"",end='')
                if n==2:
                    m+=1
                    n=0
                else:
                    n+=1
     print()
    p=0 
    for h in range(0,3,1):
        for r in range(0,3,1):
            if a[h][r]!=s:
                break
            elif a[h][r]==s and r==2:
                p=1
                break
    for r in range(0,3,1):
        for h in range(0,3,1):
            if a[h][r]!=s:
                break
            elif a[h][r]==s and h==2:
                p=1
                break
    if a[0][0]==s and a[1][1]==s and a[2][2]==s:
        p=1
    elif a[0][2]==s and a[1][1]==s and a[2][0]==s:
        p=1
    if p==1:
        break

    
    
if p==1:
    print(s,"WINS")
else:
    print("DRAW")
