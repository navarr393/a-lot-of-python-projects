favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

poll = ['jen', 'john', 'maria', 'sarah']

for value in poll:
    if value in favorite_languages:
        print(value, "thank you for taking the poll.")
    else:
        print(value, "I invite you to take the poll.")
        