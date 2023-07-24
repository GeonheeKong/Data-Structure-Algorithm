from __future__ import annotations
from typing import Any,Type
from enum import Enum
import hashlib

class Status(Enum):
    occupy=0
    empty=1
    delete=2

class Bucket:

    def __init__(self, key:Any=None,value:Any=None,stat:Status=Status.empty)->None:
        self.key=key
        self.value=value
        self.stat=stat

    def set(self,key:Any,value:Any,stat:Status)->None:
        self.key=key
        self.value=value
        self.stat=stat

    def set_status(self,stat=Status)->None:
        self.stat=stat

class OpenHash:

    def __init__(self,capacity:int)->None:
        self.capacity=capacity
        self.table=[Bucket()]*self.capacity

    def hash_value(self,key:Any)->int:
        key=key%self.capacity
    
    def rehash_value(self,key:Any)->int:
        return(self.hash_value(key)+1)%self.capacity
    
    def search_node(self,key:Any)->Any:
        hash=self.hash_value(key)
        t=self.table[hash]

        for i in range(self.capacity):
            if t.stat==Status.empty:
                break
            elif t.stat==Status.occupy:
                return t
            hash=self.rehash_value(hash)
            t=self.table[hash]
        return None
    
    def search(self,key:Any)->Any:
        t=self.search_node(key)
        if t is not None:
            return t.value
        else:
            return None
    
    def add(self,key:Any,value:Any)->bool:
        if self.search(key) is not None:
            return False
        
        hash=self.hash_value(key)
        t=self.table[hash]
        for i in range(self.capacity):
            if t.stat==Status.empty or t.stat==Status.delete:
                self.table[hash]=Bucket(key,value,Status.occupy)
                return True
            hash=self.rehash_value(key)
            t=self.table[hash]
        return False

    def remove(self,key:Any)->int:
        t=self.search_node(key)
        if t is None:
            return False
        t.set_status(Status.delete)
        return True

    

