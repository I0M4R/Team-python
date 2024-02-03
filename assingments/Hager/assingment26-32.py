# ---------------------------------------------------1

myList = [1, 2, 3, 3, 4, 5, 1]
unique_list = [1, 2, 3, 4, 5]
print(unique_list)
print(type(unique_list))
print(unique_list[:4])

# ---------------------------------------------------2

print("=" * 50)
nums = {1, 2, 3}
letters = {"A", "B", "C"}
print(nums.union(letters))
print(nums.symmetric_difference(letters))
nums.update(letters)
print(nums)

# ---------------------------------------------------3

print("=" * 50)
my_set = {1, 2, 3}
letters = {"A", "B"}
print(my_set)
print(my_set.clear())
my_set.update(letters)
print(my_set)
print(my_set.discard("C"))

# ---------------------------------------------------4

print("=" * 50)
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))

# ---------------------------------------------------5 nbmbvb
print("=" * 50)
dic = {
    "HTML": "Progress Is 90%",
    "CSS": "Progress Is 80%",
    "Python": "Progress Is 30%",
    "AI": "Progress Is 20%",
}
print("HTML", dic["HTML"])
print("CSS", dic["CSS"])
print("Python", dic["Python"])
print("AI", dic["AI"])
dic["js"] = "Progress is 10%"
print("js", dic["js"])
