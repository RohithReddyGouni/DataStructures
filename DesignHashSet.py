class MyHashSet:

    def __init__(self):
        self.size=10000;
        self.bucket=[None]*self.size;

    def hashValue(self,key):
        return key%self.size;

    def add(self, key: int) -> None:
        hv=self.hashValue(key);
        if self.bucket[hv]== None:
            self.bucket[hv]=[key];
        else :
            self.bucket[hv].append(key);

    def remove(self, key: int) -> None:
        hv=self.hashValue(key);
        if self.bucket[hv]!=None:
            while key in self.bucket[hv]:
                self.bucket[hv].remove(key);

    def contains(self, key: int) -> bool:
        hv=self.hashValue(key);
        if self.bucket[hv]!=None:
            return key in self.bucket[hv];
        return False;




# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
