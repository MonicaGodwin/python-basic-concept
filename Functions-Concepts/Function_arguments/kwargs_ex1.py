def show_info(**details):
    for key, value in details:
        print(key, value)
print(show_info(name="Monica", age=22, course="Python"))