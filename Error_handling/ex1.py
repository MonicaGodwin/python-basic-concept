def get_age():
    try:
        age = input("Enter age: ")
        converted = int(age)
        print(f"Age is {converted}")
    except ValueError:
        print("Age must be a number")
get_age()