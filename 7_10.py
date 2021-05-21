vacations = {}

name = input("What is your name?")
response  = input("What country would your first dream vacation would be in?")
response2 = input("What is the second coutry of your dream vacation?")

vacations[name] = response
vacations[name] = response

print("\n--- Poll Results ---")
for name, response in vacations.items():
    print(f"{name} would like to go to {response} and {response2} for a dream vacation.")

