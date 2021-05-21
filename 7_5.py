prompt = "\nEnter the age of the person"
prompt += "\nEnter quit to end the program: "

active = True
while active:
    message = input(prompt)
    message = int(message)
    if message == "quit":
        active = False
    elif message < 3:
        print("The ticket is free.")
    elif message >= 3 and message <= 12:
        print("The ticket is $10.")
    elif message > 12:
        print("The ticket is $15.")