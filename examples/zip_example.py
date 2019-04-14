# zip function example

names = ["Rose Tyler", "Martha Jones", "Donna Noble", "Amy Pond", "Clara Oswald"]
doctors = [9, 10, 10, 11, 11]

# Prints tuples
for example in zip(names, doctors):
    print(example)

print('-' * 10)

# Prints companion names
for companion in zip(names, doctors):
    print(companion[0])

print('-' * 10)

# Prints formatted output
for comp_doc in zip(names, doctors):
    print('{} \tis the companion of {}-th doctor'.format(comp_doc[0], comp_doc[1]))