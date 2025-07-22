############types-- type, str ##############
name='John'
print(type(name)) 
age=25
#print('my age is:'+ age) #error bcz string + int cannot
print('my age is:' + str(age))

########## math -- len,count
password='123adss'
print(len(password))

text="""
python is more fun.
i love python
Python is powerful
"""
print( text.count('python'))

############## transformation -- replace(),concat two string-'+', fstring,split,*

date='2025/12/03'
print(date.replace("/","-"))

num='+49 (176) 123-4567'
print(num.replace('+','00').replace('(','').replace('-','').replace(' ','').replace(')',''))

#concat

file_path='c:users/downloads/'
file_name='students.csv'
print(file_path + file_name)

## f- string
name='sam'
age=34
is_student = False

print(f"my name is {name} and my age is {age} and student status is {is_student}")

####### split
timestamp="2025-12-12 14:32"
print(timestamp.split(':'))

#multiply

print("hi"*3)


######################extraction - extract[]
text='Python'
print(text[0:5:2])

#############clean -lstrip,rstrip,strip

name='     ram ##'
print(name)
print(name.lstrip())
print(name.strip('##'))

############## search  - startswith(),endswith(),find()

text4='314-5859403'

print(text4.startswith('314'))
print(text4.find('-'))


#########validation

country = "USA"
num5='82773%93'
print(country.isalpha())
print(num5.isnumeric())