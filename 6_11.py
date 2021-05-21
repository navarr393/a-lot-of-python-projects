cities = {'Los Angeles':{'country':'United States', 'population':3.99, 'fact':'Popular for Hollywood movies.'},
          'Guadalajara':{'country':'Mexico', 'population':1.3, 'fact':'Popular for tequila.'},
          'Tokyo':{'country':'Japan', 'population':37.3, 'fact':'Popular for Anime.'}}

for city, info in cities.items():
    print("\n"+city)

    for key in info:
        print(key + ':',info[key])