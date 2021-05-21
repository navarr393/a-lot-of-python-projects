import matplotlib.pyplot as plt
cubes = list(range(1,5001))

cubes2 =[]

for i in cubes:
    cubes2.append(i**3)

fig, ax = plt.subplots()
ax.plot(cubes2)
plt.show()