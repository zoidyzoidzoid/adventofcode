with open('day2.txt', 'r') as f:
    dimensionss = f.read()

dimensionss = dimensionss.split('\n')
dimensionss = [d for d in dimensionss if d]

print('Calculating total wrapping paper needed')

tot = 0

for dimensions in dimensionss:
    l, w, h = dimensions.split('x')
    l, w, h = int(l), int(w), int(h)
    areas = [l * w, l * h, w * h]
    tot += sum(map(lambda x: 2 * x, areas), min(areas))

print(tot)


print('Calculating total ribbon needed')

tot = 0

for dimensions in dimensionss:
    print('Processing:', dimensions)
    l, w, h = dimensions.split('x')
    l, w, h = int(l), int(w), int(h)
    permiters = map(lambda x: 2 * x, [l + w, l + h, w + h])
    tot += (min(permiters) + (l * w * h))

print(tot)
