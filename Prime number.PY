num = int(input("Enter a number to check if its is prime: "))

prime = False

if num <= 1:
    print("Not a prime number")
    
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is NOT a prime number")
            break
    else:
        print(f"{num} is a prime number")
