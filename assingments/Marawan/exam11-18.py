name= "maro"
age= "29"
country= "eygpt"

print(f"hello my name {name}, my age is {age} years old , i live in {country}" )

str=f"hello my name {name}, my age is {age} years old , i live in {country}"
lst = str.split(',')
for element in lst:
    print(element ,sep= '\n')

print(name[1])

print(name[1:3])
print(name[3:6])

name="#@#@Elzero#@#@"
print(name[4:10])

num1="1"
num2="20"
num3="100"
num4="1000"
print(num1.zfill(4),num2.zfill(4),num3.zfill(4),num4.zfill(4))

name="marawan"
print(name.rjust(20,"@"))



