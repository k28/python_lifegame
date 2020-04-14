# coding: utf-8

import random
import sys, time
import copy
import os

LIVE = '*'
DEAD = ' '

MAX_WIDTH  = 40
MAX_HEIGHT = 20

# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

def count_live_neighbours(checkList, index, width):
    count = 0
    if checkList[index - width - 1] == LIVE:
        count += 1
    if checkList[index - width] == LIVE:
        count += 1
    if checkList[index - width + 1] == LIVE:
        count += 1
    if checkList[index - 1] == LIVE:
        count += 1
    if checkList[index + 1] == LIVE:
        count += 1
    if checkList[index + width - 1] == LIVE:
        count += 1
    if checkList[index + width] == LIVE:
        count += 1
    if checkList[index + width + 1] == LIVE:
        count += 1
    return count

def check_life(oldList, newList, index, width):
    life_cell_count = count_live_neighbours(oldList, index, width)
    if oldList[index] == LIVE:
        if life_cell_count <= 1:
            newList[index] = DEAD
        elif life_cell_count == 2 or life_cell_count == 3:
            newList[index] = LIVE
        else:
            newList[index] = DEAD
    elif oldList[index] == DEAD:
        if life_cell_count == 3:
            newList[index] = LIVE

def print_life(life_list, width, height):

    os.system('clear')

    for index in range(width * height):
        if index < width:
            pass
        elif index % width == 0:
            pass
        elif index % width == width - 1:
            pass
        elif index >= width * (height - 1):
            pass
        else:
            sys.stdout.write(str(life_list[index]))
            if index % width == width - 2:
                print("")

width = MAX_WIDTH + 2
height = MAX_HEIGHT + 2

first_list = [DEAD] * (width * height)

for index in range(width * height):
    # 枠はDEADで固定, 枠内部はランダムに設定しておく
    if index < width:
        first_list[index] = DEAD
    elif index % width == 0:
        first_list[index] = DEAD
    elif index % width == width - 1:
        first_list[index] = DEAD
    elif index >= width * (height - 1):
        first_list[index] = DEAD
    else:
        first_list[index] = random.choice([LIVE, DEAD])

print_life(first_list, width, height)

old_list = first_list
while True:
    time.sleep(0.5)
    new_list = copy.deepcopy(old_list)

    for index in range(width * height):
        # 枠は何もしない
        if index < width:
            pass
        elif index % width == 0:
            pass
        elif index % width == width - 1:
            pass
        elif index >= width * (height - 1):
            pass
        # 枠の内部は世代を進める
        else:
            check_life(old_list, new_list, index, width)
            
    print_life(new_list, width, height)
    old_list = new_list


