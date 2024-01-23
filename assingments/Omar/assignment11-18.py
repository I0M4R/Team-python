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
