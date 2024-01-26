# ---------------------------------------------------1
friends = ["hager", "fatma", "ahmed", "reham", "hazem"]
print(friends)
print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])

# ---------------------------------------------------2
print("=" * 40)


print(friends[::2])
print(friends[1::2])

print("=" * 40)
# ---------------------------------------------------3
print(friends[1:4])
print(friends[1::2])
print("=" * 40)
# ---------------------------------------------------4
friends[3:5] = ["massry", "massry"]
print(friends)
# ---------------------------------------------------5
print("=" * 40)


Friends = ["OSAMA", "AHMED", "SAYED"]

Friends.insert(0, "NASSER")
print(Friends)

Friends.append("SALEM")
print(Friends)


print("=" * 40)
# ---------------------------------------------------6
Friends[0:2] = []
print(friends)

Friends.remove("SALEM")
print(friends)

print("=" * 40)
# ---------------------------------------------------7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
employees.extend(school)
friends.extend(employees)
print(friends)
# ---------------------------------------------------8
print("=" * 40)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
a = sorted(friends)
print(a)
# ---------------------------------------------------9
print("=" * 40)

print(len(friends))
# ---------------------------------------------------10
print("=" * 40)

technologies = ["Html", "CSS", "JS", "Python"]
tec = ["Django", "Flask", "Web"]
technologies.append(tec)
print(technologies[4][0])
print(technologies[4][2])
