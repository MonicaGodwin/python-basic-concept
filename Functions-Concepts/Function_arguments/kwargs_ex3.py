def show_details(**details):
    for detail, v in details.items():
        print(detail, v)
show_details(name="Monica", age=22, course="python")