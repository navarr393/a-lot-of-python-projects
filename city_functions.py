def get_formatted_name(city, country, population):
    """Generate a full name"""
    if population:
        full_name = f"{city}, {country}"
        info = full_name.title() + f' - population {population}'
    else:
        full_name = f"{city}, {country}"
        info = full_name.title()
    return info

#print(get_formatted_name(city = 'santiago', country = 'chile', population = 100000))
    