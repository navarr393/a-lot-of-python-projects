class Restaurant:
    def __init__(self, restaurant_name, couisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = couisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    def open_restaurant(self):
        print("The restaurant is currently open!")
    
restaurant_ = Restaurant('Benihana', 'Japanese')
restaurant1 = Restaurant('McDonalds', 'fast food')
restaurant2 = Restaurant('Shake Shack', 'Burgers')
#print(f"The restaurant's name is {restaurant_.restaurant_name}.")
#print(f"The restaurant's type is {restaurant_.cuisine_type}.")

restaurant_.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

#restaurant_.open_restaurant()

