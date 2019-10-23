import gc

a = 5
b = [1, 2, 3, 4, 5]

gc.disable()
print(gc.isenabled())

gc.enable()
print(gc.isenabled())

a += 1
b.append(0)

print(gc.get_count())
print(gc.garbage)
