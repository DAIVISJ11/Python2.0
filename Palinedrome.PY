name = input("Enter a word to check if it is a palindrome :")

def is_palindrome(name):
    return name == name[::-1]
if is_palindrome(name):
    print(f"Yes! the word {name} is a palindrome")
else:
    print(f"No! the word {name} is not a palindrome")