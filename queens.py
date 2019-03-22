import operator
from multiprocessing import Pool
import time

OPERATORS = {
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


def calculate(value, operator):
    if OPERATORS[operator]:
        value = OPERATORS[operator](value, 1)
    return value


def movementscounter(dst, length, queen, obstacles_positions):
    movements_counter = 0
    pointer = queen
    pointer = [calculate(pointer[0], MOVEMENTS[dst][0]), calculate(pointer[1], MOVEMENTS[dst][1])]
    while 0 < pointer[0] <= length and 0 < pointer[1] <= length:
        if pointer in obstacles_positions:
            break
        else:
            movements_counter += 1
            pointer = [calculate(pointer[0], MOVEMENTS[dst][0]), calculate(pointer[1], MOVEMENTS[dst][1])]
    return movements_counter


def queensattack():
    with open("game4.txt") as file:
        input_txt = [list(map(int, a.split(' '))) for a in file.read().split('\n')]
    length = input_txt[0][0]
    obstacles_quantity = input_txt[0][1]
    queen = input_txt[1]
    obstacles_positions = input_txt[2:]
    if len(obstacles_positions) != obstacles_quantity or 0 > length > 100000 and queen in obstacles_positions:
        print("Validation error!")
    else:
        counter = 0
        for movement in MOVEMENTS.keys():
            counter = counter + movementscounter(movement, length, queen, obstacles_positions)
        print(counter)
        # with Pool(processes=4) as pool:
        #     multiple_results = [pool.apply_async(movementscounter, (movement, length, queen, obstacles_positions)) for movement in MOVEMENTS.keys()]
        #     print(sum([res.get() for res in multiple_results]))


if __name__ == '__main__':
    tic = time.clock()
    queensattack()
    toc = time.clock()
    print(toc - tic)
