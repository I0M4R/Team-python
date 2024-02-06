# ---------------------------------------------------1
print("=" * 40)


name = input("waht' your name ? \n")
name = name.capitalize().strip()
print(f"Hello {name}, Happy To See You Here.")

# ---------------------------------------------------2
print("=" * 40)

age = int(input("whats your age?"))

if age > 16:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
else:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")

# ---------------------------------------------------3
print("=" * 40)

first_name = input('your first name ? ')
last_name = input('your last name ? ')
first_name=first_name.capitalize().strip()
last_name=last_name.capitalize().strip()
print(f'Hello {first_name} {last_name:.1s}')
# ---------------------------------------------------4
print("=" * 40)
email = input("what' your Email Address ")
email = email.capitalize().strip()
print(f'Your Name Is {email[:email.index("@")]}')
print(f'Email Service Provider is {email[email.index("@")+1:]}')
print(f'Top Level Domain Is {email[email.index(".")+1:]}')
