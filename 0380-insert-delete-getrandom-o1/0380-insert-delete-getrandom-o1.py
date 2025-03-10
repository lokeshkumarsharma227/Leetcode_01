class RandomizedSet:

    def __init__(self):
        self.mp = {} 
        self.list = []
        

    def insert(self, val: int) -> bool:
            if val in self.mp:
                return False
            self.mp[val] = len(self.list)
            self.list.append(val)
            return True
        

    def remove(self, val: int) -> bool:
                if val not in self.mp:
                    return False
                last_element=self.list[-1]
                idx = self.mp[val]
                self.list[idx]=last_element
                self.mp[last_element] =  idx
                self.list.pop()
                del self.mp[val]
                return True

        
    def getRandom(self) -> int:
            return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()