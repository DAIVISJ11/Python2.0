def count_notes(amount):
    notes = [2000, 500, 200, 100, 50, 20, 10]
    
    print("\nBreakdown of your money: \n")

    for note in notes:
        number = amount // note
        print(f"{note} pound notes: {number}")
        amount = amount % note

amount = int(input("Enter total amount in " \
"pounds:  "))
count_notes(amount)