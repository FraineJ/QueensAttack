import operator

OPERATORS = {
    "+": operator.gt,
    "-": operator.lt,
    "0": operator.eq
}

OPERATORS_FOR_CALCULATE = {
    "+": operator.add,
    "-": operator.sub,
    "0": None
}

MOVEMENTS = {
    "UP": ("0", "+"),
    "UP-RIGHT": ("+", "+"),
    "RIGHT": ("+", "0"),
    "DOWN-RIGHT": ("+", "-"),
    "DOWN": ("0", "-"),
    "DOWN-LEFT": ("-", "-"),
    "LEFT": ("-", "0"),
    "LEFT-UP": ("-", "+"),
}


def take_second(elem):
    return elem[1]


def take_first(elem):
    return elem[0]


def filterobstaclesbydirection(dir, queen, obstacle):
    return OPERATORS[MOVEMENTS[dir][0]](obstacle[0], queen[0]) and OPERATORS[MOVEMENTS[dir][1]](obstacle[1], queen[1])


def calculate(value, operator):
    if OPERATORS_FOR_CALCULATE[operator]:
        value = OPERATORS_FOR_CALCULATE[operator](value, 1)
    return value


def movementscounter(dst, length, queen, obstacles_positions):
    movements_counter = 0
    pointer = queen
    pointer = [calculate(pointer[0], MOVEMENTS[dst][0]), calculate(pointer[1], MOVEMENTS[dst][1])]
    while 0 < pointer[0] <= length and 0 < pointer[1] <= length:
        try:
            obstacles_positions.index(pointer)
            break
        except ValueError:
            movements_counter += 1
            pointer = [calculate(pointer[0], MOVEMENTS[dst][0]), calculate(pointer[1], MOVEMENTS[dst][1])]
    return movements_counter


def queensattack():
    with open("game.txt") as file:
        input_txt = [tuple(map(int, a.split(' '))) for a in file.read().split('\n')]
    length = input_txt[0][0]
    obstacles_quantity = input_txt[0][1]
    queen = input_txt[1]
    obstacles_positions = tuple(input_txt[2:])
    if len(obstacles_positions) != obstacles_quantity or 0 > length > 100000 and queen in obstacles_positions:
        print("Validation error!")
    else:
        counter = 0
        for movement in MOVEMENTS.keys():
            if movement in ("UP", "RIGHT", "DOWN", "LEFT"):
                obstacles = list(filter(lambda x: filterobstaclesbydirection(movement, queen, x), obstacles_positions))
                if len(obstacles) == 0:
                    if movement == "UP":
                        counter = counter + (length - queen[1])
                    elif movement == "RIGHT":
                        counter = counter + (length - queen[0])
                    elif movement == "DOWN":
                        counter = counter + (queen[1] - 1)
                    elif movement == "LEFT":
                        counter = counter + (queen[0] - 1)
                else:
                    if movement == "UP":
                        obstacles.sort(key=take_second)
                        counter = counter + (obstacles[0][1] - queen[1])
                    elif movement == "RIGHT":
                        obstacles.sort(key=take_first)
                        counter = counter + (length - queen[0])
                    elif movement == "DOWN":
                        obstacles.sort(key=take_second, reverse=True)
                        counter = counter + (queen[1] - obstacles[0][1])
                    elif movement == "LEFT":
                        obstacles.sort(key=take_first, reverse=True)
                        counter = counter + (queen[0] - obstacles[0][0])
                    counter -= 1
            else:
                counter = counter + movementscounter(movement, length, queen, obstacles_positions)
        print(counter)


if __name__ == '__main__':
    queensattack()
