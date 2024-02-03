# ---------------------------------------------------1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_listprint = [1, 2, 3, 4, 5]

print(unique_listprint)
print(type(unique_listprint))
print(unique_listprint[0:4])
# ---------------------------------------------------2
print("=" * 40)

nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums.union(letters))
print(nums.symmetric_difference(letters))
nums.update(letters)
print(nums)
# ---------------------------------------------------3
print("=" * 40)

my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)
my_set.discard("C")
# ---------------------------------------------------4
print("=" * 40)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
# ---------------------------------------------------5
print("=" * 40)

Dict = {
    "HTML": "Progress is 90% ",
    "CSS": "Progress is 80% ",
    "Python": "Progress is 30% ",
    "AI": "Progress is 20%",
}
print("HTML", Dict["HTML"])
print("CSS", Dict["CSS"])
print("Python", Dict["Python"])
print("AI", Dict["AI"])
Dict["Omar"] = "Progress is 20%"
print("Omar", Dict["Omar"])
