# ---------------------------------------------------1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0])
print(friends.pop(0))

print(friends[-1])
print(friends.pop(-1))
# ---------------------------------------------------2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[::2])
print(friends[1::2])
# ---------------------------------------------------3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:-1])
print(friends[3:])
# ---------------------------------------------------4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[3:5] = ["elzero", "elzero"]
print(friends)
# ---------------------------------------------------5
friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)
# ---------------------------------------------------6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends[0:2] = []
print(friends)

friends.remove("Salem")
print(friends)
# ---------------------------------------------------7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

friends.extend(employees)
friends.extend(school)
print(friends)
# ---------------------------------------------------8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)
# ---------------------------------------------------9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))
# ---------------------------------------------------10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[4][0])
print(technologies[4][2])
