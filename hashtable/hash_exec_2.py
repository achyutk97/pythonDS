stock_prices = []
with open("nyc_weather.csv","r") as f:
    i = 0
    for line in f:
        if i == 0:
            i = 1
            continue
        tokens = line.split(',')
        day = tokens[0]
        price = int(tokens[1].replace('\n', ""))
        stock_prices.append([day,price])

print(stock_prices)


class Hashtable:
    def __init__(self) -> None:
        self.Max_size = 1000
        self.arr = [[] for i in range(self.Max_size)]

    def getHash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.Max_size
    
    def __setitem__(self, key, val):
        index = self.getHash(key)

        FOUND = False
        for i, value in enumerate(self.arr[index]):
            if len(value) == 2 and value == val:
                self.arr[index][i] = (key, val)
                FOUND = True

        if not FOUND:               
            self.arr[index].append((key,val))

    def __getitem__(self, key):
        index = self.getHash(key)

        for i in self.arr[index]:
            if i[0] == key:
                return i[1]

if __name__ == '__main__':
    hasattr = Hashtable()
    # for j in range(len(stock_prices)):
    for i in stock_prices:
        hasattr[i[0]] = i[1]
    print(hasattr['Jan 9'])
    print(hasattr['Jan 4'])