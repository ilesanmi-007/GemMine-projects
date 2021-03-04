#assignment 3

name = input("enter your name, please: ")
age = int(input("enter your age too: "))
sex = input("enter your gender: ")
print("\nthank you!")

print("--" *30)
print('Hi..{}, you\'re welcome.\n'
      'In 10 years time, you\'ll be {} years old\n'
      'and very old by then'.format(name,(age + 10)))


print("--" *30)

fruits = input('enter 2 or more favourite fruits separated by a comma: ')
print(fruits.split(','))

fav_num = input('enter 2 or more favourite numbers separated by a comma: ')
fav_num_list = fav_num.split(',')
fav_num_list.sort(reverse=True)
print(fav_num_list)

print('\n THANK YOU!')