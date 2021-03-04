data = input('enter arithmetic to be performed: ')
#data = '3 + 4 + 5 + 4 +5 +6 + 4000'
f =[ ]
y = data.split('+')
#print('this is y: ', y)
for i in y:
    #print(i)
    v = float(i)
    #print('this is float of j: ', i)
    f.append(v)
    #print(f)
cc = 0
total = 0
while cc < len(f):
    total = total + f[cc]
    cc = cc+ 1
print(total)
