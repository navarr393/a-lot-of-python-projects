

# put your function here
def makeusername(first_name, last_name):
    
    return first_name[:3]+last_name[:3]+'2'

firstname = input("Give me a first name: ")
lastname = input("Give me a last name: ")

print("Computer System name is:", makeusername(firstname,lastname))