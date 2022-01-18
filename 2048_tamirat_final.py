# sup man

import random
# the module to give random number
import numpy as np
# the package to import the numpy and in order to transpose the matrix and other staff
import copy
# the module to copy the matrix different element of the list
import os
# is the module to clear the matrix after one command
import sys
# is the module to exit whenever and wherever needed

# This is the program to add random numbers in the first matrix
new_grid = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
# what jdsg
i = random.randint(0, 3)
j = random.randint(0, 3)

for i in range(2):
    while (new_grid[i][j] != 0):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    new_grid[i][j] = 2

new_grid = np.array(new_grid)
new_grid = copy.deepcopy(new_grid)
for i in range(15):
    print('~', end=" ")
print()

for i in new_grid:

    for j in i:
        print("|", j, " ", "|", end="")
    print("")
for i in range(15):
    print('~', end=" ")
print()

# this is the function to tell weather you win or not. by checking weather consequative element are
# not the same both in row and column, there is no zero in the matrix

def winner_gameOver(new_grid):
    gameOver = False
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] >= 2048:
                print("congratulation you won !!")
                sys.exit()  #TO terminate the game after the game over
    for i in range(4):
        for j in range(3):
            if new_grid[i][j] == new_grid[i][j + 1] and 0 and np.array(new_grid).transpose()[i][j] == np.array(new_grid).transpose()[i][j + 1]  not in new_grid  not in new_grid and not gameOver:
                print("game over")
                gameOver = True
                sys.exit()  #TO terminate the game after the game over



    # this is the function to add random numbers after each update
def rand_setter(new_grid):
    i = random.randint(0, 3)
    j = random.randint(0, 3)
    while (new_grid[i][j] != 0):
        i = random.randint(0, 3)
        j = random.randint(0, 3)
    new_grid[i][j] = 2
    return new_grid

# this the function to intiate the game in the first step and display the
# options to play the game like 'w' for up, 'a' for left,'s' for down and 'd' for right

def caller(new_grid):


    command = {'a': 'left',
               'd': 'right',
               'w': 'up',
               's': 'down'}

    print(command)
    player = input("enter your choice:")
    choice = command.get(player, 'try again')
#  these functions like move_left, move_right, move_up and move_down
#  are for the game to move the numbers in different directions and the all return the updated matrix

    if choice == 'left':
        new_grid = move_left(new_grid)
        return new_grid
    elif choice == 'right':
        new_grid = move_right(new_grid)
        return new_grid
    elif choice == 'up':
        new_grid = move_up(new_grid)
        return new_grid
    elif choice == 'down':
        new_grid = move_down(new_grid)
        return new_grid


# this is the function to compress the matrix to right and merge it as
# there order.


def move_right(new_grid):
    global j, i
# the matrix to compress the main matrix using other matrix

    new_num = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

    for i in range(4):
        rank = 0
        for j in range(4):
            if new_grid[i][3-j] != 0:
                new_num[i][3-rank] = new_grid[i][3-j]
                rank += 1
# this the program to add the compressed matrix

    for i in range(4):
        if new_num[i][3] == new_num[i][2] and new_num[i][1] == new_num[i][0] and new_num[i][3] != 0 and new_num[i][1] != 0:
            new_num[i][3] = new_num[i][3] + new_num[i][2]
            new_num[i][2] = new_num[i][1] + new_num[i][0]
            new_num[i][1] = 0
            new_num[i][0] = 0
        if new_num[i][3] == new_num[i][2] and new_num[i][3] != 0:
            new_num[i][3] = new_num[i][3] + new_num[i][2]
            new_num[i][2] = new_num[i][1]
            new_num[i][1] = new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][2] == new_num[i][1] and new_num[i][2] != 0:
            new_num[i][2] = new_num[i][2] + new_num[i][1]
            new_num[i][1] = new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][1] == new_num[i][0] and new_num[i][1] != 0:
            new_num[i][1] = new_num[i][1] + new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][3] != new_num[i][2] and new_num[i][2] != new_num[i][1] and new_num[i][1] != new_num[i][0]:
            new_num[i][3] = new_num[i][3]
            new_num[i][2] = new_num[i][2]
            new_num[i][1] = new_num[i][1]
            new_num[i][0] = new_num[i][0]


    new_num = np.array(new_num)
    new_grid = copy.deepcopy(new_num)
# call the function to add random number to the updated one
    rand_setter(new_grid)
# it return the updated one to the caller function
    return new_grid


# move to left
# this is the function to compress the matrix to left and merge it as
# there order.
def move_left(new_grid):
    # the matrix to compress the main matrix using other matrix
    new_num = [[0 , 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
# this the program to add the compressed matrix
    for i in range(4):
        rank = 0
        for j in range(4):
            if new_grid[i][j] != 0:
                new_num[i][rank] = new_grid[i][j]
                rank += 1
    for i in range(4):

        if new_num[i][0] == new_num[i][1] and new_num[i][2] == new_num[i][3] and new_num[i][0] != 0 and new_num[i][3] != 0:
            new_num[i][0] = new_num[i][0] + new_num[i][1]
            new_num[i][1] = new_num[i][2] + new_num[i][3]
            new_num[i][2] = 0
            new_num[i][3] = 0
        if new_num[i][0] == new_num[i][1] and new_num[i][0] != 0:
            new_num[i][0] = new_num[i][1] + new_num[i][0]
            new_num[i][1] = new_num[i][2]
            new_num[i][2] = new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][1] == new_num[i][2] and new_num[i][1] != 0:
            new_num[i][1] = new_num[i][1] + new_num[i][2]
            new_num[i][2] = new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][2] == new_num[i][3] and new_num[i][2] != 0:
            new_num[i][2] = new_num[i][2] + new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][0] != new_num[i][1] and new_num[i][1] != new_num[i][2] and new_num[i][2] != new_num[i][3]:
            new_num[i][0] = new_num[i][0]
            new_num[i][1] = new_num[i][1]
            new_num[i][2] = new_num[i][2]
            new_num[i][3] = new_num[i][3]


    new_grid = np.array(new_num)
    new_grid = copy.deepcopy(new_grid)
# call the function to add random number to the updated one
    rand_setter(new_grid)
# it return the updated one to the caller function
    return new_grid


# this is the function called move_up to compress the matrix to  and merge it as
# there order.

def move_up(new_grid):
    # I used numpy package to transpose it easily and compress it to left and
    # merge the consquative member if the are equal and transpose it to the orginal matrix

    new_grid = np.array(new_grid).transpose()
    # the matrix to compress the main matrix using other matrix
    new_num = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

# to compress the non zero numbers in the matrix
    for i in range(4):
        rank = 0
        for j in range(4):
            if new_grid[i][j] != 0:
                new_num[i][rank] = new_grid[i][j]
                rank += 1
    new_num = np.array(new_num)
# merge the similar numbers
    for i in range(4):
        if new_num[i][0] == new_num[i][1] and new_num[i][2] == new_num[i][3] and new_num[i][0] != 0 and new_num[i][3] != 0:
            new_num[i][0] = new_num[i][0] + new_num[i][1]
            new_num[i][1] = new_num[i][2] + new_num[i][3]
            new_num[i][2] = 0
            new_num[i][3] = 0
        if new_num[i][0] == new_num[i][1] and new_num[i][0] != 0:
            new_num[i][0] = new_num[i][1] + new_num[i][0]
            new_num[i][1] = new_num[i][2]
            new_num[i][2] = new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][1] == new_num[i][2] and new_num[i][1] != 0:
            new_num[i][1] = new_num[i][1] + new_num[i][2]
            new_num[i][2] = new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][2] == new_num[i][3] and new_num[i][2] != 0:
            new_num[i][2] = new_num[i][2] + new_num[i][3]
            new_num[i][3] = 0
        if new_num[i][0] != new_num[i][1] and new_num[i][1] != new_num[i][2] and new_num[i][2] != new_num[i][3]:
            new_num[i][0] = new_num[i][0]
            new_num[i][1] = new_num[i][1]
            new_num[i][2] = new_num[i][2]
            new_num[i][3] = new_num[i][3]

# to transpose the matrix  to the original one
    new_grid = np.array(new_num).transpose()
    new_grid = copy.deepcopy(new_grid)
    rand_setter(new_grid)
    return new_grid

# this is the function called move_down to compress the matrix to  and merge it as
# there order.
def move_down(new_grid):
    # I used numpy package to transpose it easily and compress it to right and
    # merge the consequative member if the are equal and transpose it to the orginal matrix

    new_grid = np.array(new_grid).transpose()
    # the matrix to compress the main matrix using other matrix
    new_num = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    # to compress the non zero numbers in the matrix
    for i in range(4):
        rank = 0
        for j in range(4):
            if new_grid[i][3-j] != 0:
                new_num[i][3-rank] = new_grid[i][3-j]
                rank += 1
    new_num = np.array(new_num)

    # merge the similar numbers
    for i in range(4):
        if new_num[i][3] == new_num[i][2] and new_num[i][1] == new_num[i][0] and new_num[i][3] != 0 and new_num[i][1] != 0:
            new_num[i][3] = new_num[i][3] + new_num[i][2]
            new_num[i][2] = new_num[i][1] + new_num[i][0]
            new_num[i][1] = 0
            new_num[i][0] = 0
        if new_num[i][3] == new_num[i][2] and new_num[i][3] != 0:
            new_num[i][3] = new_num[i][3] + new_num[i][2]
            new_num[i][2] = new_num[i][1]
            new_num[i][1] = new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][2] == new_num[i][1] and new_num[i][2] != 0:
            new_num[i][2] = new_num[i][2] + new_num[i][1]
            new_num[i][1] = new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][1] == new_num[i][0] and new_num[i][1] != 0:
            new_num[i][1] = new_num[i][1] + new_num[i][0]
            new_num[i][0] = 0
        if new_num[i][3] != new_num[i][2] and new_num[i][2] != new_num[i][1] and new_num[i][1] != new_num[i][0]:
            new_num[i][3] = new_num[i][3]
            new_num[i][2] = new_num[i][2]
            new_num[i][1] = new_num[i][1]
            new_num[i][0] = new_num[i][0]
    # to transpose the matrix  to the original one
    new_grid = np.array(new_num).transpose()
    new_grid = copy.deepcopy(new_grid)
    rand_setter(new_grid)
    return new_grid

while True:
   
    new_grid = (caller(new_grid))
    _ = os.system('cls')

    for i in range(15):
        print('_', end=" ")
    print()

    for i in new_grid:

        for j in i:

            print("|", j, " ", "|", end=" ")
        print("")
    for i in range(15):
        print('~', end=" ")
    print()
    winner_gameOver(new_grid)

