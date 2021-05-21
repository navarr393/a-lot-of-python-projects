def city_country(city, country):
    city_and_country = f"{city}, {country}"
    return city_and_country.title()

city1=city_country('Guadalajara', 'Mexico')
city2=city_country('Tokyo', 'Japan')
city3=city_country('Barcelona', 'Spain')

print(city1)
print(city2)
print(city3)
