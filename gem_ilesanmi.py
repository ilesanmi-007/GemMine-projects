#Assignment 1

'''declaring varibles with suitable names'''

first_name = 'samson'  #firstname isnt surname, shey?
last_name = 'ilesanmi'
sex = 'male'
discordUsername = 'ilesanmi'   #camel case
year_of_birth = 1997    #snake case
fav_num = 0
fav_color = 'black'
matric_num = 170403071
StateOfOrigin = 'osun state'  #Pascal case

'''best friend = bfriend
closest friend = cfriend
most disliked friend = dfriend '''

bfriend, cfriend, dfriend = 'samuel', 'samuel', 'nobody'

#if best friend == closest friend

bfriend = cfriend = 'samuel'

#introducing myself

print('hey.. \n '
      'my name is '+ first_name+ '. and my surname is '+ last_name +
      '.\n I am a ' + sex + '.\n My discord username is '+ discordUsername+
      '. \n I was born in the year '+str(year_of_birth)+ ', My favourite number is '+ str(fav_num)+
      '.\n And also, my favourite color is '+ fav_color
+ '.\n my matric number is '+str(matric_num)+ ' and i hail from ' + StateOfOrigin +
' \nThanks!')


#mathematics
yob_minus_5 = year_of_birth - 5
print(float(yob_minus_5))

#using just pure python
result_1 = 10**100
print(complex(result_1)) #print as complex

result_2 = 10//3
print(result_2)   #floor division

result_3 = 62%3
print(result_3)   #output remainder

result_4 = 6 * 80
print(result_4)    #multiplication

result_5 = 20 - 9
print(result_5)   #subtraction

result_6 = 1.2 ** 0.3
print(int(result_6))   #power

#CHECK FOR DATA TYPE

print(type(99.99))
print(type(34))
print(type(-768.3))
print(type("56"))
print(type('67'))
print(type('seventy'))
print(type("-87"))
print(type(-87))

#an intro about python
'''
python is a simple programming language. 
it is an interpreted, object-oriented, high level programming language
with dynamic semantics
python can be used for many things, such as data science, ML, Web design
and so on
'''

#MEDIUM ARTICLE LINK:
link = 'https://ilesanmi007.medium.com/python-variable-names-and-number-data-types-ee0040754520'