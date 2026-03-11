class Parrot:
    species = "Bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

John = Parrot("John", 10)
bandit = Parrot("bandit", 3)

print(f"{John.name} is a {John.species} and he is {John.age} years old")
print(f"{bandit.name} is a {bandit.species} and he is {bandit.age} years old") 