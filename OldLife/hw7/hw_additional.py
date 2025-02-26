#1. sort list of dicts by key ‘type’,
#2.sort list of dicts by value of key ‘year’.

vehicles = [
    {'type': 'Sedan', 'weight': 1500, 'year': 2000},
    {'type': 'SUV', 'weight': 2000, 'year': 1999},
    {'type': 'Pickup', 'weight': 2500, 'year': 2011},
    {'type': 'Minivan', 'weight': 1600, 'year': 1999},
    {'type': 'Van', 'weight': 2400, 'year': 2012},
    {'type': 'Semi', 'weight': 13600, 'year': 2015},
    {'type': 'bycicle', 'weight': 7, 'year': 2012},
    {'type': 'Motocycle', 'weight': 100, 'year': 2008}
    ]

#use sorted() to make a new list
#sort() is case sencitive metod, so if we use also lower() to have corect abc sort in result
type_sorted_vehicles = sorted(vehicles, key = lambda d_key: d_key['type'].lower())
print(type_sorted_vehicles)

year_sorted_vehicles = sorted(vehicles, key = lambda d_key: d_key['year'])
print(year_sorted_vehicles)