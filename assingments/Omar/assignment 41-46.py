# ---------------------------------------------------1
# print("=" * 40)

# num1 = int(20)
# num2 = int(40)

# print(int(num1 + num2))
# print(int(num1 * num2))
# ---------------------------------------------------1-1
print("=" * 40)
num1 = int(input("First Number :  ").strip())
num2 = int(input("Secend Number :  ").strip())
operation = input("Operation (+, -, *, /, %): ").strip()

if operation == "+":
    result = num1 + num2
    print(f"result : {result}")
elif operation == "-":
    result = num1 - num2
    print(f"result : {result}")
elif operation == "*":
    result = num1 * num2
    print(f"result : {result}")
elif operation == "%":
    result = num1 % num2
    print(f"result : {result}")
elif operation == "/":
    result = num1 / num2
    print(f"result : {result}")
else:
    print("miss click")

# ---------------------------------------------------2
print("=" * 40)

age = int(input("Whats your age ? "))

if age >= 16:
    print("App is Suitable For You")
else:
    print("app is not suitable for you")

# ---------------------------------------------------3
print("=" * 40)

age = int(input("whats your age : "))
months = age * 12
weeks = months * 4
Days = age * 365
hours = Days * 24
mint = hours * 60
secs = mint * 60


if age >= 10 and age <= 100:
    print(
        f"Months : {months}\nWeeks : {weeks:,}\nDays : {Days:,}\nHours : {hours:,}\nMintes : {mint:,}\nSec : {secs:,}"
    )
else:
    print("out of range")
# ---------------------------------------------------4
print("=" * 40)

countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
country = input("Whats Your Country ").strip().capitalize()
price = 100
discount = 30
Sale = price-discount

if country in countries:
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${Sale}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
# ---------------------------------------------------5
print("=" * 40)