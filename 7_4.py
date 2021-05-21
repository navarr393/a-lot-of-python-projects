prompt = "\nEnter the amount of pizza toppings you would like on your pizza:"
prompt += "\nEnter quit to end the program. "

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)