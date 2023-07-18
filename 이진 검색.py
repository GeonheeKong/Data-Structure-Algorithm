from typing import Any,Sequence
def bin_search(a=Sequence,b=Any)->int:
    pl=0;pr=len(a)-1
    while True:
        pc=(pl+pr)//2
        if a[pc]<b:
            pl=pc+1            
        elif a[pc]>b:
            pr=pc-1            
        else:
            return pc
            break
        return -1
lst=[]
if __name__=="__main__":
    num=int(input())
    for i in range(0,num):
        lst.append(int(input()))
    lst.sort() #배열의 원소는 일정한 규칙대로 정렬되어 있어야 함(오름차순)
    key=int(input())
    idx=bin_search(lst,key)
    
    if idx==-1:
        print("False")
    else:
        print("검색값은 x[%d]이다"%idx)
    