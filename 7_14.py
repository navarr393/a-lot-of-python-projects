famous_people = [{'Name': 'Naruto Uzumaki', 'Birth Date': 'October 10, 1994', 'Birth Place': 'Japan', 'Famous quote': 'Thats my ninja way!'},
                 {'Name': 'Kobe Bryant', 'Birth Date': 'August 23, 1978', 'Birth Place': 'Philadelphia', 'Famous quote': 'I focus on one thing and one thing only'},
                 {'Name': 'Cristiano Ronaldo', 'Birth Date': 'February 5, 1985', 'Birth Place': 'Portugal', 'Famous quote': 'Your love makes me strong, your hate makes me unstoppable'}
                 ]

print('{:<10} {:>20} {:>30} {:>40}'.format('Name', 'Birth Date', 'Birth Place', 'Famous quote'))
print('{:->130}'.format(''))

for people in famous_people:
        print(people['Name'], '{:>20}'.format(people['Birth Date']), '{:>20}'.format(people['Birth Place']), '{:>60}'.format(people['Famous quote']))