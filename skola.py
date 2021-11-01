#     1
a = [0, 1, 2, 3, 4]


#     2
a[0] = a[-1]


#     3
a[1] = len(a)


#     4
b = a[0:2]


#     5
c = []
for n in b:
    c.append(n*5)

    
#     6
for n in range(len(b)):
    b[n]+=10
    if b[n] > 20:
        print(b[n])    


#     7
sumA = sum(a)
print(sumA)
