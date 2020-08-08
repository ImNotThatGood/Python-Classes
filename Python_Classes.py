# Class
class Robot:
    # Constructor
    def __init__(self, name, color, weight):
        # Attributes
        self.name = name
        self.color = color
        self.weight = weight

    # Method
    def introduceSelf(self):
        print("My name is {}, I like the color {}, and my weight it {} pounds".format(self.name, self.color, self.weight))

# Class
class Person:
    # Constructor
    def __init__(self, name, personality, isSitting):
        # Attributes
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    
    # Method
    def sit_down(self):
        # Attribute
        self.isSitting = True
    
    # Method
    def stand_up(self):
        # Attribute
        self.isSitting = False

# Objects
robot1 = Robot('Tom', 'red', 30)
robot2 = Robot('Jerry', 'blue', 40)
p1 = Person('Alice', 'aggressive', False)
p2 = Person('Becky', 'talkative', True)

# Defining a new attribute in p1/p2 object and sets it to the robot1/robot2 objects
p1.robot_owned = robot2
p2.robot_owned = robot1

# Running a method by calling the p1 object, the attribute, the robot1 object (which now refrences the Robot class), and then finally to the method
p1.robot_owned.introduceSelf()
p2.robot_owned.introduceSelf()