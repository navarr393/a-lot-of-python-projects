list2 = list(range(1,11))
list3 = []

for cubes in list2:
    list3.append(cubes**3)
print(list3)

print("The first three items in the list are: ", list3[0:3])
print("The three items from the middle of the list are: ", list3[3:6])
print("The last three items from the list are: ", list3[6:9])
