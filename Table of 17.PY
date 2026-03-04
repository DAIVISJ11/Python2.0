number = int(input('enter a number to print its times table:'))
print(f"table of {number}")

for i in range(1, 11):
    x = number * i
    print(f'{number} x {i} = {x}')