# By submitting this assignment, all team members agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Hayden Holmquist
# Richard Teran
# Orlando Bracamontes
# Jude Rangel
# Section: 560
# Assignment: End of Semester Project
# Date: Start: 20 11 2023  End: 12/4/23
"""I really hope this is the last time we'll have to use this dumb header lol
-_-  -Hayden"""
# from math import *
"""currently, math isn't called so im keeping it unimported for efficiency"""
from random import randint
from time import sleep
from pynput import keyboard

"""/// Hayden's Global Variables ///"""
ph = "Placeholder, yeah!"  # used generally for unfinished results in functions
winner = []  # used in tiebreaker
###
""""keyboard input related global variables"""
key_pressed = set()  # the current key being pressed down, globally as a truly blank variable
current_key = ""  # stores the current key as a str for key released (idk why)
###


"""/// Richard's Global Variables///"""

############################################
############################################
############################################
biglist = []
############################################
############################################
############################################
# ITS
# ALL
# BIG
# LIST.
# Empty for now! Will be referenced in a series of functions, which each do their part to it.
current_turn = 0  # Keep this at zero. (but why? -Hayden)
next_turn = 0

"""/// Orlando's Global Variables///"""
cpu_scores = []
score = set()  # I cleaned this up to have continuity with the other function orlando made

"""/// Jude's Global Variables///"""
game = 0
check = 0
pos1 = 1
pos = 1
arrow = ''
menu = False
looping = True
new_game = False
settings = 0
start = 0
first_run = True
gameing = False
gameing_setup = False
waiting = True
rolls = 1

'''### NO MORE THAN 10-LINE FUNCTIONS! ###  (not a hard rule, 
but an important guideline for leaves. -Hayden)'''

"""Richard's leaf functions"""

'''##########NEW#########'''


def make_big_list():  # This makes the big list we will use and keep using throughout the while script!
    enter_names = str(input('Enter player names (each followed by a space):\n'))
    cpu_list = enter_names.split()
    for i in range(len(cpu_list)):
        biglist.append([cpu_list[i]])

    return biglist


print(make_big_list())


def enter_chips(chips_value):  # Run this after we ENTER the game. Uses set chips value to append.
    for i in range(len(biglist)):  # AND NOW, we begin using biglist for our indexing! yay!
        biglist[i].append(chips_value)

    return biglist  # Every time. It's the same list we're working with after establishing names for the start of each!


print(enter_chips(24))

# function here maxrolls += 1
maxrolls = 3


# all_data = [["hayden", 20, 135]]
# function thing
# newlist = [data1, data2, data3]
# all_data.append(newlist)


def change_turn():
    """
    "Player turn tracking," or an increasing-number loop dictating the index for which each player goes.
    This could be done by just numbers. When run, cannot run again for the same player until looping-through.
    """
    global current_turn
    global next_turn
    current_turn = current_turn + 1 if current_turn <= len(biglist) - 1 else 1
    next_turn = current_turn + 1 if current_turn <= len(biglist) - 1 else 1
    print(f'/// [[ TURN CHANGE ]] ///\nP{current_turn} plays.\nP{next_turn} goes next turn.')


change_turn()


def game_over():
    """
    "Winner order," or...yeah.
    Sum-up point totals and order them in a list. Then we print the announcements in output. That's...literally it.
    Very compact!! No loop!! Sorts players and their values in pairs of tuples within a list. I am so freaking proud.
    TODO: Remember to include marker to end all other function loops.
    # what does that mean -Hayden
    """
    pscores = sorted(biglist, key=lambda x: x[1], reverse=True)  # Sick!
    announcement = '##### {{{ GAME OVER }}} #####\n'
    for i in range(len(biglist)):
        announcement += f'{pscores[0][0]} came 1st with {pscores[0][1]} points!\n' if i == 0 else ''
        announcement += f'{pscores[1][0]} came in 2nd with {pscores[i][1]}.\n' if i == 1 else ''
        announcement += f'{pscores[2][0]} came in 3rd with {pscores[i][1]}.\n' if i == 2 else ''
        announcement += f'{pscores[i][0]} came in {i + 1}th with {pscores[i][1]}.\n' if i > 2 else ''
    print(announcement)  # pscores is a list of tuple pairs. Fitting for read-only!


#game_over()

"""Orlando's leaf-oriented functions"""


def dice_to_points(x):
    """orlando didn't write a doc string, nor did he even make it a funciton
    but im going to assume this is how he intended it to be executed. im not
    hatin on you, it was just kinda weird to implement this into the game lol
    Use: dice_to_points(x): where x is the current set of dice roll (list of
    3)."""
    point_values = {'1': 100, '2': 2, '3': 3, '4': 4, '5': 5, '6': 60}
    comb_values = {'123': 301, '666': 302, '555': 303, '444': 304, '333': 305, '222': 306, '111': 307, '456': 310}
    # making sure the comb_values are higher than the point_values
    rand_values = x  # no clue why orlando named it rand_values, but i just slapped a function input on it and it
    # works kinda -hayden
    # rand_values = sorted(input("Random set of numbers:"))  ## for testing
    dice_numbers = ''.join(rand_values)  # set of numbers as one string
    """idk why you had to make the dice rolls strings, not integers, but it works
    so im not gonna complain!"""
    list_of_values = []
    global cpu_scores, score

    if dice_numbers in comb_values:
        score = comb_values.get(dice_numbers)
    else:
        for i in rand_values:
            list_of_values.append(point_values[i])
            score = int(sum(list_of_values))
    print(score)  ## to check if score is right
    return score


dice_to_points(["1", "1", "1"])
# i'd assume that we're going to make score append/set a dictionary to keep track of
# each player/cpu's scores - hayden

from matplotlib import pyplot as mlt  # idk what orlando did here but im not touching

#  it incase something breaks -hayden

# enter_names = input('Enter player names (each followed by a space):')
cpu_list = make_big_list()  # Richard: Since names were entered before, this should work.


def chip_tally():
    if len(cpu_list) < 2:
        print("No friends")
    else:
        print(f'There are {len(cpu_list)} players\n{enter_names}')

    # assuming the scores for everyone from the round are
    # in a list 'cpu_scores' and is respected with stone_count
    # references values in dictionary from other file 'point_values'
    # and 'comb_values'
    stone_count = [20] * len(cpu_list)
    cpu_scores = [250, 303, 200]  ##### hypothetical

    if 1 < max(cpu_scores) <= 260:
        stone_count[cpu_scores.index(min(cpu_scores))] = stone_count[cpu_scores.index(min(cpu_scores))] + (
                1 * (len(cpu_list) - 1)) + 1
        stone_count = [x - 1 for x in stone_count]

    elif max(cpu_scores) == 301:
        stone_count[cpu_scores.index(min(cpu_scores))] = stone_count[cpu_scores.index(min(cpu_scores))] + (
                2 * (len(cpu_list) - 1)) + 2
        stone_count = [x - 2 for x in stone_count]

    elif 302 <= max(cpu_scores) <= 307:
        stone_count[cpu_scores.index(min(cpu_scores))] = stone_count[cpu_scores.index(min(cpu_scores))] + (
                3 * (len(cpu_list) - 1)) + 3
        stone_count = [x - 3 for x in stone_count]
    else:
        stone_count[cpu_scores.index(min(cpu_scores))] = stone_count[cpu_scores.index(min(cpu_scores))] + (
                4 * (len(cpu_list) - 1)) + 4
        stone_count = [x - 4 for x in stone_count]
    print(stone_count)
    return stone_count


"""Hayden's leaf-oriented functions"""


def tiebreaker(x, y):
    """This function breaks any ties between players. supports two inputs
       but this can be changed if needed. 1st Player is the leftmost input"""
    global winner
    rng = randint(0, 1)
    if rng == 0:
        winner = ["{}st Player".format(x), x]

    elif rng == 1:
        winner = ["{}nd Player".format(y), y]
    return winner


help(tiebreaker)
print(tiebreaker(1, 2))  # you can just return rng instead for coin flips -Hayden

# required global variables for dicerolls()
roll = []


def dicerolls(x, y=0):
    """prints a list of dice rolls between one and six as many times as
       requested by x. (x = number of dice rolls, y = 0 (default) reset roll
       before adding new rolls). roll (the output list) gets reset with EACH
       function call, unless you put 1 as the second parameter, eg (3, 4)."""
    global roll
    if y != 1:
        roll = []
    counter = 0
    while counter < x:
        die_roll = str(randint(1, 6))
        roll.append(die_roll)
        counter += 1
    roll.sort()
    return roll


help(dicerolls)
print(dicerolls(3))


def scorecheck(x):
    """function that checks the person's dice roll(s) to the scoring index
    and returns either a win condition or the point value of their roll.
    (x = the list of rolls (eg [4, 5, 6])"""
    if x == [4, 5, 6]:
        # implement point values/win conditions for further code
        print(ph)
    elif x[0] == x[1] and x[0] == x[2]:  # way of comparing all three values to be equal
        # implement point values/win conditions for further code
        print(ph)
    elif x == [1, 2, 3]:
        # implement point values/win conditions for further code
        print(ph)
    else:
        print(ph)  # should be the sum values (which should be a function?)


help(scorecheck)
print(dicerolls(3))
scorecheck(dicerolls(3))

"""jude fucntion"""


def start_window():
    """function that draws the main menu for zanzibar."""
    win = t.Screen()
    t.ht()
    global game, check, pos1, pos, arrow, menu
    game = 0
    menu = True
    check = 0
    pos1 = 1
    pos = 1
    arrow = ''
    win.bgcolor('light goldenrod yellow')
    t.speed(10)
    t.color('black')
    t.begin_fill()
    t.penup()
    t.setpos(-225, -225)
    t.pendown()
    t.setpos(225, -225)
    t.setpos(225, 0)
    t.setpos(-225, 0)
    t.setpos(-225, -225)
    t.end_fill()
    t.penup()
    t.color('white')
    t.begin_fill()
    t.penup()
    t.setpos(-220, -220)
    t.pendown()
    t.setpos(220, -220)
    t.setpos(220, -5)
    t.setpos(-220, -5)
    t.setpos(-220, -220)
    t.end_fill()
    t.penup()
    t.setpos(0, -75)
    t.color('black')
    t.write('NEW GAME', align='center', font=('arial', 20, 'normal'))
    t.setpos(0, -170)
    t.write('QUIT', align='center', font=('arial', 20, 'normal'))
    t.setpos(0, -210)
    # You can change the button by adding an elif before line 89
    t.write('Input the enter key to select an option', align='center', font=('arial', 12, 'normal'))
    t.setpos(0, 170)
    t.write('Zanzibar', align='center', font=('comic sans ms', 47, 'normal'))
    # Above is the code for the start menu
    global a
    global looping
    looping = False
    a = t.Turtle()
    a.penup()
    a.ht()
    a.speed(10)
    a.setpos(-87, -58)


def mouse(x, y):
    if check == 0:
        a.speed(0)
        a.clear()
        a.setpos(x, y)
        a.begin_fill()
        a.pendown()
        a.setheading(150)
        a.fd(25)
        a.lt(120)
        a.fd(25)
        a.lt(120)
        a.fd(25)
        a.end_fill()
        a.penup()
    elif check == 1:
        a.pendown()
        a.clear()


def players():
    c.clear()
    c.setpos(113, 40)
    c.write(numplayers, align='center', font=('arial', 17, 'normal'))


def startchips():
    d.clear()
    d.setpos(80, -60)
    d.write(chips, align='center', font=('arial', 17, 'normal'))


# Above is the code for start game mouse and below is quit mouse. use a or b.clear() to remove just one.


def rules():  # here is the function to pull up rules, to look at it type r
    e.penup()
    e.begin_fill()
    e.speed(10)
    e.setpos(-225, -225)
    e.pendown()
    e.setpos(225, -225)
    e.setpos(225, 200)
    e.setpos(-225, 200)
    e.setpos(-225, -225)
    e.end_fill()
    e.penup()
    e.color('white')
    e.begin_fill()
    e.penup()
    e.setpos(-220, -220)
    e.pendown()
    e.setpos(220, -220)
    e.setpos(220, 195)
    e.setpos(-220, 195)
    e.setpos(-220, -220)
    e.end_fill()
    e.penup()
    e.setpos(0, -75)
    e.color('black')
    e.setpos(174, -30)
    e.write('Combos ranked from \n    highest to lowest', align='right', font=('arial', 12, 'normal'))
    e.setpos(95, -150)
    e.write('456\n111\n222\n333\n444\n555\n666\n123', align='center', font=('arial', 8, 'normal'))
    e.setpos(-123, -138)
    e.write(
        'In Zanzibar the starting\nplayer will roll 3 dice up\nto 3 times and players\nafter must roll the dice\nto '
        'get a better combo in\nthe same or fewer rolls.\nPlayers will compare\ntheir scores based on\nwhat they '
        'rolled. Specific\ncombos are worth more,\nand other combos are a\nsum ofthe scores for each\ndice. At the '
        'end of a round\nall players give the player\nwith the lowest score chips\nbased on the type of combo\nof the '
        'highest score',
        align='center', font=('arial', 9, 'normal'))
    e.setpos(175, 100)
    e.write('Dice Scores', align='center', font=('arial', 12, 'normal'))
    e.setpos(180, 15)
    e.write('1 = 100 points\n6 = 60 points\n2 = 2 points\n3 = 3 points\n4 = points\n5 = 5 points', align='center',
            font=('arial', 8, 'normal'))
    e.setpos(25, 100)
    e.write('Chip Rules', align='center', font=('arial', 12, 'normal'))
    e.setpos(25, 85)
    e.write('If highest score is', align='center', font=('arial', 9, 'normal'))
    e.setpos(38, 23)
    e.write(
        '-Points total give one chip\n-1, 2, 3 give two chips\n-Three of a kind give 3 chips\n-4, 5, 6 (Zanzibar) '
        'give four chips',
        align='center', font=('arial', 8, 'normal'))
    e.setpos(0, 130)
    e.write('Rules', align='center', font=('arial', 30, 'normal'))
    keye = ''
    while keye != 'r':
        keye = input('?')
    e.clear()


def one():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    # Above is the code for the blank dice face
    f.lt(180)
    f.fd(40)
    f.rt(90)
    f.penup()
    f.fd(50)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()


def two():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.rt(90)


def three():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(180)
    f.fd(20)
    f.rt(90)
    f.fd(40)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.rt(180)


def four():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(90)
    f.fd(90)
    f.rt(90)
    f.fd(20)
    f.lt(270)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()


def five():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(180)
    f.fd(20)
    f.rt(90)
    f.fd(40)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(90)
    f.fd(50)
    f.lt(90)
    f.fd(30)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(180)
    f.fd(50)
    f.rt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.rt(90)


def six():
    f.speed(10)
    # f.ht()
    f.color('white')
    f.begin_fill()
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.end_fill()
    f.pendown()
    f.color('black')
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(90)
    f.fd(100)
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(90)
    f.fd(90)
    f.rt(90)
    f.fd(20)
    f.lt(270)
    f.fd(10)
    f.rt(90)
    f.penup()
    f.fd(20)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.fd(70)
    f.lt(90)
    f.fd(70)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(180)
    f.fd(10)
    f.rt(90)
    f.fd(40)
    f.rt(180)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.lt(270)
    f.fd(40)
    f.rt(90)
    f.pendown()
    f.begin_fill()
    f.circle(10)
    f.end_fill()
    f.penup()
    f.rt(90)


chipmenu = []


def dice():  # You may want to build the game into this
    # function and just call the function
    # as soon as player starts the game
    player = 0  # This is just a placeholder for the real player counter
    name = 'Player '
    name += str(player)
    f.setpos(0, 225)
    f.write(name, align='center', font=('arial', 30, 'normal'))
    g.setpos(0, -225)
    g.write('Input "r" for rules or "f" to roll', align='center', font=('arial', 12, 'normal'))
    keyf = current_key
    while keyf != 'f':
        keyf = input('enter r or f')
        if keyf == 'r':
            rules()
    g.clear()
    while keyf != 'x':  # Use x to break of the loop
        # you can change keyf != 'x' to something checking that no score == 0
        # keyf is just a placeholder for the real dice system but whatever value is rolled,
        # call the function to draw the corresponding dice and after 3 are drawn press a button
        # to clear and restart
        for i in range(numplayers):
            chipmenu.append(str(chips))
        cmenutext = '   '.join(chipmenu)

        f.setpos((-32 * numplayers) + 10, -110)
        f.color('white')
        f.pendown()
        f.begin_fill()
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(35)
        f.rt(90)
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(70)
        f.rt(90)
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(35)
        f.lt(90)
        f.end_fill()
        f.penup()
        f.setpos((-32 * numplayers) + 10, -110)
        f.color('black')
        f.pendown()
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(35)
        f.rt(90)
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(70)
        f.rt(90)
        f.fd((50 * numplayers) + 25)
        f.rt(90)
        f.fd(35)
        f.lt(90)
        f.penup()
        f.setpos(0, -10)
        f.write('Chips', align='center', font=('arial', 30, 'normal'))
        f.setpos((-25 * numplayers), -150)
        f.color('black')
        for i in range(len(chipmenu)):  # I would recommend to use a list with the chip values
            # to show the scores in game, as you could just edit chips below
            # to be chips[i]
            f.write(chips, align='left', font=('arial', 30, 'normal'))
            f.fd(50)
        f.setpos((-25 * numplayers), -115)
        num = 1
        for i in range(len(chipmenu)):  # I would recommend to use a list with the chip values
            # to show the scores in game, as you could just edit chips below
            # to be chips[i]
            f.write(num, align='left', font=('arial', 30, 'normal'))
            f.fd(50)
            num += 1
        while keyf != 'd':  # This while loop is to break whenever all players turns have passed
            keyf = str(input('type a number 1-6 for a dice or x to exit'))
            f.setpos(-225, 100)
            if keyf == '1':
                one()
            elif keyf == '2':
                two()
            elif keyf == '3':
                three()
            elif keyf == '4':
                four()
            elif keyf == '5':
                five()
            elif keyf == '6':
                six()
            keyf = str(input('type a number 1-6 for a dice or x to exit'))
            f.setpos(-50, 100)
            if keyf == '1':
                one()
            elif keyf == '2':
                two()
            elif keyf == '3':
                three()
            elif keyf == '4':
                four()
            elif keyf == '5':
                five()
            elif keyf == '6':
                six()
            keyf = str(input('type a number 1-6 for a dice or x to exit'))
            f.setpos(125, 100)
            if keyf == '1':
                one()
            elif keyf == '2':
                two()
            elif keyf == '3':
                three()
            elif keyf == '4':
                four()
            elif keyf == '5':
                five()
            elif keyf == '6':
                six()
            player += 1  # This is a makeshift turn system, please remove it when making final code
            f.setpos(0, 55)
            f.write('press r to reroll or n to move on', align='center', font=('arial', 12, 'normal'))
            # ^^^ replace this with whichever keyboard input will be used to continue
            keyf = current_key
            if keyf == 'n':
                # f.shape('dice1')
                f.clear()  # This clears the dice layer


"""The Keyboard input parsing functions!"""


def on_press(key):
    """Function(?) that checks what key is pressed and stores it if it's one
        of the whitelisted keys (see the function for more)"""
    if key == keyboard.Key.esc:
        return False
    try:
        k = key.char  # if its just one letter
    except:
        k = key.name  # if its something like up or down
    if k in ["enter", "left", "right", "up", "down", "r", "f", "c", "n"]:  # what keys you want
        global key_pressed
        global current_key
        if key not in key_pressed:
            # here i would do the thing depending on the key lol
            current_key = k
            key_pressed.add(key)
            print(current_key)
            # print("pressed {}".format(key))
        else:
            pass
    return


# I'll be honest, I'm kinda lost how these two even work. I wrote them myself,
# which is something I shouldn't need to clarify, but it's still really jank and confusing
def on_release(key):
    """Function(?) that is tangential to on_press that clears the "key_pressed"
     buffer and allows more inputs to be recorded/stored. (see the function
     for more.)"""
    if key == keyboard.Key.esc:
        return False
    try:
        k = key.char  # if its just one letter
    except:
        k = key.name  # if its something like up or down
    if k in ["enter", "left", "right", "up", "down", "r", "f", "c", "n"]:  # what keys you want
        # here i would do the thing depending on the key lol
        global key_pressed
        if key in key_pressed:  # cool limiter i made to try and make pyinput not blow up my pc
            key_pressed.remove(key)
            # print("released {}".format(key))
        else:
            pass  # how would this even happen
    return


"""Main loop for running the game. Must be run under this in order for
keyboard input to actually run for some reason"""
while True:  # literally just makes it an infinite loop
    listen = keyboard.Listener(on_press=on_press,
                               on_release=on_release)  # pycharm thinks something is wrong here, but it isnt (probably)  -hayden
    listen.start()
    sleep(0.3)  # Increasing or decreasing this exponentially and inversely effects
    # performance due to how listen works.
    if current_key == "up":
        print("updog")  # silly debug to check if my code even works
        current_key = ""
    import turtle as t

    if looping:
        start_window()
        mouse(-87, -58)
    if menu:
        while game == 0:
            arrow = current_key
            if arrow == 'down' and pos1 == 1:
                a.clear()
                mouse(-43, -153)
                pos1 = 2
                current_key = ""
            elif arrow == 'down':
                a.clear()
                mouse(-87, -58)
                pos1 = 1
                current_key = ""
            elif arrow == 'up' and pos1 == 1:
                a.clear()
                mouse(-43, -153)
                pos1 = 2
                current_key = ""
            elif arrow == 'up':
                a.clear()
                mouse(-87, -58)
                pos1 = 1
                current_key = ""
            elif pos1 == 1 and arrow == "enter":
                game = 1
                current_key = ""
            else:

                pass
        a.clear()
        if game != 0:
            t.clear()
            menu = False
            new_game = True

    if new_game:
        while settings == 0:
            win = t.Screen()
            win.bgcolor('light goldenrod yellow')
            t.speed(10)
            t.ht()
            t.penup()
            numplayers = 2
            chips = 20
            start = 0
            x = ''
            pos = 1
            a = t.Turtle()
            a.ht()
            a.penup()
            t.setpos(-300, -200)
            t.color('black')
            t.begin_fill()
            t.setpos(300, -200)
            t.setpos(300, 200)
            t.setpos(-300, 200)
            t.setpos(-300, -200)
            t.end_fill()
            t.penup()
            t.setpos(-295, -195)
            t.color('white')
            t.begin_fill()
            t.pendown()
            t.setpos(295, -195)
            t.setpos(295, 195)
            t.setpos(-295, 195)
            t.setpos(-295, -195)
            t.penup()
            t.end_fill()
            t.color('black')
            t.setpos(0, 140)
            t.write('Game Configuration', align='center', font=('arial', 30, 'normal'))
            t.setpos(0, 40)
            t.write('Number of Players: ', align='center', font=('arial', 17, 'normal'))
            t.setpos(0, -60)
            t.write('Starting Chips: ', align='center', font=('arial', 17, 'normal'))
            t.setpos(0, -160)
            t.write('Start Game', align='center', font=('arial', 30, 'normal'))
            c = t.Turtle()
            c.ht()
            c.penup()

            d = t.Turtle()
            d.ht()
            d.penup()
            settings = 1
            players()
            startchips()
    while start == 0:
        arrow = current_key
        if arrow == 'down' and pos <= 2:
            pos += 1
        elif arrow == 'down' and pos == 3:
            pos = 1
        elif arrow == 'up' and pos > 1:
            pos -= 1
        elif arrow == 'up' and pos == 1:
            pos = 3
        elif arrow == 'left' and pos == 1 and numplayers > 2:
            numplayers -= 1
            players()
        elif arrow == 'right' and pos == 1 and numplayers < 11:
            numplayers += 1
            players()
        elif arrow == 'left' and pos == 2 and chips > 4:
            chips -= 5
            startchips()
        elif arrow == 'right' and pos == 2 and chips < 50:
            chips += 5
            startchips()
        elif current_key == "enter" and pos == 3:  # moves on to the game window
            enter_chips(chips)  # Richard: PLEASE PLEASE PLEASE WORK!
            a.clear()
            c.clear()
            d.clear()
            t.clear()
            t.penup()
            e = t.Turtle()
            f = t.Turtle()
            f.speed(0)
            f.penup()
            e.ht()
            f.ht()
            g = t.Turtle()
            g.speed(0)
            g.ht()
            g.penup()
            key = ''
            keyf = ''
            start = 1
            new_game = False
            gameing = True
            gameing_setup = True
            check += 1
            mouse(0, 0)
        elif arrow == 'f' and pos == 3:
            a.clear()
            start += 1
        if pos == 1 and current_key != "":
            mouse(-105, 55)
            current_key = ""
        elif pos == 2 and current_key != "":
            mouse(-85, -47)
            current_key = ""
        elif pos == 3 and current_key != "":
            mouse(-113, -137)
            current_key = ""
        elif first_run:
            mouse(-105, 55)
            first_run = False
            current_key = ""
        else:
            pass
    if gameing:
        while gameing_setup:
            # dice()  yeah this aint gonna happen in epic style just leaver it alone! :(((
            # function and just call the function
            # as soon as player starts the game
            player = 0  # This is just a placeholder for the real player counter
            name = 'Player '
            name += str(player)
            f.setpos(0, 225)
            f.write(name, align='center', font=('arial', 30, 'normal'))
            g.setpos(0, -225)
            g.write('Input "r" for rules or "f" to roll', align='center', font=('arial', 12, 'normal'))
            keyf = current_key
            while keyf != 'x':  # Use x to break of the loop
                # you can change keyf != 'x' to something checking that no score == 0
                # keyf is just a placeholder for the real dice system but whatever value is rolled,
                # call the function to draw the corresponding dice and after 3 are drawn press a button
                # to clear and restart
                for i in range(numplayers):
                    chipmenu.append(str(chips))
                cmenutext = '   '.join(chipmenu)
                if keyf == 'r':
                    rules()
                f.setpos((-32 * numplayers) + 10, -110)
                f.color('white')
                f.pendown()
                f.begin_fill()
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(35)
                f.rt(90)
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(70)
                f.rt(90)
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(35)
                f.lt(90)
                f.end_fill()
                f.penup()
                f.setpos((-32 * numplayers) + 10, -110)
                f.color('black')
                f.pendown()
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(35)
                f.rt(90)
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(70)
                f.rt(90)
                f.fd((50 * numplayers) + 25)
                f.rt(90)
                f.fd(35)
                f.lt(90)
                f.penup()
                f.setpos(0, -10)
                f.write('Chips', align='center', font=('arial', 30, 'normal'))
                f.setpos((-25 * numplayers), -150)
                f.color('black')
                for i in range(numplayers):  # I would recommend to use a list with the chip values
                    # to show the scores in game, as you could just edit chips below
                    # to be chips[i]
                    f.write(chips, align='left', font=('arial', 30, 'normal'))
                    f.fd(50)
                f.setpos((-25 * numplayers), -115)
                num = 1
                for i in range(numplayers):  # I would recommend to use a list with the chip values
                    # to show the scores in game, as you could just edit chips below
                    # to be chips[i]
                    f.write(num, align='left', font=('arial', 30, 'normal'))
                    f.fd(50)
                    num += 1
                waiting = True
                while waiting:
                    f.setpos(0, 45)
                    f.write(('Roll', rolls), align='center', font=('arial', 10, 'normal'))
                    keyf = current_key
                    if keyf == "f":  # This while loop is to break whenever all players turns have passed
                        keyf = dicerolls(3)
                        f.setpos(-225, 100)
                        if keyf[0] == '1':
                            one()
                        elif keyf[0] == '2':
                            two()
                        elif keyf[0] == '3':
                            three()
                        elif keyf[0] == '4':
                            four()
                        elif keyf[0] == '5':
                            five()
                        elif keyf[0] == '6':
                            six()
                        f.setpos(-50, 100)
                        if keyf[1] == '1':
                            one()
                        elif keyf[1] == '2':
                            two()
                        elif keyf[1] == '3':
                            three()
                        elif keyf[1] == '4':
                            four()
                        elif keyf[1] == '5':
                            five()
                        elif keyf[1] == '6':
                            six()
                        f.setpos(125, 100)
                        if keyf[2] == '1':
                            one()
                        elif keyf[2] == '2':
                            two()
                        elif keyf[2] == '3':
                            three()
                        elif keyf[2] == '4':
                            four()
                        elif keyf[2] == '5':
                            five()
                        elif keyf[2] == '6':
                            six()
                        player += 1  # This is a makeshift turn system, please remove it when making final code
                        f.setpos(0, 55)
                        f.write('press n to keep roll or f to roll again', align='center', font=('arial', 12, 'normal'))
                        # ^^^ replace this with whichever keyboard input will be used to continue
                        current_key = ""
                        keyf = current_key
                        while waiting:
                            keyf = current_key
                            if keyf == 'n':
                                # f.shape('dice1')
                                f.clear()  # This clears the dice layer
                                waiting = False
                                rolls = 1
                            if keyf == 'f':
                                rolls += 1
                                f.clear()
                                waiting = False
                            else:
                                # [ass]  ?????
                                pass

# this code never runs in normal "gameplay", see my paragraph below for more. -Hayden
while current_key == "up":
    print("updog")
    current_key = ""
    """nope! I think this means everything has to run within the
    while True loop otherwise keyboard input isn't registered. I really hope 
    this doesnt effect anything other than key calling it shouldn't since its
    just a 0.4 sec break BEFORE the other functions run. this could also mean
    that any keyboard listens wont run while the code is executing, OR it 
    means that everything will just be delayed by 0.4 seconds who knows."""
