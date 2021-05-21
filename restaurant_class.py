class Restaurant:
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = couisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is currently open!")
 