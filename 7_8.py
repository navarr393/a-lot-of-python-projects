sandwitch_orders = ['chicken', 'ham', 'pbj']
finished_sandwitches = []

x = 0
for order in sandwitch_orders:
    print(f"I made your {sandwitch_orders[x]}")
    finished_sandwitches.append(sandwitch_orders[x])
    x+=1
for i in finished_sandwitches:
    print(f"Your {i} has been made and is ready for pickup.")