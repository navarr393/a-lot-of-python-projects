class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def descibe_user(self):
        print(f"The user's first name is: {self.first_name}.")
        print(f"The user's last name is: {self.last_name}.")
    
    def greet_user(self):
        print(f"Hello there {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('david', 'Navarro')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.descibe_user()
print(f"Your login attempts are: {user.login_attempts}")

#reseting 
user.reset_login_attempts()
print(f"Your login attempts have been reset to {user.login_attempts}")