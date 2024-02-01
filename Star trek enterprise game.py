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
    key = (new_row, new_col) #새로 움직일 좌표를 key라 저장하고
    energy_reduced = near_klingon_energy(direction) #이거는 밑에 'near_klingon_energy()'라는 메소드에서 근처에 K있으면 에너지 깎이는 값이 얼마인지 받아와서 저장하고
    if energy_reduced != 0: #만약 깎이는 에너지가 있는데
        if not klingon_check_enterprise(direction): #만약 깎이는 에너지가 있는데 내가 가려는 위치에 K가 없으면 (상황1)
            enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)] #새로운 좌표를 딕셔너리에 추가하면서 옛날 좌표의 에너지값을 저장해주고
            enterprise_location[(new_row, new_col)] = enterprise_location[(new_row, new_col)] - energy_reduced #에너지 깎이는게 있었으니 그걸 깎아주고
            enterprise_location[(old_row, old_col)] = 0 #옛날좌표의 에너지는 0으로 만들어놨어, 앞에서도 잠깐 써놨는데 update_grid()에서 옛날좌표는 empty모양으로 바꿔주려고 에너지값은 임의로 0으로 해서 모양바꾸고 그뒤에 지울수 있게!
            print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key]) #E위치랑 에너지값 프린트
        else: #만약 깎이는 에너지가 있는데 내가 가려는 위치에 K가 있으면
            if not klingon_energy_checker(key): #만약 깎이는 에너지가 있는데 내가 가려는 위치에 K가 있고 K의 에너지가 0이하라 K사라지고 E가 옮기는 상황 (상황2)
                enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)]
                enterprise_location[(new_row, new_col)] = enterprise_location[(new_row, new_col)] - energy_reduced
                enterprise_location[(old_row, old_col)] = 0
                print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
            else: #만약 깎이는 에너지가 있는데 내가 가려는 위치에 K가 있고 K의 에너지가 1보다 커서 못가 (상황3)
                if enterprise_location[(old_row,old_col)] > 0:
                    enterprise_location[(old_row, old_col)] = enterprise_location[(old_row, old_col)] - energy_reduced #움직이지 않고 에너지만 빼줘
                    print('The Enterprise at', (old_row,old_col), 'Energy remaining:', enterprise_location[(old_row,old_col)])
    else: #깎이는 에너지가 없으면
        if not klingon_check_enterprise(direction): #깎이는 에너지도 없고 내가 가려는 곳에 K가 없어 간다 (상황4)
            enterprise_location[(new_row, new_col)] = enterprise_location[(old_row, old_col)] #에너지 변화업시 움직이기만
            enterprise_location[(old_row, old_col)] = 0
            print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
        else: #깎이는 에너지는 없는데 내가 가려는곳에 K가 있다
            if not klingon_energy_checker(key): #그 K를 먹어버릴수 있는 상황이라 움직여 (상황5)
                enterprise_location[(new_row,new_col)] = enterprise_location[(old_row,old_col)]
                enterprise_location[(old_row, old_col)] = 0
                print('The Enterprise at', key, 'Energy remaining:', enterprise_location[key])
            else: #하지만 K를 먹을 수없어서 그냥 위치도 에너지도 가만히.. (상황6)
                print('The Enterprise at', (old_row, old_col), 'Energy remaining:',
                      enterprise_location[(old_row, old_col)])


#grid밖으로 나가면 안되니까 그거 확인해주는 메소드! 밖으로 나가면 False, 안에 잘 있으면 True
def bound_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction) #위에서 만들어논 'new_enterprise()'메소드 이용하면 이동전좌표랑 이동후좌표 편하게 사용할 수 있어서 사용했어
    if new_row < 0 or new_col < 0 or new_row >= map_row or new_col >= map_col:
        print("You can't move outside the universe")
        print("Try again!")
        return False
    return True


#star위치로는 이동못하니까 star위치랑 이동하려는 위치랑 같은지 아닌지 확인하는 메소드. 같으면 False, 이동할수있으면(같지않으면) True
def star_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    if (new_row, new_col) in star_location:
        print("You can't fly into stars!")
        print("Try again!")
        return False
    return True


#이거는 내가 가려는 위치에 K가 있으면 True, 가려는 위치에 K가 없으면 False
def klingon_check_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    for i in klingon_location:
        if i == (new_row, new_col):
            return True
            break
    return False


# K의 에너지가 0이하면(사라져야한다면) False, 에너지가 있으면(K가 존재할수 있다면) True
def klingon_energy_checker(key):
    if klingon_location[key] <= 0:
        return False
    return True


# K랑 E랑 만났을때 E가 K 먹어버리거나 때리는 메소드
def meet_klingon_enterprise(direction):
    new_row, new_col, old_row, old_col = new_enterprise(direction) #일단 E 움직이기 전후 위치 받아와서
    key = (new_row, new_col) #key는 가려는 좌표
    if key in klingon_location: #가려는 좌표에 K가 있으면
        print("The Klingon at ", key, "got attacked!", end=' ') #일단 때려
        energy_reduced = random.randint(23,29) #23~28사이 에너지 랜덤으로 구해서
        klingon_location[key] = klingon_location[key] - energy_reduced #그 K좌표의 에너지를 빼!
        if klingon_energy_checker(key): #E가 때렸는데도 K의 에너지가 남아있다면
            print("Energy remaining:", klingon_location[key]) #에너지 뽑아주고
        else: #K가 이제 에너지 없으면
            del klingon_location[key] # K삭제! (여기서 그 먹혀진 K의 좌표랑 에너지값 둘다를 없애줬으니까 위에서 'update_grid()'할때 지금 삭제된애들 빼고 남은애들만 표시돼!..)
            print("Boop! Klingon removed")
            # E는 못움직이는상황들도 있고 이래저래.. 근데 머리 좀더 쓰면 뭔가 E도 더 간단하게 할거 같은데.. 하튼 K는 그냥 계속 없어지는게 끝이니 딱히 따로 예전 좌표 남겨둘 이유가 없어서..이런식으로 써놨어


#Euclidean distance구하는 메소드 E랑 K근처인지 아닌지 거리 계산식
def calculate_distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


#위에서 만든 'calculate_distance()'이용해서 E 근처인 K좌표들을 저장하는 메소드!
def get_near_klingon_enterprise(direction):
    near_klingon = [] #근처 K들 저장할 좌표
    new_row, new_col, old_row, old_col = new_enterprise(direction)
    for i in klingon_location: #k좌표들 중에서
        x, y = i
        if calculate_distance(x,y,new_row,new_col) < 3: #거리가 3미만이면
            near_klingon.append(i) #그 좌표 저장
    return near_klingon


#이제 그 근처 K좌표들에서 각각 43%확률로 5~10사이의 에너지를 뺏는거 그러면 계산하면 총 에너지 얼마나 뺏기는지 구하는 메소드
def near_klingon_energy(direction):
    near_klingon = get_near_klingon_enterprise(direction) #위에 'get_near_klingon_enterprise()'메소드 이용해서 근처K좌표들 저장하고
    total_energy_reduced = 0
    if len(near_klingon) > 0: #근처에 K좌표가 있으면
        for i in near_klingon: #각각 좌표들에 대해서
            chance = random.randint(1, 100) #랜덤확률
            if chance <= 43: #그게 43이하면
                energy_reduced = random.randint(5, 11) #5~10사이에 랜덤한 에너지 뽑아서
                print("The Klingon at", i, "attacked enterprise by", energy_reduced, 'energy') #i위치에 있는 K로부터 E가 'energy_reduced'만큼 에너지 뺏김
                total_energy_reduced = total_energy_reduced + energy_reduced #총 에너지 손실에 각각거를 계속 더해줘
    return total_energy_reduced #총 E가 근처 K한테 뺏길 에너지양


#이거는 게임종료 위해서 만든 boolean메소드. K의 갯수가 0이하면 E가 승리! E가 다 먹어버려서 승리!
def count_klingon_checker():
    if len(klingon_location) <=0:
        return True
    return False


#위에 'count_klingon_checker()'랑 마찬가지로 게임종료 위해서 만든 boolean 메소드. E의 에너지값이 0보다 작아지면 lose.. 근데 내가 실행해보니까 바보아닌이상 그럴일 잘 없겠더라
def enterprise_energy_checker():
    temp = list(enterprise_location.values())
    if temp[0] <=0:
        return True
    return False


#main()이랑 같은 메소드. 여기가 이제 총괄 실행창같은 느낌
def game_loop():
    map = []
    make_grid(map) #일단 처음에 map을 만들어. 'make_grid()'메소드안에 랜덤으로 좌표 뽑고 모양정하는거 코드 써놨어 위에
    while True: #이제 계속 이 루프를 돌릴거야 게임종료해야할 상황(K가 없어지거나, E에너지가 0이하가 되는 상황빼고는 계속 돌려
        print_grid(map) #그리드를 화면에 프린트해

        # command input check
        while(True): #여기는 이제 command input 관련 루프
            cmd_input = input('Command:')
            # abbreviated commands execute
            cmd = cmd_input.lower() #혹시몰라서 대문자로 쳐도 인식하도록 cmd_imput를 다 자동으로 소문자로 바꾼걸 cmd라는 변수에 저장 (딕셔너리에 다 소문자로 써놔서)
            long = list(short.values()) #quit, south...기타등등 딕셔너리 value부분 값들로 써도 인식하도록 확인
            if cmd in long: #quit, south..기타등등 맞으면
                break; #잘 입력한거니까 이제 루프 나와
            elif cmd in short: #이하동문
                cmd = short[cmd]
                break;
            else: #만약 이상한거친거면
                print("I don't know that command.") #루프못나오고 다시 input받기

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

        # 위에서 써논 메소드들을 이제 실행창에서 한번에 실행시켜줘
        if bound_check_enterprise(cmd): #먼저 cmd에 입력된 방향이 창안에 있는건지 확인하고
            if star_check_enterprise(cmd): #별이 안막는지 확인한후에
                meet_klingon_enterprise(cmd) #K를 만나게되는 상황이면 먹어버리거나 에너지공격하거나 하고
                move_enterprise(cmd) #E를 드디어 움직이고
                update_grid(map)#다시 map에 모양들을 (E,K)위치 조정해서 다시 저장

        #그리고 다시 위로 올라가 print_grid()로 화면에 프린트해서 다시 input받고 돌고돌고돌고....하는데
        #만약
        if count_klingon_checker(): #K가 0개야, 그럼 이제 break로 loop 종료시키기
            print_grid(map) #### K가 다 사라지고 E만 남은 맵이 보이면서 끝
            print("WIN!")
            break;

        if enterprise_energy_checker() : #E가 에너지가 없어져, 그럼 이제 break로 loop 종료시키기
            print("Lose...")
            break;


#실행창을 이제 실행!
game_loop()
