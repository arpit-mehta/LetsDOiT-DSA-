class MyHashSet:

    def __init__(self):
        self.size = 10000
        
        #list of lists created
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        
        #index at which we have to add in our list of lists
        i=key%self.size
        
        #add at i only if not present in i
        if key not in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key: int) -> None:
        #index at which we have to add in our list of lists
        i=key%self.size
        
        #remove only if already present
        if key in self.buckets[i]:
            self.buckets[i].remove(key)


    def contains(self, key: int) -> bool:
        i=key%self.size
        return key in self.buckets[i]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
