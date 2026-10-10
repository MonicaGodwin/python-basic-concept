class InvalidBudgetError(Exception):
    pass

def check_budget(budget):
    if budget <= 0:
        raise InvalidBudgetError("Invalid Input")

    print("Budget accepted")
try:
    check_budget(-100)
except InvalidBudgetError as e:
    print(e)
