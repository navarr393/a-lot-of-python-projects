class Restaurant:
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = couisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is currently open!")

    def set_numbers_served(self, number):
        self.number_served = number

    def increment_numbers_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, couisine_type):
        super().__init__(restaurant_name, couisine_type)
        self.flavors = ['vanilla', 'chocolate', 'rocky road', 'strawberry',]
    
    def display_flavors(self):
        print("The flavors are:")
        for flavor in self.flavors:
            print(f"{flavor}")

icecream = IceCreamStand('Bobs Freeze', 'ice cream')
icecream.display_flavors()
