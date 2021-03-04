
# a = [[1,2], [3,4]]
# print(a)
# for i,j in a:
#     print(i,j, end = '\n') #i is column...j is row

print('hiii...welcome to your GP calculator...'
      'Please, fill in details accordingly.\n\n')

name = input('enter name: ')
matric_num = input('matric number: ')
dept = input('enter the department you are: ')
main = int(input('enter number of main courses'
                 '(not elective): '))
print('\n\n ')
a = []
b = []
c = []
for i in range(main):
    course_code = input('enter course code: ')
    units = int(input('enter number of unit of course entered: '))
    grade = input('enter your grade(A,B or C): ')
    print('\n')
    a.append(course_code)
    b.append(units)
    #c.append(grade)
    if grade == 'a' or grade == 'A':
        grade_point = 5
        c.append(grade_point)
    elif grade == 'b' or grade == 'B':
        grade_point = 4
        c.append(grade_point)
    elif grade == 'c' or grade == 'C':
        grade_point = 3
        c.append(grade_point)
    elif grade == 'd' or grade == 'D':
        grade_point = 2
        c.append(grade_point)
    elif grade == 'e' or grade == 'E':
        grade_point = 1
        c.append(grade_point)
    elif grade == 'f' or grade == 'F':
        grade_point = 0
        c.append(grade_point)
    else:
        print('You have entered an incorrect grade')
total = [ ]
TCP = 0
GP = 0
total_units = 0 #total number of Units

for i in range(main):
    total.append(c[i] * b[i])
    TCP = TCP + total[i] #total credit point
    total_units = total_units + b[i]
    GP = TCP / total_units


# print('this is total units', total_units)
# print('this is GP:', GP)

print('here is your data: ')
print('course  |   unit    |  total')
for i in range(1):
    for j in range(main):

        print(' {}  |   {}   |   {}'.format(a[j],b[j], grade_point))

if GP >= 4.50:
    greetings = ' Excellent job!'
    Gp_description = ' First Class Honors.'
elif 3.50<= GP < 4.49:
    greetings = ' Very good job!'
    Gp_description = 'Second Class Upper Division.'
elif 2.40 <= GP < 3.49:
    greetings = ' Good job!'
    Gp_description = ' Second Class Lower Division.'
elif 1.50 <= GP < 2.39:
    greetings = '  Fair job!'
    Gp_description = 'Third Class.'
elif 1 <= GP < 1.49:
    greetings = 'Pass Degree. Bad job!'
    Gp_description = ''
elif 0 <= GP <0.99:
    greetings = 'Failure!!!!'
    Gp_description = 'Very bad job'

print('\n\n{},\n At the end of the Semester alone,\n {} with the matric number '
      '{}\n from {} has a total grade of {}'
      ' and is in {}.\n '
      '{} again.'.format(greetings,name, matric_num, dept, GP,Gp_description,greetings))