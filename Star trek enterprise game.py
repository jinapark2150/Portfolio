import sys
import random
import time
import math

# create the universe
empty = '.'
enterprise = 'E'
klingon = 'K'
star = '*'
k_energy, e_energy = 50, 125 
map_row, map_col = 9, 12 
old_e_row, old_e_col = 0, 0 

random_coordinates = [] 
star_location = [] 
klingon_location = {}
enterprise_location = {} 

#abbreviated commands dictionary
short = {
    'q':    'quit',
    'n':    'north',
    's':    'south',
    'e':    'east',
    'w':    'west',
    'd':    'destruct'
}


def random_star_klingon_enterprise():
    # make 15 random coordinates
    for i in range(15):
        while True:
            row = random.randint(0,map_row-1)
            col = random.randint(0,map_col-1)
            if (row, col) not in random_coordinates:
                break;
        random_coordinates.append((row, col))

def random_star():
    # make 10 stars
    for i in range(10):
        star_location.append(random_coordinates[i])


def random_klingon():
    # make 4 klingons
    for i in range(10,14):
        klingon_row, klingon_col = random_coordinates[i]
        klingon_location[(klingon_row, klingon_col)]= k_energy

def random_enterprise():
    # make 1 enterprise
    enterprise_row, enterprise_col = random_coordinates[14]
    enterprise_location[(enterprise_row, enterprise_col)] = e_energy

def make_grid(map):
    random_star_klingon_enterprise() 
    random_star() 
    random_klingon() 
    random_enterprise() 
    for col in range(9):
        map.append([empty] * 12)
    for i in star_location:
        s_row, s_col = i
        map[s_row][s_col] = star
    for i in klingon_location:
        k_row, k_col = i
        map[k_row][k_col] = klingon
    for i in enterprise_location:
        e_row, e_col = i
        map[e_row][e_col] = enterprise


def update_grid(map):
    checker = False
    old_e_row, old_e_col = (0,0) 
    for i in klingon_location: 
        k_row, k_col = i
        map[k_row][k_col] = klingon
    for i, j in enterprise_location.items(): 
        if j == 0: 
            old_e_row, old_e_col = i 
            map[old_e_row][old_e_col] = empty 
            checker = True 
        else:
            e_row, e_col = i 
            map[e_row][e_col] = enterprise
    if checker: 
        del enterprise_location[(old_e_row, old_e_col)] 

def print_grid(map):
    # print map
    for i in map:
        for j in i:
            print(j, end=' ')
        print()


def new_enterprise(direction):
    [(old_row, old_col)] = enterprise_location
    new_row, new_col = old_row, old_col
    if direction == 'north':
        new_row = old_row - 1
    elif direction == 'south':
        new_row = old_row + 1
    elif direction == 'west':
        new_col = old_col - 1
    elif direction == 'east':
        new_col = old_col + 1
    return new_row, new_col, old_row, old_col

def move_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction) 
    key = (new_row, new_col) 
    energy_reduced = near_klingon_energy(direction) 
    if energy_reduced != 0: 
        if not klingon_check_enterprise(direction): 
            enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)] 
            enterprise_location[(new_row, new_col)] = enterprise_location[(new_row, new_col)] - energy_reduced 
            enterprise_location[(old_row, old_col)] = 0 
            print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key]) 
        else: 
            if not klingon_energy_checker(key): 
                enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)]
                enterprise_location[(new_row, new_col)] = enterprise_location[(new_row, new_col)] - energy_reduced
                enterprise_location[(old_row, old_col)] = 0
                print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
            else: 
                if enterprise_location[(old_row,old_col)] > 0:
                    enterprise_location[(old_row, old_col)] = enterprise_location[(old_row, old_col)] - energy_reduced 
                    print('The Enterprise at', (old_row,old_col), 'Energy remaining:', enterprise_location[(old_row,old_col)])
    else: 
        if not klingon_check_enterprise(direction): 
            enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)]
            enterprise_location[(old_row, old_col)] = 0
            print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
        else: 
            if not klingon_energy_checker(key): 
                enterprise_location[(new_row,new_col)] = enterprise_location[(old_row,old_col)]
                enterprise_location[(old_row, old_col)] = 0
                print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
            else: 
                print('The Enterprise at', (old_row, old_col), 'Energy remaining:',
                      enterprise_location[(old_row, old_col)])

def bound_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    if new_row < 0 or new_col < 0 or new_row >= map_row or new_col >= map_col:
        print("You can't move outside the universe")
        print("Try again!")
        return False
    return True


def star_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    if (new_row, new_col) in star_location:
        print("You can't fly into stars!")
        print("Try again!")
        return False
    return True


def klingon_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    for i in klingon_location:
        if i == (new_row, new_col):
            return True
            break
    return False

def klingon_energy_checker(key):
    if klingon_location[key] <= 0:
        return False
    return True

def meet_klingon_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    key = (new_row, new_col) 
    if key in klingon_location: 
        print("The Klingon at ", key, "got attacked!", end=' ') 
        energy_reduced = random.randint(23,29) 
        klingon_location[key] = klingon_location[key] - energy_reduced 
        if klingon_energy_checker(key): 
            print("Energy remaining:", klingon_location[key]) 
        else: 
            del klingon_location[key] 
            print("Boop! Klingon removed")


def calculate_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def get_near_klingon_enterprise(direction):
    near_klingon = [] 
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    for i in klingon_location: 
        x, y = i
        if calculate_distance(x,y,new_row,new_col) < 3: 
            near_klingon.append(i)
    return near_klingon

def near_klingon_energy(direction):
    near_klingon = get_near_klingon_enterprise(direction) 
    total_energy_reduced = 0
    if len(near_klingon) > 0:
        for i in near_klingon:
            chance = random.randint(1, 100) 
            if chance <= 43:
                energy_reduced = random.randint(5, 11) 
                print("The Klingon at", i, "attacked enterprise by", energy_reduced, 'energy') 
                total_energy_reduced = total_energy_reduced + energy_reduced
    return total_energy_reduced 


def count_klingon_checker():
    if len(klingon_location) <=0:
        return True
    return False

def enterprise_energy_checker():
    temp = list(enterprise_location.values())
    if temp[0] <=0:
        return True
    return False


def game_loop():
    map = []
    make_grid(map) 
    while True: 
        print_grid(map) 
        
        # command input check
        while(True): 
            cmd_input = input('Command:')
            # abbreviated commands execute
            cmd = cmd_input.lower() 
            long = list(short.values()) 
            if cmd in long: 
                break; 
            elif cmd in short: 
                cmd = short[cmd]
                break;
            else: 
                print("I don't know that command.")

        # quit and destruct commands
        if cmd == 'quit':
            sys.exit()
        elif cmd == 'destruct':
            i = 5
            while i >= 1:
                print(i)
                time.sleep(1)
                i = i - 1
            print('*** The Enterprise has self-destructed ***')
            print('GAME OVER')
            sys.exit()


        if bound_check_enterprise(cmd): 
            if star_check_enterprise(cmd):
                meet_klingon_enterprise(cmd) 
                move_enterprise(cmd) 
                update_grid(map)


        if count_klingon_checker(): 
            print_grid(map) 
            print("WIN!")
            break;

        if enterprise_energy_checker() : 
            print("Lose...")
            break;


#Execute!
game_loop()
