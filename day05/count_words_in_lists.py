celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

L = []
for x in celestial_objects:
    if x not in L:
        L.append(x)
for x in L:
    num = celestial_objects.count(x)
    print("{:<12}{}".format(x, num))
