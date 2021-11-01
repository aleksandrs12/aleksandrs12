a = [0, 1, 2, 3, 4]


a[0] = a[-1]
a[1] = len(a)
b = a[0:2]
c = []
for n in b:
    c.append(n*5)

for n in range(len(b)):
    b[n]+=10
    if b[n] > 20:
        print(b[n])    


sumA = sum(a)
print(sumA, a, b, c)