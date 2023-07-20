from __future__ import annotations
from typing import Any,Type
import hashlib
class Node:
    def __init__(self,key:Any,value:Any,next:Node)->None:
        self.key=key
        self.value=value
        self.next=next

class Hash:
    def __init__(self,capacity:int)->None:
        self.capacity=capacity
        self.table=[0]*capacity
    
    def hash_value(self,key:Any)->int:
        return key%self.capacity
    
    def search(self,key:Any)->Any:
        h=self.hash_value(key)
        t=self.table[h]

        while t is not None:
            if t.key==key:
                return t.value
            t=t.next
        return None

    def add(self,key:Any,value:Any)->bool:
        h=self.hash_value(key)
        t=self.table[h]

        while t is not None:
            if t.key==key:
                return False
            t=t.next
        addNode=Node(key,value,self.table[h])
        self.table[h]=addNode
        return True

    def remove(self,key:Any)->bool:
        h=self.hash_value(key)
        t=self.table[h]
        tt=None
        while t is not None:
            if t.key==key:
                if tt is None:
                    self.table[h]=t.next
                else:
                    tt.next=t.next
                return True
            tt=t
            t=t.next
        return False


    def dump(self)->None:
        for i in range(self.capacity):
            t=self.table[i]
            print(i,end='')
            while t is not None:
                print(f' -> {t.key} ({t.value})',end='')
                t=t.next
            print()

