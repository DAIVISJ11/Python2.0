class Robot:
    def __init__(self, name):
        self.name = name 

    def greet(self):
        
        return f"Hello, I am {self.name}!"


my_robot = Robot("Terminator")
print(my_robot.greet())  