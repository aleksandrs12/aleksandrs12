import random



def randomm(num):
    x = []
    for n in range(num):
        x.append(random.randint(0, 30))
    return x



#   1
a = []
a = randomm(5)


min = 31
for n in a:
    if n % 3 == 0 and n < min:
        min = n

if min == 31:
    print('neviens skaitlis nedalas ar 3')
else:
    print(min)





#   2
b = randomm(5)

newb = []

min = 31
i = 0

for n1 in range(len(b)):
    for n in range(len(b)):
        if b[n] < min:
            min = b[n]
            i = n
    newb.append(min)
    min = 31
    b.pop(i)







#   3
a = randomm(10)
b = randomm(10)
seen = {}
for n in a:
    seen[n] = True

for n in b:
    try:
        seen[n]
        print('True')
        break
    except:
        pass



    
#    4
a = ["cdrs", "rkt", "wx","aads", "ers","eeeer","sss", 'hiasd', 'uhloasd', 'enkl']
patskani = {'a': True, 'e': True, 'i': True, 'u': True, 'o': True}
num = 0

for n in a:
    for n1 in n:
        try:
            patskani[n1]
            num += 1
        except:
            pass
    if num > 2:
        print(n)
    num = 0
print('')




for n in a:
    if len(n) > 2 and n[-1] == 's':
        print(n)



