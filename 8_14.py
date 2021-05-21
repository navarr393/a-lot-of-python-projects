def make_car(manufacturer, name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['name'] = name
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)