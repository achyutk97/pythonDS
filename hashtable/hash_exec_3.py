dict = {}
with open('pem.txt', "r") as fd:
    data = fd.read().split()

for i in data:
    dict[i] = data.count(i)
print(dict["sorry"])
sorted(dict)
print(dict)