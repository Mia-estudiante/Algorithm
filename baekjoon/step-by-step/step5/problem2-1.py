not_self = list()
for i in range(1, 10000):
    d = int(str(i))+sum(list(map(int, list(str(i)))))
    not_self.append(d)
yes_self = [x for x in range(1,10000) if x not in not_self]

for n in yes_self: print(n)