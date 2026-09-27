def calculate_total(**prices):
    total_amount = 0
    for total, value in prices.items():
        total_amount += value
    return total_amount
    
print(calculate_total(
    rice=7000,
    beans=3000,
    milk=2000
))

