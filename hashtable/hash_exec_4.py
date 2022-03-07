class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arry = [None for i in range(self.MAX)]

    def getHashKey(self, key):
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.MAX

    def __setitem__(self, key, data):
        h = self.getHashKey(key)
        if self.arry[h] is None:
            self.arry[h] = (key, data)
        else:
            h = self.getEmptySlot(key, h)
            self.arry[h] = (key, data)
    
    def getProbrange(self, key):
        list = [*range(key, len(self.arry))] + [*range(0, key-1)]
        print(list)
        return list

    def getEmptySlot(self, key, index):
        prob_range = self.getProbrange(index)
        for prob_index in prob_range:
            if self.arry[prob_index] is None:
                return prob_index
            if self.arry[prob_index][0] == key:
               
                return prob_index
        raise Exception("Hash is full")

    def __getitem__(self, key):
        h = self.getHashKey(key)
        if self.arry[h] is None:
            return
        prob_range = self.getProbrange(h)
        for prob_index in prob_range:
            element = self.arry[prob_index]
            if element is None:
                return 
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        h = self.getHashKey(key)
        prob_range = self.getProbrange(h)
        for prob_index in prob_range:
            if self.arry[prob_index] is None:
                return
            if self.arry[prob_index][0] == key:
                self.arry[prob_index] = None
        print(self.arry)

if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] =  88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    print(t["dec 1"])
    print(t["march 33"])
    t["march 33"] = 999
   
    print(t['march 17'])
    print(t["march 33"])
    t["april 1"]=87
    t["april 2"]=123
    t["april 3"]=234234
    t["april 4"]=91
    t["May 22"]=4
    t["May 7"]=47
 
    del t["april 2"]
    t["Jan 1"]=0
    print(t.arry)