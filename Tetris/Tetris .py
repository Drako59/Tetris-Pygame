import time

import pygame
import random
import sys
print(sys.version)

# from screeninfo import get_monitors


#ליצור כלאס של בלוק אשר יכלול פונקציה של הופעה סיבוב תזוזה בנוסף לחלק כל 60 פיקלסים לתחום שבו אני אבדוק מה הY הגבוה ביותר ולפי זה יקבע על נחיתת הבלוקים

class block:
    global block_models
    block_models = {"purple": [[1,1,1],
                               [0,1,0]],

                    "orange" : [[0,0,1],
                                [1,1,1]],

                   "light blue" : [[1],
                                   [1],
                                   [1],
                                   [1]],

                   "blue" : [[1,0,0],
                             [1,1,1]],

                   "yellow" : [[1,1],
                               [1,1]],

                   "green" : [[0,1,1],
                              [1,1,0]],
                   "red"  : [[0,1],
                             [1,1],
                             [1,0]]}
    name = ""
    # def __init__(self,image_url: str == "",size: tuple,color : str ) -> None:
    def __init__(self,size: tuple,color : str ) -> None:
        # self.block = pygame.image.load(image_url)
        # self.block = pygame.transform.scale(self.block , (60,60))
        self.size = size
        # self.block = pygame.transform.scale(self.block ,(self.size[0],self.size[1]))
        self.name = color
        self.blocks : list
    def create_block(self):
        block_shape = [None,None,None,None]
        block_place = [[0,0],[0,0],[0,0],[0,0]]

        #1
        # j = 0
        # for i in range(-self.size[0],2 * self.size[0] + 1,self.size[0]):
        #     block_place[j][0] = WIDTH / 2 + i
        #     j += 1
        # block_place[3][0] = WIDTH / 2
        # block_place[3][1] = 60
        i = 0
        k = 0
        for row in range(len(block_models[self.name])):
            for col in range(len(block_models[self.name][1])):
                if block_models[self.name][row][col] == 1:
                    k = 2
                    if self.name == "light blue":
                        k = 4
                    block_place[i] = [(WIDTH / 2) + (col * self.size[1] - self.size[1]),row * self.size[0] - k * self.size[1]]
                    print(block_place)
                    i += 1
        for i in range(4):
            block_shape[i] = pygame.Rect(block_place[i][0],block_place[i][1],self.size[0],self.size[1])
        self.blocks = block_shape
        return block_shape.copy() , block_place.copy()

    def check_continue_x(self,blocks, size_block, board_block, i) -> bool:
        for block in blocks:
            if block.x > 0 and block.x + size_block < WIDTH and block.y > 0:
                if board_block[int(block.y / size_block) + 1][int(block.x / size_block) + i]:
                    return False

        return True

    def check_continue(self,blocks, size_block, board_block) -> bool:
        from copy import deepcopy
        board_block = deepcopy(board_block)
        blocks = blocks.copy()
        for block in blocks:
            if block.y >= 0:
                if block.bottom < HEIGTH:
                    # if (int(block.y / size_block) + next_rows < len(board_block  -1)):
                    if board_block[int(block.y / size_block) + 2][int(block.x / size_block)]:
                        return False
                else:
                    return False
        return True


    def check_lose(self,board_block):
        for col in board_block[0]:
            if col:
                return True
        return False
    def go_down(self,blocks) -> None:
        for block in blocks:
            if block.bottom == HEIGTH:
                return None
        for i in range(len(blocks)):
            blocks[i] = blocks[i].move(0,self.size[1])
        self.blocks = blocks
    def move_right(self,blocks) -> None:
        if self.check_continue_x(blocks, self.size[1], board_blocks,1):
            for block in blocks:
                if block.x + self.size[0] == WIDTH:
                    return
            for i  in range(len(blocks)):
                blocks[i] = blocks[i].move(self.size[0],0).copy()
            self.blocks = blocks

    def move_left(self,blocks) -> None:
        if self.check_continue_x(blocks, self.size[1], board_blocks, -1):
            for block in blocks:
                if block.x == 0:
                    return
            for i in range(len(blocks)):
                blocks[i] = blocks[i].move(-self.size[0],0).copy()
            self.blocks = blocks



    def rotate(self,blocks) -> None:
        # if check_continue_x(blocks, self.size[1], board_blocks, 1) and  check_continue_x(blocks, self.size[1], board_blocks,-1):
        global rotation
        match self.name:
            case "purple":
                # def rotate(self,blocks) -> None:
                #[0,0,0
                # 1,2,3
                # 0,4,0]

                match rotation:
                    case 1:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change -1].move(self.size[0],-self.size[1]).copy()
                        # [0,1,0
                        #  0,2,3
                        #  0,4,0]
                    case 2:
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0],-self.size[1]).copy()
                        #[0,1,0
                        # 4,2,3
                        # 0,0,0]
                    case 3:
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0],self.size[1]).copy()
                        #[0,1,0
                        # 4,2,0
                        # 0,3,0]
                        rotation = 0
                        return None

                    case 0:
                        #[0,0,0
                        # 1,2,3
                        # 0,4,0]
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change-1].move(self.size[0],-self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change-1].move(self.size[0], self.size[1]).copy()
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change-1].move(-self.size[0], self.size[1]).copy()
                rotation += 1
            case "orange":

                match rotation:
                    #[0,0,1
                    # 2,3,4
                    # 0,0,0]
                    case 1:
                        block_change = 1
                        blocks[block_change -1] = blocks[block_change - 1].move(-2 * self.size[0],0).copy()
                        block_change = 2
                        blocks[block_change -1] = blocks[block_change - 1].move(self.size[0],-self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], self.size[1]).copy()
                        #[1,2,0
                        # 0,3,0
                        # 0,4,0]
                    case 2:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change -1].move(-self.size[0],2* self.size[1]).copy()

                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],-self.size[1]).copy()
                        # [0,0,0
                        #  1,3,4
                        #  2,0,0]

                    case 3:
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],0).copy()
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],-self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(0,self.size[1]).copy()
                        rotation = 0
                        return
                        # [0,1,0
                        #  0,3,0
                        #  0,2,4]
                    case 0:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],0).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], -self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, 0).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, -self.size[1]).copy()
                        #[0,0,1
                        # 2,3,4]
                rotation += 1
            case "light blue":
                match rotation:
                    # [0,1,0,0
                    # 0,2,0,0
                    # 0,3,0,0
                    # 0,4,0,0]

                    case 1:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], -self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(2 * self.size[0], -2 * self.size[1]).copy()
                        # [0,0,0,0
                        # 1,2,3,4
                        # 0,0,0,0
                        # 0,0,0,0]
                    case 2:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(2 * self.size[0], -self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], 0).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], 2 * self.size[1]).copy()
                        # [0,0,1,0
                        # 0,0,2,0
                        # 0,0,3,0
                        # 0,0,4,0

                    case 3:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0], self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], 0).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, -self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], -2 * self.size[1]).copy()
                        # [0,0,0,0
                        # 1,2,3,4
                        # 0,0,0,0
                        # 0,0,0,0]
                        rotation = 0
                        return
                    case 0:

                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], -self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0], 2 * self.size[1]).copy()
                rotation += 1

            case "blue":
                #[1,0,0
                # 2,3,4
                # 0,0,0]
                match rotation:
                    case 1:
                        block_change = 1
                        blocks[block_change - 1 ] = blocks[block_change - 1].move(0,2 * self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(0,0).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0],-self.size[1]).copy()
                        #[0,4,0
                        # 0,3,0
                        # 1,2,0]
                    case 2:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(2 * self.size[0],0).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],-self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0],self.size[1]).copy()
                        # [0,0,0
                        #  4,3,2
                        #  0,0,1]
                    case 3:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(0,-2 * self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], -self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], self.size[1]).copy()
                        rotation = 0
                        return
                        # [0,2,1
                        #  0,3,0
                        #  0,4,0]
                    case 0:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0],0).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0], self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0], -self.size[1]).copy()
                        rotation = 0
                rotation += 1
            case"yellow":
                pass
            case "green":
                #[0,1,2
                # 3,4,0]
                match rotation:
                    case 1:
                        block_change = 3;
                        blocks[block_change - 1] = blocks[block_change -1].move(0, - self.size[1]).copy()
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0] , -self.size[1]).copy()
                        #[2,0,0
                        # 3,1,0
                        # 0,4,0]
                    case 2:
                        block_change = 2
                        blocks[block_change - 1] = blocks[block_change - 1].move( 2 * self.size[0],self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, self.size[0]).copy()
                        # [0,1,2
                        # 3,4,0]
                    case 3:
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move( self.size[0], -2 * self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],0).copy()
                        rotation = 0
                        return
                        # [0,3,0
                         # 0,1,2
                         # 0,0,4]
                    case 0:
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0] , 2 * self.size[1]).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(-self.size[0],0).copy()
                rotation += 1
            case "red":

                #[0,0,1
                # 0,2,3
                # 0,4,0]
                match rotation:
                    case 1:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0],0).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, -2 * self.size[1]).copy()
                        #[1,4,0
                        # 0,2,3
                        # 0,0,0]
                    case 2:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(0, 2 * self.size[1]).copy()
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(-2 * self.size[0],0).copy()
                        #[0,4,0
                        # 3,2,0
                        # 1,0,0]
                    case 3:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(2 * self.size[0],0).copy()
                        block_change = 4
                        blocks[block_change - 1] = blocks[block_change - 1].move(0,2 * self.size[1]).copy()
                        rotation = 0
                        return
                        #[0,0,0
                        # 3,2,0
                        # 0,4,1]
                    case 0:
                        block_change = 1
                        blocks[block_change - 1] = blocks[block_change - 1].move(0,-2 * self.size[1]).copy()
                        # block_change = 2
                        # blocks[block_change - 1] = blocks[block_change - 1].move(self.size[0],80)
                        block_change = 3
                        blocks[block_change - 1] = blocks[block_change - 1].move(2 * self.size[0], 0).copy()
                        #[0,0,1
                        # 0,2,3
                        # 0,4,0]
                rotation += 1
        self.blocks = blocks

    def check_rotate(self, blocks, board_blocks) -> None:

        global rotation
        rotation_backup = rotation
        # print(rotation) # debug staff
        import copy
        blocks_backup = copy.deepcopy(blocks)
        self.rotate(blocks)
        for block in blocks:
            if  (block.x >= 0 and block.x <= WIDTH - self.size[0]):
                if (int(block.x / self.size[0]) >= len(board_blocks[0]) or int(block.x/ self.size[0]) < 0) or (int(block.y / self.size[1]) >= len(board_blocks) or int(block.y / self.size[1]) < 0):
                        # if rotation == 0:
                        #     rotation = 3
                        # else:
                        #     rotation -= 1
                    # rotation = rotation_backup
                    return blocks_backup.copy(),rotation_backup
                if board_blocks[int(block.y / self.size[1]) + 1][int(block.x / self.size[0])]: #add plus 1 because the board list is bigger by one for check lose more usful and playable
                    # rotation = rotation_backup
                    return blocks_backup.copy(),rotation_backup
            else:
                # rotation = rotation_backup
                return blocks_backup.copy(),rotation_backup
        return blocks.copy(),rotation
        # blocks = blocks_backup
    def hard_drop(self,blocks,board_blocks) -> None:
        # for block in blocks:
        #     for row in range(len(board_blocks)):
        #         col = int(blocks.x / 60)
        #         if board_blocks[row][col]:
        while True:
            print("loop")
            if self.check_continue(blocks,self.size[0],board_blocks):
                    self.go_down(blocks)
            else:
                return









def main_page():
    while True:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                x,y = pygame.mouse.get_pos()



def create_2d_list(rows,cols) -> list[list]:
    D2_list : list[list] = []
    for i in range(rows):
        organ = []
        for j in range(cols):
            organ.append(0)
        D2_list.append(organ)
    return D2_list.copy()
def print_2d_list(list_2d) -> list[list]:
    for row in list_2d:
        for col in row:
            print(col, end = " ")
        print()
def rotate(block , angle_rotate) -> object:
    # global angle
    # angle = angle + angle_rotate
    # if angle
    return pygame.transform.rotate(block, angle_rotate)

def return_row_full(list_2D) -> int:
    counter: int = 0
    for row in range(len(list_2D)):
        counter = 0
        for col in range(len(list_2D[row])):
            if list_2D[row][col] == 0:
                break
            counter += 1
        if counter  == len(list_2D[row]):
            return row
    return -1

# def return_row_full(list_2D) -> int:
#     for row in range(len(list_2D)):
#         counter = 0
#         for col in range(len(list_2D[row])):
#             if list_2D[row][col] == 1:  # Assuming 1 indicates a filled cell
#                 counter += 1
#             else:
#                 break
#         if counter == len(list_2D[row]):
#             return row
#     return -1
def del_row(list_2d,row) -> None:
    list_2d.pop(row)
def create_row(num) -> list:
    row = []
    for i in range(num):
        row.append(0)
    return row

# def check_continue_x(blocks,size_block,board_block,i) -> bool:
#     for block in blocks:
#         if block.x > 0 or block.x + size_block < WIDTH:
#             if board_block[int(block.y / 60)][int(block.x / 60) + i]:
#                 return False
#
#     return True
# def check_continue(blocks,size_block,board_block) -> bool:
#     for block in blocks:
#         if block.bottom < HEIGTH:
#             if board_block[int(block.y  / size_block) + 1][int(block.x / size_block)]:
#                 return False
#     return True
def main():
    # start_time = time.time()
    pygame.init()
    backSound = pygame.mixer.music.load("Sounds/Tetris.mp3")
    full_row_sound = pygame.mixer.Sound("Sounds/full_row_sound.mp3")
    tetris_row_sound = pygame.mixer.Sound("Sounds/full_tetris_sound.mp3")
    hard_drop_sound = pygame.mixer.Sound("Sounds/Hard-drop-sound.mp3")
    set_block_sound  = pygame.mixer.Sound("Sounds/block_set_sound.mp3")
    lose_sound = pygame.mixer.Sound("Sounds/lose_sound_(I_AM_COMING_FOR_YOU).mp3")
    global score,level,level_speed,WIDTH,HEIGTH,positions,board_blocks
    global level
    score = 0
    level = 1
    level_speed = 10
    next_level = 10_000
    bonus_score = 3000
    global WIDTH
    global HEIGTH
    global positions
    monitors = pygame.display.get_desktop_sizes()
    print(monitors)
    # WIDTH = monitors[0][0] // 3
    # size = WIDTH // 10
    # HEIGTH = size * 16
    WIDTH = monitors[0][0] / 1920 * 480
    if WIDTH == 0:
        WIDTH = 300
    size = WIDTH / 10
    HEIGTH = size * 20
    WIDTH = size * 10
    positions = create_2d_list(int(HEIGTH / size) + 1,int(WIDTH / size))
    global board_blocks
    board_blocks = create_2d_list(int(HEIGTH / size) + 1,int(WIDTH / size))
    debug_list = create_2d_list(int(HEIGTH / size) + 1,int(WIDTH / size))
    print(board_blocks)
    color_blocks = create_2d_list(int(HEIGTH / size) + 1,int(WIDTH / size))
    SIZE = (WIDTH,HEIGTH)
    mikum_list: list[list] = create_2d_list(int(HEIGTH / size) + 1, int(WIDTH / size))
    screen = pygame.display.set_mode(SIZE)
    block_url = { "purple" : "background remvoer/purple.png",
                   "orange" : "background remvoer/orange block.png",
                   "light blue" : "background remvoer/light blue block.png",
                   "blue" : "background remvoer/blue block.png",
                   "yellow" : "background remvoer/yellow block.png",
                   "green" : "background remvoer/green block.png",
                   "red"  : "background remvoer/red block.png"}
    block_name = ("purple","orange","light blue","blue","yellow","green","red")
    block_exit = 0
    font = pygame.font.SysFont("Comic Sans MS",int(size / 48 * 20))
    text = font.render("Score: " + str(score),True,"white")
    # block_sizes = [[180,120],[180,120],[60,240],[180,120],[120,120],[180,120],[120,180]]

    clock = pygame.time.Clock()
    run = True
    # rnd = random.randint(0,6)
    # block = pygame.image.load(block_list[block_name[rnd]])
    # block = pygame.transform.scale( block, (block_sizes[rnd][0],block_sizes[rnd][1]))
    # block_x_pose = (WIDTH /2)  - (block.get_width() / 2);
    block_y_pose = 0
    # background = pygame.image.load("background remvoer/background_3.jpeg")
    # background = pygame.transform.scale(background,(WIDTH,HEIGTH))
    # screen.blit(background,(0,0))
    background_white = pygame.Rect(0,0,WIDTH,HEIGTH)
    pygame.draw.rect(screen,"black",background_white)
    blocks_list = []
    angle = 0
    counter = 0
    block_down_counter = 0
    allow_key = True
    pause = False

    #start screen--------------------------------------------------------------------------------------------------------
    pygame.mixer.music.play(loops = -1)
    pygame.mixer.music.set_volume(0.1)
    x = WIDTH / 2 - 130
    y = HEIGTH / 2 - 90
    start_background = pygame.Rect(x,y,size * 5,size * 8)
    while not run:
        pygame.draw.rect(screen,"White",start_background)
    #-------------------------------------------------------------------------------------------------------------------
    while run:


        # set block details
        global rotation
        blocks = []
        rotation = 1
        rnd = random.randint(0, 6)
        color_key  = block_name[rnd]
        blocks_list.append(0)
        blocks_list[counter] = block((size,size),block_name[rnd])
        blocks, blocks_mikum = blocks_list[counter].create_block()
        allow_key = True
        while True:
            block_down_premission = True

            #keys-----------------------------------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_z or event.key == pygame.K_UP:
                        blocks,rotation = blocks_list[counter].check_rotate(blocks, board_blocks)

                    if event.key == pygame.K_SPACE:
                        blocks_list[counter].hard_drop(blocks,board_blocks)
                        allow_key = False
                        pygame.mixer.Sound.play(hard_drop_sound)
                        # blocks_list[counter].rotate(blocks)
                    if event.key == pygame.K_m:
                        if not pause:
                            pygame.mixer.music.pause()
                            pause = True
                        else:
                            pygame.mixer.music.unpause()
                            pause = False
                    if event.key == pygame.K_ESCAPE:
                        _break =False
                        while True:
                            time.sleep(1)
                            for event in pygame.event.get():
                                if event.key == pygame.K_ESCAPE:
                                    _break =True
                                    break
                            if _break == True:
                                break

                    # if event.key == pygame.K_z:
                    #     block = rotate(block, 270)
                    # if event.key == pygame.K_x:
                    #     block = rotate(block, 90)

                    # if event.key == pygame.K_RIGHT and block_x_pose < WIDTH:
                    #     block_x_pose += 60
                    # if event.key == pygame.K_LEFT and block_x_pose > 0:
                    #     block_x_pose -= 60
            if allow_key:
                key = pygame.key.get_pressed()
                if key[pygame.K_DOWN]:
                    block_down_counter = 1
                    blocks_list[counter].go_down(blocks)
                    block_down_premission = False
                if key[pygame.K_RIGHT]:
                    blocks_list[counter].move_right(blocks)
                if key[pygame.K_LEFT]:
                    blocks_list[counter].move_left(blocks)


            # if key[pygame.K_RIGHT] and  block_x_pose < WIDTH - block_sizes[rnd][0]:
            #     block_x_pose += 60
            # if key[pygame.K_LEFT] and  block_x_pose > 0:
            #     block_x_pose -= 60
            # if key[pygame.K_z]:
            #     block = rotate(block,270)
            # if key[pygame.K_x]:
            #     block = rotate(block,90)
            #end keys-----------------------------------------------------------------------------


            clock.tick(10)
            start_time = time.time()
            # screen.blit(background, (0, 0))
            pygame.draw.rect(screen, "black", background_white)

            #print all the blocks---------------------------------------------------------------------------------------------
            for row in range(len(board_blocks)):
                for col in range(len(board_blocks[row])):
                    if board_blocks[row][col] != 0:
                        # print(color_blocks)
                        # print(row,col)
                        pygame.draw.rect(screen,color_blocks[row][col],board_blocks[row][col])
            # for user in blocks_list:
            #     for rect in user.blocks:
            #         pygame.draw.rect(screen,user.name,rect)

            for p in range(len(blocks)):
                pygame.draw.rect(screen,block_name[rnd],blocks[p],)
            screen.blit(text,(int(size / 48 * 20), int(size / 48 * 20)))
            pygame.display.flip()
            #-------------------------------------------------------------------------------------------------------------------
            for block_value in blocks:
                if block_value.bottom == HEIGTH:
                    block_exit = 1
                    blocks_list[counter].blocks = blocks.copy()
                    break

            if not blocks_list[counter].check_continue(blocks.copy(),blocks_list[counter].size[1],board_blocks):
                block_exit = 1
            num = 0

            if block_exit:
                for rect in blocks:
                    print(num)
                    num += 1
                    # print((rect.bottom / 60)-1,(rect.x + blocks_list[counter].size[0]))
                    print_2d_list(board_blocks)
                    # print_2d_list(debug_list)
                    y = int(rect.bottom / blocks_list[counter].size[0])-1
                    x = int((rect.x + blocks_list[counter].size[0]) / blocks_list[counter].size[0])-1
                    print(f"{rect.bottom}  {rect.x + blocks_list[counter].size[0]}")
                    print(f"{x}  {y}")
                    pygame.draw.rect(screen,"pink",rect)
                    debug_list[int(rect.y / blocks_list[counter].size[0] + 1)][int((rect.x + blocks_list[counter].size[0]) / blocks_list[counter].size[0])-1] = "[]"
                    positions[int(rect.y / blocks_list[counter].size[0]) + 1][int((rect.x + blocks_list[counter].size[0]) / blocks_list[counter].size[0])-1] = 1
                    print(int(rect.y / blocks_list[counter].size[0]))
                    print(rect.y)
                    board_blocks[int(rect.y / blocks_list[counter].size[0]) + 1 ][int((rect.x + blocks_list[counter].size[0]) / blocks_list[counter].size[0])-1] = rect.copy()
                    color_blocks[int(rect.y / blocks_list[counter].size[0] + 1)][int((rect.x + blocks_list[counter].size[0]) / blocks_list[counter].size[0])-1] = blocks_list[counter].name
                    print_2d_list(positions)
                if allow_key:
                    pygame.mixer.Sound.play(set_block_sound)

                #check for full row-----------------------------------------------------------------------------------------------
                # while (return_row_full(positions) + 1):
                #     row_pop = return_row_full(positions)
                #     # for rect in range(len(board_blocks[row_pop])):
                #     #     board_blocks[row_pop][rect] = board_blocks[row_pop][rect].move(0,blocks_list[counter].size[1])
                #     board_blocks.pop(row_pop)
                #     board_blocks.insert(0, create_row(int(WIDTH / blocks_list[counter].size[0])))
                #     positions.pop(row_pop)
                #     positions.insert(0, create_row(int(WIDTH / blocks_list[counter].size[0])))
                #     color_blocks.pop(row_pop)
                #     color_blocks.insert(0, create_row(int(WIDTH / blocks_list[counter].size[0])))
                #     print_2d_list(board_blocks)
                #     for row in range(len(board_blocks)):
                #         if row <= row_pop:
                #             for col in range(len(board_blocks[row])):
                #                 if board_blocks[row][col]:
                #                     board_blocks[row][col] = board_blocks[row][col].move(0,
                #                                                                          blocks_list[counter].size[1])
                #     score += 1000
                #     text = font.render(f"Score: {score}", True, "white")
                # if score == 10000:
                #     if level_speed > 0:
                #         level_speed -= 5
                # if block_down_counter % level_speed == 0:
                #     blocks_list[counter].go_down(blocks)
                # block_down_counter += 1
                #--------------------------------------------------------------------------------------------------------------
                block_exit = 0
                break
            row_pop_counter: int  = 0
            while (return_row_full(positions) + 1):
                row_pop_counter += 1
                row_pop = return_row_full(positions)
                # for rect in range(len(board_blocks[row_pop])):
                #     board_blocks[row_pop][rect] = board_blocks[row_pop][rect].move(0,blocks_list[counter].size[1])
                board_blocks.pop(row_pop)
                board_blocks.insert(0,create_row(int(WIDTH / blocks_list[counter].size[0])))
                positions.pop(row_pop)
                positions.insert(0,create_row(int(WIDTH / blocks_list[counter].size[0])))
                color_blocks.pop(row_pop)
                color_blocks.insert(0,create_row(int(WIDTH / blocks_list[counter].size[0])))
                print_2d_list(board_blocks)
                for row in range(len(board_blocks)):
                    if row <= row_pop:
                        for col in range(len(board_blocks[row])):
                            if board_blocks[row][col]:
                                board_blocks[row][col] = board_blocks[row][col].move(0,blocks_list[counter].size[1])
                pygame.mixer.Sound.stop(set_block_sound)
                score += 1000 + ((len(board_blocks) - row_pop) * 100)
                text = font.render(f"Score: {score}", True, "white")
            if row_pop_counter == 4:
                score += bonus_score
                text = font.render(f"Score: {score}", True, "white")
                if bonus_score < 10000:
                 bonus_score += 1000
                pygame.mixer.Sound.play(tetris_row_sound)
            elif row_pop_counter > 0:
                bonus_score = 3000
                pygame.mixer.Sound.play(full_row_sound)

            #level speed set---------------------------------------------------------------------------------
            if score > next_level:
                level_speed -= 1
                next_level += 1.2 * next_level
            if block_down_counter % level_speed == 0:
                if  block_down_premission:
                    blocks_list[counter].go_down(blocks)
            block_down_counter += 1
            # print_2d_list(board_blocks)
            #--------------------------------------------------------------------------------------------------

            # for row in range(len(board_blocks)):
            #     for col in range(len(board_blocks[row])):
            #         if board_blocks[row][col] != 0:
            #             print(color_blocks)
            #             print(row,col)
            #             pygame.draw.rect(screen,color_blocks[row][col],board_blocks[row][col])

            # screen.blit(block,(block_x_pose,block_y_pose))

            # if block_y_pose < HEIGTH - block_sizes[rnd][1]:
            #     block_y_pose += 60
        block_down_counter = 0
        counter += 1
        if blocks_list[counter - 1].check_lose(positions):
            break
        end_time = time.time()
        print(f"time took: {end_time - start_time}")
    pygame.mixer.Sound.play(lose_sound)
    text_score = text
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if not pause:
                        pygame.mixer.music.pause()
                        pause = True
                    else:
                        pygame.mixer.music.unpause()
                        pause = False
        pygame.draw.rect(screen, (0, 0, 0), background_white)
        for row in range(len(board_blocks)):
            for col in range(len(board_blocks[row])):
                if positions[row][col] != 0:
                    # print(color_blocks)
                    # print(row,col)
                    pygame.draw.rect(screen, color_blocks[row][col], board_blocks[row][col])
        screen.blit(text_score,(int(size / 48 * 20), int(size / 48 * 20)))
        x = WIDTH / 2 - 130
        y = HEIGTH / 2  - 90
        rec_ending = pygame.Rect(x, y, round(size / 48 * 300),round((size / 48) * 80))
        pygame.draw.rect(screen,"white",rec_ending)
        font = pygame.font.SysFont("Comic Sans MS", round(size / 48 * 40))
        text = font.render(f"You lost :(",True,(255,0,0))
        x = WIDTH // 2 - round((size / 48) * 80)
        y = HEIGTH // 2 - round(size / 48 * 80)
        screen.blit(text,(x,y))
        pygame.display.flip()





if __name__ == '__main__':
    main()



# debug------------------
# def check_rotate(self, blocks, board_blocks) -> None:
#     blocks_gibuy = [block.copy() for block in blocks]  # Ensure a deep copy
#     print("Original blocks before rotation:", [(block.x, block.y) for block in blocks_gibuy])
#
#     self.rotate(blocks)
#     print("Blocks after rotation:", [(block.x, block.y) for block in blocks])
#
#     for block in blocks:
#         x_index = int(block.x / self.size[0])
#         y_index = int(block.y / self.size[1])
#         print(f"Checking block at ({block.x}, {block.y}) -> indices ({x_index}, {y_index})")
#
#         # Check if block is within the height of the game
#         if block.y >= HEIGTH or block.y < 0:
#             print("Block out of vertical bounds, reverting.")
#             blocks[:] = blocks_gibuy
#             return
#
#         # Check if block is within the width of the game
#         if block.x >= WIDTH or block.x < 0:
#             print("Block out of horizontal bounds, reverting.")
#             blocks[:] = blocks_gibuy
#             return
#
#         # Check if indices are within the board bounds
#         if y_index >= len(board_blocks) or y_index < 0 or x_index >= len(board_blocks[0]) or x_index < 0:
#             print("Block index out of board bounds, reverting.")
#             blocks[:] = blocks_gibuy
#             return
#
#         # Check if the block collides with an existing block
#         if board_blocks[y_index][x_index]:
#             print("Collision detected at board position, reverting.")
#             blocks[:] = blocks_gibuy
#             return
#
#     print("Rotation successful. Blocks are valid after rotation.")
