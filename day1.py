with open('day1.txt', 'r') as f:
	inp = f.read()

print(inp.count('(') - inp.count(')'))

pos = 0
floor = 0

while floor > -1:
    pos += 1
    cur = inp[pos-1]
    if cur == '(':
        cur = 1
    else:
        cur = -1
    floor += cur
    print('Position:', pos, 'Floor:', floor)
