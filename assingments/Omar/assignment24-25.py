# ---------------------------------------------------1
o = ("Osama",)
print(o)
print(type(o))
# ---------------------------------------------------2
friends = ("Osama", "Ahmed", "Sayed")
f = list(friends)
f[0] = "elzero"
friends = tuple(f)

print(friends)
print(type(friends))
print(len(friends))
# ---------------------------------------------------3
nums = (1, 2, 3)
letters = ("A", "B", "C")
c = nums + letters

print(c)
print(len(c))
# ---------------------------------------------------4
T = (1, 2, 3, 4)
a, b, _, c = T

print(a)
print(b)
print(c)
