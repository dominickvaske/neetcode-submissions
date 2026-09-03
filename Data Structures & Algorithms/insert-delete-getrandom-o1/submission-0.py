class RandomizedSet:

    def __init__(self):
        self.myMap = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.myMap:
            return False

        self.vals.append(val)
        self.myMap[val] = len(self.vals)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.myMap:
            return False
        
        # swap element to be deleted with end element
        index = self.myMap[val]
        end = len(self.vals)-1
        swappedVal = self.vals[end]
        self.vals[index], self.vals[end] = self.vals[end], self.vals[index]

        # update index of swapped val
        self.myMap[self.vals[index]] = index

        # delete the end element by popping and removing
        self.vals.pop()
        del self.myMap[val]
        return True


    def getRandom(self) -> int:
        randIndex = random.randint(0,len(self.vals)-1)
        return self.vals[randIndex]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()