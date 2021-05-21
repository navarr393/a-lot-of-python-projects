information = {'first_name':'David', 'last_name': 'Navarro', 'age':21, 'city':'Los Angeles'}
information2 = {'first_name':'Maria', 'last_name': 'Lopez', 'age':25, 'city':'Fullerton'}
information3 = {'first_name':'Steph', 'last_name': 'Kun', 'age':23, 'city':'Palos Verdes'}

people = [information, information2, information3]

for person in people:
    print(person['first_name'], person['last_name'], "is", person['age'], "and lives in the city of", person['city'],)