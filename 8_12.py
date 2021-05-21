def make_sandwich(*toppings):
    print(f"The toppings you chose on your sandwich are:\n")
    for topping in toppings:
        print(f"-{topping}")

make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('peanut butter', 'jelly', 'honey', 'strawberry')
