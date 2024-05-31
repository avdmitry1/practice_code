employees = [
    'Pankratiy', 'Innokentiy', 'Anfisa', 'Yaroslava', 'Veniamin',
    'Leonti', 'Daniil', 'Mishka', 'Lidochka',
    'Terenti', 'Vladik', 'Svetka', 'Maks', 'Yura', 'Sergei'
]

identifiers = [77, 48, 88, 85, 76, 81, 62, 43, 5, 56, 17, 20, 37, 32, 96]
a = sorted(employees)
b = sorted(identifiers)
res = dict(zip(a, b))
print(res)