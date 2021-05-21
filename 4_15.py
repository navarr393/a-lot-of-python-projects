UPPER_LIMIT = 1000
list1 = list(range(2,UPPER_LIMIT))
for i in list1:
    if (UPPER_LIMIT % 2) == 0:
        list1.remove(i)
for i in list1:
        if (UPPER_LIMIT % i) != 0:
            list1.remove(i)

print(list1)
print(len(list1))


