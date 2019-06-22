countries = ['Turkey', 'USA', 'France', 'Germany', 'Italy']
capitals = ['Ankara', 'Washington D.C.', 'Paris', 'Berlin', 'Rome']

# Enumarate function returns a list of tuples
# First element is the index and the second one is
# the current element of the list
for index, country in enumerate(countries):
    capital = capitals[index]
    print('Capital city of {} is {}'.format(country, capital))
