def even_numbers():
    for num in range(2, 11):
        if num % 2 == 0:
            yield num
result = even_numbers()
for rst in result:
    print(rst)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))