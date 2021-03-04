"""EXERCISE"""

num = 0
while  num<=10:
    print(num)
    num +=1

#2 ------------------------------------------------not done
# for i in range(1,2):
#     print(i)
#     for j in range(5):
#         print(i,j)
#


#3
print('\n')
#print(1+2+3+4+5+6+7+8+9+10)
num = int(input('enter number: '))
def addition(num):
    total= 0
    for i in range(num+1):
        total = total + float(i)
    print(total)

addition(num)

#4
mul = int(input('enter number: '))
for i in range(mul+1):
    print(mul,' * ' ,i ,'=', 12*i)
    if i ==12:
        break

#5
var = input('enter a number: ')
count= 0
for i in var:
    count = count + 1
print(count)

print('\n')
6
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in list1:
    if i%5 == 0:
        print(i)
    if i>=150:
        break

print('\n')
#7 ----------------------------------------------not done
# lis2 = [10,20,30,40,50]
# for i in lis()
#     lis4 = []
#     lis4.index(len(lis2)-1)
#
#     print(lis4)


#8
def fact(numb):
    if numb ==0 or numb == 1:
        res = 1
        return res
    elif numb > 0:
        res = numb * fact((numb-1))
        return res

print(fact(4))

#9
test = True
while test:
    for i in range(11):
        if i <5:
            print(i *'*')
        if i >= 5:
            print('*'*(10-i))
    if i == 10:
        test = False
#

#10
def calculation(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    return add,sub

print(calculation(1,2))


#11
def showEmployee(name , salary = 9000):
    print('{}, your salary is {}'.format(name,salary))

showEmployee('ilesanmi', 5000)

#12
def calculateArea(radius, diameter):
    return (3.142 * radius *radius)

print(calculateArea(7,5))


