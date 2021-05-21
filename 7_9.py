sandwitch_orders = ['chicken', 'ham', 'pbj', 'pastrami', 'pastrami', 'pastrami']
print("Our deli has ran out of pastrami.")
finished_sandwitches = []

x = 0
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')
    
for order in sandwitch_orders:
    print(f"I made your {sandwitch_orders[x]}")
    finished_sandwitches.append(sandwitch_orders[x])
    x+=1
for i in finished_sandwitches:
    print(f"Your {i} has been made and is ready for pickup.")

