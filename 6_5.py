rivers = {'Yangste':'China', 'Nile':'Egypt', 'Amazon':'Brazil'}

for river in rivers:
    print("The",river, "River runs through", rivers[river])

print('\nThe names of the rivers are:')
for key in rivers:
    print(key, "River")

print('\nThe countries of the rivers are:')
for value in rivers:
    print(rivers[value])
