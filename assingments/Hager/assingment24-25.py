# ---------------------------------------------------1
name = ("hager",)
print(name)
print(type(name))

print("=" * 50)
# ---------------------------------------------------2
friends = ("hager", "fatma", "hazem")
a = list(friends)
a[0] = "masry"
friends = tuple(a)
print(friends)
print(type(friends))
print(len(friends))

print("=" * 50)
# ---------------------------------------------------3
num = (1, 2, 3)
alpha = ("A", "B", "C")
a = list(num)
b = list(alpha)
a.extend(b)
num = tuple(a)
alfa = tuple(b)
print(num)
print(len(num))

print("=" * 50)
# ---------------------------------------------------4
myTuple = (1, 2, 3, 4)
a, b, _, c = myTuple
print(a, b, c)
