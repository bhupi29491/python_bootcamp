# Car names are proper names, so the names of most cars should be printed
# in title case. However, the value 'bmw' should be printed in all uppercase.
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
