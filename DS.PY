def is_disarium(n):
   
    str_n = str(n)
    total_sum = 0
    
    for i, digit in enumerate(str_n):
        
        total_sum += int(digit) ** (i + 1)
    
    return total_sum == n


number = int(input("Enter a number to check: "))
divisor = float(input("Enter a number to divide it by: "))

if is_disarium(number):
    result = number / divisor
    print(f"✨ {number} is a Disarium number!")
    print(f"Result of {number} / {divisor} = {result}")
else:
    print(f"❌ {number} is not a Disarium number.")