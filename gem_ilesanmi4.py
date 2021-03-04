#python exercises on tuples, set and dictionaries.

#1- printing the first item

fruits = ('apple', 'banana', 'cherry')
print(fruits[0])

#printing number of items
print(len(fruits))

#printing last item with negative index

print(fruits[-1])

#printing 3rd, 4th, and 5th
fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(fruits[3:6])

#add orange to set
fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)

#add a list to set
fruits = {'apple', 'banana', 'cherry'}
more_fruits = ['orange', 'mango', 'grapes']
fruits.update(more_fruits)
print(fruits)

#remove from a set
fruits = {'apple', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)

#using discard to remove banana
fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')
print(fruits)

#using get to get a value from a dictionary
car = {
    'brand': 'ford',
    'model': 'Mustang',
    'year': '1964'
}
print(car.get('model'))

#change the year to 2020
car.update({'year': 2020})
print(car)

#adding key and value to dict
car.update({'color': 'red'})
print(car)

#using pop to remove model
car.pop('model')
print(car)

#clearing the dictionary
car.clear()
print(car)

print('\n\n\t THANK YOU')


#medium link:
medium_link = 'https://ilesanmi007.medium.com/python-list-sets-tuples-and-dictionaries-37104a4bc54c'
