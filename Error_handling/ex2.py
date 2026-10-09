def check_budget(budget):
    if budget <= 0:
        raise ValueError("Invalid Input")
    else:
        print("Budget accepted")
check_budget(-100)