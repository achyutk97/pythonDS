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
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        found = False
        for idx, val in enumerate(self.arr[h]):
            if len(val) == 2 and val == value:
                self.arr[h][idx] = (key, value)
                found = True
        
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)

        for idx in self.arr[h]:
            if idx[0] == key:
                return idx[1]

if __name__ == '__main__':
    h = Hashtable()
    for i in stock_prices:
        h[i[0]] = i[1]
    sum = 0
    for i in range(7):
        sum += h[stock_prices[i][0]]
    avg = sum/7
    print(avg)
    list = []
    for i in range(10):
        list.append(h[stock_prices[i][0]])
    print(list)
    print(max(list))

