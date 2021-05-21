class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def descibe_user(self):
        print(f"The user's first name is: {self.first_name}.")
        print(f"The user's last name is: {self.last_name}.")
    
    def greet_user(self):
        print(f"Hello there {self.first_name} {self.last_name}.")
    
user1 = User('David', 'Navarro')
user2 = User('John', 'Milton')

user1.descibe_user()
user1.greet_user()
print("\n")
user2.descibe_user()
user2.greet_user()