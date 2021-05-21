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

restaurant = Restaurant('Benihana', 'Japanese')
print(f"numbers served: {restaurant.number_served}")

restaurant.number_served = 15
print(f"numbers served: {restaurant.number_served}")

restaurant.set_numbers_served(20)
print(f"numbers served: {restaurant.number_served}")

restaurant.increment_numbers_served(25)
print(f"numbers served: {restaurant.number_served}")


