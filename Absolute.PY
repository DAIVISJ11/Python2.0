num = int( input("Enter a number to find its absolute value:"))

def absolute_value(num):
    if num>=0:
       return num
    else:
        return -num
    
print(f'absolute value of {num} is ', absolute_value(num))