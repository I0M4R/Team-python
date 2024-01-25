name = "omar"
age = "27"
country = "alexandria"

# need to make 3rd qoute                    v Here
print(
    f""" "Hello '{name}' , How You Doing \\ "" you age is "{age}""  + and your country is: {country} """
)


print(
    f""" "Hello '{name}' , How You Doing \\ 
    "" you age is "{age}""  +
    and your country is: {country} """
)

Name = "Elzero"


print(Name[1:2])
print(Name[2:3])
print(Name[5:6])


print(Name[1:4])
print(Name[0::2])
print(Name[-2::-2])


nname = "#@#@Elzero#@#@"
print(nname.strip("#@"))


num = "9"
num = "15"
num = "130"
num = "950"
num = "1500"

print(num.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

name_onee = "OSamA"
name_twoo = "osaMA"

print(name_onee.swapcase())
print(name_twoo.swapcase())

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

print(Name.find("z"))


mssg = "I <3 Python And Although <3 Elzero Web School"

print(mssg.replace("<3", "Love" , 1))

print(mssg.replace("<3", "Love" ))

name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")

