data = input('enter arithmetic to be performed: ')
#data = '3 + 4 + 5 + 4 +5 +6 + 4000'
#data = '3+4'
x = data.split(' ')
count = 0
f =[ ]
#print(x)
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
    cc = cc + 1
print(total)


# for i in x:
#     if i == '+':
#         #count = + 1
#         for j in x:
#             #count =+ 1
#             #float (j)
#             if j == '+':
#                 continue
#             else:
#                 print('this is j: ', j)
#                 v = float(j)
#                 print('this is float of j: ', j)
#                 f.append(v)
#             if len(f) >= len(x):
#                 print('hiii\n')
#                 break
#             print('this is f:', f)
#             #print(x)
#             count = + 1
#             print('this na count: ', count)
#         result= f[count-1] + f[count]
#         print(result)
