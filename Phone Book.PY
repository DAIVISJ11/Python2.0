import sys
FIELDS = ["Name*", "Number*", "Email*", "DOB*", "Category*"]

def get_contact():
    contact = {}
    for field in FIELDS:
        while True:
            value = input(f"Enter {field}: ").strip()

            if"*" in field and value == "":
                print(f"{field} is manditory!")
                continue

            if field == "Number" and not value.isdigit():
                print("Invalid number! Please enter digits only. ")
                continue
            break

def initial_phonebook():
    n = int(input("How many contacts:"))
    pb = []
    for i in range(n):
        print(f"\n contact {i+1}")
        pb.append(get_contact())
    return pb

def display_all(pb):
    if not pb :
        print("Phonebook is Empty")
    else:
        for contact in pb:
            print(contact)

def add_contact(pb):
    pb.append(get_contact())
    return pb

def remove_contact(pb):
    name = input("Enter name to remove: ")
    for contact in pb:
        if contact["Name*"]==name:
            pb.remove(contact)
            print("Removed successfully")
            return pb
    
        print("Contact not found!")
        return pb
    
        
def  search_contact(pb):
    name = input("Enter name to search: ")
    results = [c for c in pb if c["Name*"] == name]

    if results:
        display_all(results)
    else:
        print("Not found")



def Menu():
    print("\n1.Add 2.Remove 3.Delete All 4.Search 5.Display 6.Exit")
    while True:
        try:
            return int(input("choice :"))
        except ValueError:
            print('please enter a valid numer(1-6)')

def main():
    pb = initial_phonebook()

    while True:
        ch = Menu()

        if ch == 1:
            add_contact(pb)
        elif ch == 2:
            remove_contact(pb)
        elif ch == 3:
            pb.clear()
            print("All contact deleted")
        elif ch == 4:
            search_contact(pb)
        elif ch == 5:
            display_all(pb)

        elif ch == 6 :
            print('Goodbye!')
            break
        else:
            print("invalid choice. Try again")
main()

