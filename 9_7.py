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

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilages = ['can add post', 'can delete post', 'can ban user', 'can mute user']
    
    def show_privilages(self):
        print("The admins privilages are:")
        for privilage in self.privilages:
            print(privilage)

user = Admin('David', 'Navarro')
user.show_privilages()