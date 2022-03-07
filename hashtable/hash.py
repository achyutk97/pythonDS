class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hashtable(self, key) -> int:
        sum = 0
        for i in key:
            sum += ord(i)
        return sum % self.MAX

    def __setitem__(self, key, data):
        index = self.get_hashtable(key)

        found = False
        for idx, kv in enumerate(self.arr[index]):
            if len(kv) == 2 and kv[0] == key:
                self.arr[index][idx] = (key, data)
                found = True

        if not found:
            self.arr[index].append((key, data))

    def __getitem__(self, key):
        index = self.get_hashtable(key)
        for kv in self.arr[index]:
            if kv[0] == key:
                return kv[1]

    def __delitem__(self, key):
        index = self.get_hashtable(key)
        for kv in self.arr[index]:
            if kv[0] == key:
                print("Deleted item", kv)
                self.arr[index].remove(kv)
                return

if __name__ == '__main__':
    obj = HashTable()
    obj['march 6'] = 123
    obj['march 17'] = 145
    obj['march 8'] = 12
    print(obj.arr)
    print(obj['march 6'])
    del obj['march 6']
    print(obj.arr)
