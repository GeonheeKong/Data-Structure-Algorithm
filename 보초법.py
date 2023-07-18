from typing import Any,Sequence
import copy

def search(a=Sequence,b=Any) ->bool:
    a.append(b)
    for i in range(0,len(a)-1):
        if b==a[i]:
            return True
            break
    if b==a[len(a)-1]:
        return False
        
d=[]    
if __name__=="__main__":
    c=int(input())
    for i in range(0,c):
        d.append(int(input()))
    e=int(input())
    f=search(d,e)
    if f==True:
        print("True")
    else:
        print("False")

    
