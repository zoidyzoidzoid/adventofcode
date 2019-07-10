with open('day3.txt', 'r') as f:
    instructions = f.read()


def calc_gifted_houses(commands):
    santa_x, santa_y = 0, 0

    gifted_houses = {(santa_x, santa_y)}

    print('Counting houses delivered to:')
    print(len(commands), 'instructions')

    for command in commands:
        if command == '>':
            santa_x += 1
        elif command == '^':
            santa_y += 1
        elif command == '<':
            santa_x -= 1
        elif command == 'v':
            santa_y -= 1
        gifted_houses.add((santa_x, santa_y),)

    print(len(gifted_houses))

calc_gifted_houses('>')
calc_gifted_houses('^>v<')
calc_gifted_houses('^v^v^v^v^v')

calc_gifted_houses(instructions)


def calc_gifted_houses_with_robo(commands):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    santas_turn = True

    gifted_houses = {(santa_x, santa_y)}

    print('Counting houses delivered to:')
    print(len(commands), 'instructions')

    for command in commands:
        if santas_turn:
            santas_turn = False
            if command == '>':
                santa_x += 1
            elif command == '^':
                santa_y += 1
            elif command == '<':
                santa_x -= 1
            elif command == 'v':
                santa_y -= 1
            gifted_houses.add((santa_x, santa_y),)
        else:
            santas_turn = True
            if command == '>':
                robo_x += 1
            elif command == '^':
                robo_y += 1
            elif command == '<':
                robo_x -= 1
            elif command == 'v':
                robo_y -= 1
            gifted_houses.add((robo_x, robo_y),)

    print(len(gifted_houses))

calc_gifted_houses_with_robo('^v')
calc_gifted_houses_with_robo('^>v<')
calc_gifted_houses_with_robo('^v^v^v^v^v')

calc_gifted_houses_with_robo(instructions)
