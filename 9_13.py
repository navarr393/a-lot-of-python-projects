import random

class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(0, self.sides))

dice = Die(6)
print("Rolling die 10 times:")
for i in range(10):
    dice.roll_die()

dice2 = Die(10)
print("Rolling die 10 times:")
for i in range(10):
    dice2.roll_die()

dice3 = Die(20)
print("Rolling die 10 times:")
for i in range(10):
    dice3.roll_die()