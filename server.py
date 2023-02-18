import socket
from _thread import *
import pickle
# from game import Game
import pygame
import math
import json
# from arena_shooter import Hitbox

# class Hitbox():
#     def __init__(self, width, height, x, y, color, type, angle):
#         # super().__init__()
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color
#         self.rect = (x, y, width, height)
#         self.type = type
#         self.angle = angle
#
#     def draw(self, dis):
#         pygame.draw.rect(dis, self.color, self.rect)
#
#     def move(self):
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_w]:
#             self.y -= 5
#         if keys[pygame.K_s]:
#             self.y += 5
#         if keys[pygame.K_d]:
#             self.x += 5
#         if keys[pygame.K_a]:
#             self.x -= 5
#         self.update()
#
#     def update(self):
#         self.rect = (self.x, self.y, self.width, self.height)

class Hitbox(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type, angle):
        super().__init__()
        rectangle = pygame.Surface([width, height])
        rectangle.fill(color)
        self.image = rectangle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.count = 0
        all_gameplay_sprites.add(self)
        if type == 1:
            platform_list.add(self)
        if type == 2 or type == 3:
            self.angle = angle
            bullet_list.add(self)
        if type == 4:
            explosion_list.add(self)
        if type == 5:
            reload_box_list.add(self)

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color, type, menu_number):
        super().__init__()
        rectangle = pygame.Surface([width, height])
        rectangle.fill(color)
        self.image = rectangle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        if menu_number == 0:
            all_main_menu_sprites.add(self)
        if menu_number == 1:
            all_map_menu_sprites.add(self)
        if menu_number == 2:
            all_loudout_menu_sprites.add(self)
        if menu_number == 3:
            all_start_menu_sprites.add(self)



    # def __init__(self, width, height, x, y, color, type, angle):
    #     super().__init__()
    #     rectangle = pygame.Surface([width, height])
    #     rectangle.fill(color)
    #     self.image = rectangle
    #     self.rect = self.image.get_rect()
    #     self.rect.x = x
    #     self.rect.y = y
    #     self.type = type
    #     self.count = 0
        # all_gameplay_sprites.add(self)
        # if type == 1:
        #     platform_list.add(self)
        # if type == 2 or type == 3:
        #     self.angle = angle
        #     bullet_list.add(self)
        # if type == 4 or type == 5:
        #     explosion_list.add(self)

server = "192.168.1.77"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

# connected = set()
# games = {}
idCount = 0

dis_width = 1920
dis_height = 1080

clock = pygame.time.Clock()

black = (0, 0, 0)
black2 = (1, 1, 1)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 120, 0)
violet = (148, 0, 211)
orange = (255, 165, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)
gray3 = (240, 240, 240)

map_selection = 0
difficulty_selection = 0
gun_choice1 = 0
gun_name_list = ["Assault Rifle", "Sniper", "Flamethrower", "Sub Machine Gun", "Semi-Auto", "Rocket Launcher",
                 "Light Machine Gun", "Sword", "Shotgun", "full auto rocket launcher"]
gun_damage_list = [12, 100, 2, 10, 20, 100, 16, 30, 15, 100]
gun_fire_rate_list = [8, 150, 0, 4, 12, 300, 12, 5, 40, 0]
gun_reload_speed_list = [80, 150, 0, 70, 90, 300, 130, 0, 40, 0]
gun_range_list = [120, 400, 30, 50, 200, 400, 160, 8, 30, 400]
gun_ammo_list = [(30, 90), (1, 9), (650, 0), (45, 90), (15, 30), (1, 5), (100, 100), (99999, 0), (1, 24), (99999, 0)]
gun_reload_box_values = [20, 2, 150, 30, 10, 1, 50, 0, 4, 100]
# (start, reserve)
gun_fire_type = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
# Auto = 0  Semi = 1 Single Fire = 2
# gun_image_list = [basic_bullet_image, sniper_bullet_image, fireball_image, basic_bullet_image, basic_bullet_image,
#                   rocket_image, basic_bullet_image, pygame.Surface([0, 0]), energy_ball_image]

ground_y = 900
player_hitbox_height = 100
all_start_menu_sprites = pygame.sprite.Group()
all_main_menu_sprites = pygame.sprite.Group()
all_map_menu_sprites = pygame.sprite.Group()
all_loudout_menu_sprites = pygame.sprite.Group()
all_gameplay_sprites = pygame.sprite.Group()
reload_box_list = pygame.sprite.Group()
platform_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
pyramid_hitbox = pygame.sprite.Group()
bullet_position_list = [(0,0)]
bullet_position_list2 = [(0,0)]


for n in range(0, 4):
    menu_button = MenuButton(1100, 200, 410, 65 + 250*n, black, n, 0)
for n in range(0, 2):
    menu_button = MenuButton(1100, 400, 410, 90 + 500 *n, black, n, 3)

for n in range(0, 2):
    for i in range(0, 2):
        menu_button = MenuButton(192*4, 108*4, 150 + 852 * i, 80 + 488 * n, black, (i, n), 1)

for n in range(0, 3):
    for i in range(0, 3):
        menu_button = MenuButton(250*2, 150*2, 150 + 550 * i, 40 + 350 * n, black, (i, n), 2)

# all_gameplay_sprites = pygame.sprite.Group()
# platform_list = pygame.sprite.Group()
# bullet_list = pygame.sprite.Group()
# all_gameplay_sprites.empty()
# platform_list.empty()
# bullet_list.empty()
# pyramid_hitbox.empty()
explosion_position_list = []

player1_hitbox = Hitbox(50, player_hitbox_height, 100, 800, blue, 0, 0)
player2_hitbox = Hitbox(50, player_hitbox_height, dis_width - 150, 800, orange, 0, 0)


timer = 0
player1_shot_timer = 500
player2_shot_timer = 500
gun_choice2 = 0

player1_ammo = gun_ammo_list[gun_choice1][0]
player1_reserve_ammo = gun_ammo_list[gun_choice1][1]
player2_ammo = gun_ammo_list[gun_choice2][0]
player2_reserve_ammo = gun_ammo_list[gun_choice2][1]
player1_reload_speed = gun_reload_speed_list[gun_choice1]
player2_reload_speed = gun_reload_speed_list[gun_choice2]
current_player1_ammo = 0
current_player2_ammo = 0

heal_timer_1 = 0
heal_timer_2 = 0
prev_time = 0
player1_jumping = True
player2_jumping = True
player1_descending = False
player2_descending = False
player1_reload = False
player2_reload = False
player1_health = 100
player2_health = 100
player1_kill_count = 0
player2_kill_count = 0
angle1 = 0
angle2 = 0
P1_mouse_clicked = False
P2_mouse_clicked = False
shot_fired = False
P1_gun_state = 0
P2_gun_state = 0
dt1 = 0.01
dt2 = 0.01



player1_y_velocity = 0
player1_x_velocity = 0
player2_y_velocity = 0
player2_x_velocity = 0

player1_info_list = [player1_hitbox.rect.x, player1_hitbox.rect.y, player1_jumping, player1_descending,
                     player1_x_velocity, player1_y_velocity, 0, gun_choice1, angle1, player1_ammo, player1_reserve_ammo,
                     player1_reload, P1_gun_state, P1_mouse_clicked, dt1, player1_health, player1_kill_count, heal_timer_1, player1_shot_timer, [], 6, (0, 0)]
player2_info_list = [player2_hitbox.rect.x, player2_hitbox.rect.y, player2_jumping, player1_descending,
                     player2_x_velocity, player2_y_velocity, 1, gun_choice2, angle2, player2_ammo, player2_reserve_ammo,
                     player2_reload, P2_gun_state, P2_mouse_clicked, dt2, player2_health, player2_kill_count, heal_timer_2, player2_shot_timer, [], 6, (0, 0)]

players = [player1_info_list, player2_info_list]

player_hitboxes = [player1_hitbox, player2_hitbox]

player_spawn_coordinates = [(100, 800), (dis_width-150, 800)]

player_shot_timer = 0
player_reload_speed = 0


def threaded_client(conn, player):
    global idCount
    global player1_x_velocity
    global player2_x_velocity
    global player1_y_velocity
    global player2_y_velocity
    global player1_hitbox
    global player2_hitbox
    global player1_info_list
    global player2_info_list
    global player1_jumping
    global player2_jumping
    global players
    global player1_shot_timer
    global player2_shot_timer
    global player1_reload_speed
    global player2_reload_speed
    global player1_reload
    global player2_reload
    global heal_timer_1
    global heal_timer_2
    global player1_descending
    global player2_descending
    global player1_ammo
    global player2_ammo
    global player1_reserve_ammo
    global player2_reserve_ammo
    global player1_health
    global player2_health
    global player1_kill_count
    global player2_kill_count
    global gun_choice1
    global gun_choice2
    global map_selection
    global platform_list
    global bullet_list
    global bullet_position_list
    global all_gameplay_sprites
    global reload_box_list
    change = 0
    player_jumping = False

    reply = ""
    playing = False
    in_multiplayer_menu = True
    conn.send(pickle.dumps(players[player]))
    reload_box_list = pygame.sprite.Group()
    reload_box_sent_pos_list = []
    while in_multiplayer_menu:
        try:
            reload_box_timer = 1000
            data = pickle.loads(conn.recv(2048))

            players[player] = data

            if not data:
                break
            else:
                players[player][20] = 6
                print(players[player][20])
                print(f'not playing {player}')
                timer = 0
                # timer = 0
                # player1_shot_timer = 500
                # player2_shot_timer = 500
                # gun_choice2 = 2
                # players[1][7] = gun_choice2

                player1_ammo = gun_ammo_list[gun_choice1][0]
                player1_reserve_ammo = gun_ammo_list[gun_choice1][1]
                player2_ammo = gun_ammo_list[gun_choice2][0]
                player2_reserve_ammo = gun_ammo_list[gun_choice2][1]
                player1_reload_speed = gun_reload_speed_list[gun_choice1]
                player2_reload_speed = gun_reload_speed_list[gun_choice2]
                current_player1_ammo = 0
                current_player2_ammo = 0
                #
                heal_timer_1 = 0
                heal_timer_2 = 0
                # prev_time = 0
                player1_jumping = True
                player2_jumping = True
                player1_descending = False
                player2_descending = False
                player1_reload = False
                player2_reload = False
                player1_health = 100
                player2_health = 100
                player1_kill_count = 0
                player2_kill_count = 0
                # angle1 = 0
                # angle2 = 0
                # P1_mouse_clicked = False
                # P2_mouse_clicked = False
                # shot_fired = False
                # P1_gun_state = 0
                # P2_gun_state = 0
                dt1 = 0.01
                dt2 = 0.01

                player1_y_velocity = 0
                player1_x_velocity = 0
                player2_y_velocity = 0
                player2_x_velocity = 0
                #
                # player_spawn_coordinates = [(100, 800), (dis_width - 150, 800)]
                #
                # player_shot_timer = 0
                # player_reload_speed = 0
                player1_hitbox.rect.x = player_spawn_coordinates[0][0]
                player1_hitbox.rect.y = player_spawn_coordinates[0][1]
                player2_hitbox.rect.x = player_spawn_coordinates[1][0]
                player2_hitbox.rect.y = player_spawn_coordinates[1][1]

                for key in players[player][19]:
                    if key == 'g' and key == 'o' and key == 'd' and key == 'u' and key == 'n' and \
                            not key == 'h' and not key == 'j' and not key == 'k' and not key == 'f':
                        gun_choice1 = 9
                    if key == 'esc':
                        in_multiplayer_menu = False
                playing = False
                map_selection_menu = False
                loadout_menu = False
                all_gameplay_sprites = pygame.sprite.Group()
                platform_list = pygame.sprite.Group()
                bullet_list = pygame.sprite.Group()
                all_gameplay_sprites.empty()
                platform_list.empty()
                bullet_list.empty()
                pyramid_hitbox.empty()
                reload_box_list.empty()
                explosion_position_list = []
                if players[player][13]:
                    print('worked')
                    mouse_pos = players[player][21]
                    print(mouse_pos)
                    i = 0
                    for s in all_main_menu_sprites:
                        if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            if i == 0:
                                print('register')
                                playing = True
                            if i == 1 and player == 0:
                                map_selection_menu = True
                            if i == 2:
                                pass
                            if i == 3:
                                loadout_menu = True
                        i += 1

                while map_selection_menu:
                    try:
                        timer += 1
                        if timer > 1:
                            data = pickle.loads(conn.recv(2048))
                        # print(data)

                        players[player] = data

                        if not data:
                            print('no data')
                            break
                        else:
                            for key in players[player][19]:
                                if key == 'esc':
                                    map_selection_menu = False
                            players[player][20] = 7
                            i = 0
                            if players[player][13]:
                                for s in all_map_menu_sprites:
                                    if s.rect.collidepoint(players[player][21][0], players[player][21][1]):
                                        map_selection = i
                                    i += 1
                            conn.sendall(
                                pickle.dumps([players[player], reply, bullet_position_list, explosion_position_list,
                                              map_selection, reload_box_sent_pos_list]))
                    except:
                        break
                    clock.tick(60)
                reload_box_pos_list = [(dis_width / 2 - 50, 650), (dis_width / 2 - 50, 940), (dis_width / 2 - 50, 580),
                                       (dis_width / 2 - 50, 300)]
                if map_selection == 0:
                    ground_hitbox = Hitbox(dis_width, 1080 - ground_y, 0, ground_y, black, 0, 0)
                    cieling_hitbox = Hitbox(dis_width, 80, 0, -200, black, 0, 0)
                    left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
                    rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
                    platform1_hitbox = Hitbox(300, 20, 300, 600, gray, 1, 0)
                    platform2_hitbox = Hitbox(300, 20, dis_width - 600, 600, gray, 1, 0)
                    platform3_hitbox = Hitbox(300, 20, dis_width / 2 - 150, 400, gray, 1, 0)
                    platform4_hitbox = Hitbox(200, 20, 350, 300, gray, 1, 0)
                    platform5_hitbox = Hitbox(200, 20, dis_width - 550, 300, gray, 1, 0)
                    reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 650, gray, 5, 0)

                    for i in range(0, 20):
                        pyramid_hitbox_piece = Hitbox(700 - i * 20, 10, 610 + i * 10, 900 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                if map_selection == 1:
                    ground_hitbox = Hitbox(dis_width, 1080 - 1000, 0, 1000, black, 0, 0)
                    cieling_hitbox = Hitbox(dis_width, 80, 0, -200, black, 0, 0)
                    left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
                    rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)

                    reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 940, gray, 5, 0)
                    # platform1_hitbox = Hitbox(300, 20, 300, 600, gray, 1, 0)
                    # platform2_hitbox = Hitbox(300, 20, dis_width - 600, 600, gray, 1, 0)
                    # platform3_hitbox = Hitbox(300, 20, dis_width / 2 - 150, 400, gray, 1, 0)
                    # platform4_hitbox = Hitbox(200, 20, 350, 300, gray, 1, 0)
                    # platform5_hitbox = Hitbox(200, 20, dis_width - 550, 300, gray, 1, 0)

                    # for i in range(0, 38):
                    #     pyramid_hitbox_piece = Hitbox(760 - i * 20, 10, 590 + i * 10, 600 - i * 10, black, 0, 0)
                    #     pyramid_hitbox.add(pyramid_hitbox_piece)

                    for i in range(0, 16):
                        pyramid_hitbox_piece = Hitbox(320 - i * 20, 10, 590 + i * 10, 600 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(320 - i * 20, 10, dis_width - 320 - 590 + i * 10, 600 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                    for i in range(0, 14):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 320 - i * 10, 380 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 320 - i * 10, 380 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                    for i in range(0, 11):
                        pyramid_hitbox_piece = Hitbox(200 - i * 20, 10, dis_width / 2 - 100 + i * 10, 330 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                    for i in range(0, 22):
                        pyramid_hitbox_piece = Hitbox(760 - i * 20, 10, 190 + i * 10, 1000 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(760 - i * 20, 10, dis_width - 760 - 190 + i * 10, 1000 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        # pyramid_hitbox_piece = Hitbox(460 - i * 20, 10, 730 + i * 10, 600 - i * 10, white, 0, 0)
                        # pyramid_hitbox.add(pyramid_hitbox_piece)
                    platform1_hitbox = Hitbox(100, 20, 0, 700, gray, 1, 0)
                    platform2_hitbox = Hitbox(100, 20, 0, 400, gray, 1, 0)
                    platform3_hitbox = Hitbox(100, 20, dis_width - 100, 700, gray, 1, 0)
                    platform4_hitbox = Hitbox(100, 20, dis_width - 100, 400, gray, 1, 0)

                if map_selection == 2:

                    ground_hitbox = Hitbox(dis_width, 1080 - 1000, 0, 1000, black, 0, 0)
                    cieling_hitbox = Hitbox(dis_width, 80, 0, 0, black, 0, 0)
                    left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
                    rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
                    platform1_hitbox = Hitbox(100, 20, 0, 710, gray, 1, 0)
                    platform2_hitbox = Hitbox(100, 20, dis_width - 100, 710, gray, 1, 0)
                    reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 580, gray, 5, 0)
                    for i in range(0, 22):
                        pyramid_hitbox_piece = Hitbox(440 - i * 20, 10, dis_width / 2 - 220 + i * 10, 440 - i * 10, black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox((1 + i) * 20, 10, dis_width / 2 - 10 - i * 10, 850 - i * 10, black, 0,
                                                      0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250 + i * 15, 1000 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width - 330 - 250, 1000 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(220 - i * 10, 10, dis_width - 330 - 250 - 220 + i * 10, 1000 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(220 - i * 10, 10, 330 + 250, 1000 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250 + i * 15, 540 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width - 330 - 250, 540 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width - 330 - 250 + i * 15, 540 + i * 10, black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250, 540 + (i + 1) * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                        pyramid_hitbox_piece = Hitbox(630 - i * 15, 10, dis_width - 330 - 250 + i * 15, 80 + i * 10, black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(580 - i * 15, 10, 0, 80 + i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                if map_selection == 3:
                    ground_hitbox = Hitbox(dis_width, 1080 - ground_y, 0, ground_y + 200, black, 0, 0)
                    cieling_hitbox = Hitbox(dis_width, 80, 0, -200, black, 0, 0)
                    left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
                    rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
                    reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 300, gray, 5, 0)
                    for i in range(0, 16):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 340 - i * 10, 400 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 340 - i * 10, 400 - i * 10,
                                                      black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                    for i in range(0, 10):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 160 - i * 10, 1000 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 160 - i * 10, 1000 - i * 10,
                                                      black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                    for i in range(0, 16):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 500 - i * 10, 800 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 500 - i * 10, 800 - i * 10,
                                                      black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                    for i in range(0, 10):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width / 2 - 10 - i * 10, 900 - i * 10, black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                    for i in range(0, 7):
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 70 - i * 10, 600 - i * 10, black, 0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                        pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 80 - i * 10, 600 - i * 10,
                                                      black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)
                    for i in range(0, 30):
                        pyramid_hitbox_piece = Hitbox(20 + i * 16, 10, dis_width / 2 - 10 - i * 8, 650 - i * 10, black,
                                                      0, 0)
                        pyramid_hitbox.add(pyramid_hitbox_piece)

                while loadout_menu:
                    try:
                        timer += 1
                        if timer > 1:
                            data = pickle.loads(conn.recv(2048))
                        # print(data)

                        players[player] = data

                        if not data:
                            print('no data')
                            break
                        else:
                            for key in players[player][19]:
                                if key == 'esc':
                                    loadout_menu = False
                            players[player][20] = 8
                            if players[player][13]:
                                i = 0
                                for s in all_loudout_menu_sprites:
                                    if s.rect.collidepoint(players[player][21][0], players[player][21][1]):
                                        if player == 0:
                                            gun_choice1 = i
                                            players[0][7] = i
                                            player1_reload_speed = gun_reload_speed_list[gun_choice1]
                                            player1_ammo = gun_ammo_list[gun_choice1][0]
                                            player1_reserve_ammo = gun_ammo_list[gun_choice1][1]
                                        if player == 1:
                                            gun_choice2 = i
                                            players[1][7] = i
                                            player2_reload_speed = gun_reload_speed_list[gun_choice2]
                                            player2_ammo = gun_ammo_list[gun_choice2][0]
                                            player2_reserve_ammo = gun_ammo_list[gun_choice2][1]
                                    i += 1
                            conn.sendall(pickle.dumps([players[player], reply, bullet_position_list,
                                                       explosion_position_list, map_selection, reload_box_sent_pos_list]))
                    except:
                        break
                    clock.tick(60)

                if playing:
                    # players[player][20] = 5
                    players[player][13] = False
                    players[player][19].clear()
                    timer = 0

                while playing:
                    if map_selection == 0:
                        ground_hitbox = Hitbox(dis_width, 1080 - ground_y, 0, ground_y, black, 0, 0)
                    if map_selection == 1:
                        ground_hitbox = Hitbox(dis_width, 1080 - 1000, 0, 1000, black, 0, 0)
                    print(players[player][20])
                    print(f'playing {player}')
                    a_pressed = False
                    d_pressed = False
                    clock.tick(60)
                    timer += 1
                    # if timer > 1:
                    try:
                        if timer > 1:
                            data = pickle.loads(conn.recv(2048))
                        # print(data)

                        players[player] = data

                        if not data:
                            print('no data')
                            break
                        else:
                            players[player][20] = 5
                            if player == 1:
                                heal_timer_2 += 1
                                player2_shot_timer += 1
                                player_shot_timer = player2_shot_timer
                                player_reload_speed = player2_reload_speed
                                player_jumping = player2_jumping
                                player_descending = player2_descending
                                player_reload = player2_reload
                                player_x_velocity = player2_x_velocity
                                player_y_velocity = player2_y_velocity
                                player_ammo = player2_ammo
                                player_reserve_ammo = player2_reserve_ammo
                                # heal_timer_2 += 1
                                heal_timer = heal_timer_2
                                player_health = player2_health
                                players[player][0] = player2_hitbox.rect.x
                                players[player][1] = player2_hitbox.rect.y
                                players[player][16] = player2_kill_count
                            else:
                                heal_timer_1 += 1
                                player1_shot_timer += 1
                                player_shot_timer = player1_shot_timer
                                player_reload_speed = player1_reload_speed
                                player_jumping = player1_jumping
                                player_descending = player1_descending
                                player_reload = player1_reload
                                player_x_velocity = player1_x_velocity
                                player_y_velocity = player1_y_velocity
                                player_ammo = player1_ammo
                                player_reserve_ammo = player1_reserve_ammo
                                # heal_timer_1 += 1
                                heal_timer = heal_timer_1
                                player_health = player1_health
                                players[player][0] = player1_hitbox.rect.x
                                players[player][1] = player1_hitbox.rect.y
                                players[player][16] = player1_kill_count
                                reply = players[1]
                            # print(players[player][19])
                            if player == 1:
                                player2_descending = False
                            if player == 0:
                                player1_descending = False
                            player_descending = False

                            for key in players[player][19]:
                                if key == 'esc':
                                    playing = False
                                if key == 'r':
                                    if player == 1:
                                        player2_reload = True
                                    if player == 0:
                                        player1_reload = True
                                    player_reload = True
                                if key == 'w' and not player_jumping:
                                    # print('w pressed')
                                    if player == 1:
                                        player2_jumping = True
                                        player2_y_velocity = -21
                                    if player == 0:
                                        player1_jumping = True
                                        player1_y_velocity = -21
                                    player_y_velocity = -21
                                    player_jumping = True
                                    # players[player][2] = True
                                    # players[player][5] = -21
                                if key == 's':
                                    # player[3] = True
                                    if player == 1:
                                        player2_descending = True
                                    if player == 0:
                                        player1_descending = True
                                    player_descending = True
                                if key == 'd' and not player_jumping:
                                    d_pressed = True
                                    if player_x_velocity < 12:
                                        if player == 1:
                                            player2_x_velocity += 1.3
                                        if player == 0:
                                            player1_x_velocity += 1.3
                                        player_x_velocity += 1.3
                                if key == 'a' and not player_jumping:
                                    a_pressed = True
                                    if player_x_velocity > -12:
                                        if player == 1:
                                            player2_x_velocity -= 1.3
                                        if player == 0:
                                            player1_x_velocity -= 1.3
                                        player_x_velocity -= 1.3

                            if -1 < player_x_velocity < 1 and not d_pressed and not a_pressed:
                                if player == 1:
                                    player2_x_velocity = 0
                                if player == 0:
                                    player1_x_velocity = 0
                                player_x_velocity = 0
                            if player_x_velocity > 0 and not player_jumping:
                                print('friction -')
                                if player == 1:
                                    player2_x_velocity -= 1
                                if player == 0:
                                    player1_x_velocity -= 1
                                player_x_velocity -= 1
                            if player_x_velocity < 0 and not player_jumping:
                                print('friction +')
                                if player == 1:
                                    player2_x_velocity += 1
                                if player == 0:
                                    player1_x_velocity += 1
                                player_x_velocity += 1
                            ########################################################################################
                            if player_shot_timer > 5 and players[player][7] != 7:
                                players[player][12] = 0
                                if players[player][7] == 5 and player_ammo == 0:
                                    players[player][12] = 2
                            if players[player][7] == 7:
                                if player_shot_timer < 6:
                                    players[player][12] = player_shot_timer
                                if player_shot_timer > 6:
                                    players[player][12] -= 1
                                    if players[player][12] < 0:
                                        players[player][12] = 0
                            if player_reload:
                                players[player][13] = False
                                if player_reserve_ammo > 0:
                                    if player == 1:
                                        player2_reload_speed -= 1
                                    else:
                                        player1_reload_speed -= 1
                                    player_reload_speed -= 1
                                    if player_reload_speed <= 0:
                                        if player_reserve_ammo - gun_ammo_list[players[player][7]][0] + player_ammo > 0:
                                            players[player][10] -= gun_ammo_list[players[player][7]][0] - player_ammo
                                            players[player][9] = (gun_ammo_list[players[player][7]][0])
                                            if player == 1:
                                                player2_reserve_ammo -= gun_ammo_list[players[player][7]][0] - player_ammo
                                                player2_ammo = (gun_ammo_list[players[player][7]][0])
                                            else:
                                                player1_reserve_ammo -= gun_ammo_list[players[player][7]][0] - player_ammo
                                                player1_ammo = (gun_ammo_list[players[player][7]][0])
                                            player_reserve_ammo -= gun_ammo_list[players[player][7]][0] - player_ammo
                                            player_ammo = (gun_ammo_list[players[player][7]][0])
                                        else:
                                            players[player][9] += player_reserve_ammo
                                            players[player][10] -= player_reserve_ammo
                                            if player == 1:
                                                player2_ammo += player_reserve_ammo
                                                player2_reserve_ammo -= player_reserve_ammo
                                            else:
                                                player1_ammo += player_reserve_ammo
                                                player1_reserve_ammo -= player_reserve_ammo
                                            player_ammo += player_reserve_ammo
                                            player_reserve_ammo -= player_reserve_ammo
                                        if player == 1:
                                            player2_reload_speed = gun_reload_speed_list[players[player][7]]
                                            player2_reload = False
                                        else:
                                            player1_reload_speed = gun_reload_speed_list[players[player][7]]
                                            player1_reload = False
                                        player_reload = False
                                        players[player][11] = False
                                else:
                                    if player == 1:
                                        player2_reload = False
                                    else:
                                        player1_reload = False
                                    player_reload = False
                                    players[player][11] = False

                            shot_fired = False
                            if player_shot_timer > gun_fire_rate_list[players[player][7]] and player_ammo > 0 and not \
                                    player_reload and timer > 10:
                                if players[player][13] and gun_fire_type[players[player][7]] == 0:
                                    shot_fired = True
                                elif gun_fire_type[players[player][7]] == 1 and players[player][13]:
                                    shot_fired = True
                                    players[player][13] = False
                                if shot_fired:
                                    players[player][12] = 1
                                    if players[player][7] == 7 or players[player][7] == 8:
                                        for i in range(0, 5):
                                            bullet_hitbox = Hitbox(10, 10, players[player][0]+25, players[player][1]+50,
                                                                   red, player+2,
                                                                   players[player][8] + i * (math.pi / (9 * 5)))
                                            bullet_hitbox = Hitbox(10, 10, player_hitboxes[player].rect.centerx,
                                                                   player_hitboxes[player].rect.centery, red, player+2,
                                                                   players[player][8] - i * (math.pi / (9 * 5)))
                                    if player == 1:
                                        player2_shot_timer = 0
                                        players[1][18] = 0
                                        player2_ammo -= 1
                                    else:
                                        player1_shot_timer = 0
                                        players[0][18] = 0
                                        player1_ammo -= 1
                                    players[player][9] -= 1
                                    bullet_hitbox = Hitbox(10, 10, player_hitboxes[player].rect.centerx,
                                                           player_hitboxes[player].rect.centery, red, player+2,
                                                           players[player][8])
                                    shot_fired = False

                            for bullet in bullet_list:
                                gun_selection = players[player][7]
                                dt = players[player][14]
                                if bullet.count > gun_range_list[gun_choice1] and bullet.type == 2:
                                    bullet.kill()
                                if bullet.count > gun_range_list[gun_choice2] and bullet.type == 3:
                                    bullet.kill()
                                bullet.count += 1
                                if gun_selection == 5:
                                    bullet.rect.y -= (500 * math.sin(bullet.angle) / 20 * dt * 70) / 2.2
                                    bullet.rect.x += (500 * math.cos(bullet.angle) / 20 * dt * 70) / 2.2
                                else:
                                    bullet.rect.y -= (500 * math.sin(bullet.angle) / 20 * dt * 70) / 2
                                    bullet.rect.x += (500 * math.cos(bullet.angle) / 20 * dt * 70) / 2
                                for p in platform_list:
                                    if bullet.rect.colliderect(p):

                                        if gun_selection == 5 or gun_selection == 9:
                                            explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125,
                                                                      bullet.rect.centery - 125, \
                                                                      red, 4, 0)
                                        bullet.kill()
                                for pp in pyramid_hitbox:
                                    if bullet.rect.colliderect(pp):

                                        if gun_selection == 5 or gun_selection == 9:
                                            explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125,
                                                                      bullet.rect.centery - 125,
                                                                      red, 4, 0)
                                        bullet.kill()
                                if bullet.rect.colliderect(ground_hitbox):
                                    if gun_selection == 5 or gun_selection == 9:
                                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                                  red, 4, 0)
                                    bullet.kill()
                                if bullet.rect.colliderect(cieling_hitbox):
                                    if gun_selection == 5 or gun_selection == 9:
                                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                                  red, 4, 0)
                                    bullet.kill()
                                if bullet.rect.colliderect(player2_hitbox) and bullet.type == 2:
                                    print('hit1')
                                    player2_health -= gun_damage_list[gun_choice1]
                                    print('hit2')
                                    players[1][15] -= gun_damage_list[gun_choice1]
                                    print('hit3')
                                    if gun_choice1 == 5 or gun_selection == 9:
                                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                                  red, 4, 0)
                                    print('hit4')
                                    bullet.kill()
                                    print('hit5')
                                    heal_timer_2 = 0
                                    print('hit6')
                                if bullet.rect.colliderect(player1_hitbox) and bullet.type == 3:
                                    print(f'hit {player}')
                                    bullet.kill()
                                    player1_health -= gun_damage_list[gun_choice2]
                                    players[0][15] -= gun_damage_list[gun_choice2]
                                    if gun_choice2 == 5 or gun_selection == 9:
                                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                                  red, 4, 0)
                                    heal_timer_1 = 0

                            if player_health > 100:
                                if player == 1:
                                    player2_health = 100
                                else:
                                    player1_health = 100
                                players[player][15] = 100
                                player_health = 100
                            # print(players[player][17])
                            if player_health < 100 and heal_timer > 120:
                                heal_timer = 90
                                print('tick')
                                players[player][15] += 10
                                if player == 0:
                                    heal_timer_1 = 90
                                    player1_health += 10
                                elif player == 1:
                                    heal_timer_2 = 90
                                    player2_health += 10
                            if player_health <= 0:
                                player_hitboxes[player].rect.x = player_spawn_coordinates[player][0]
                                player_hitboxes[player].rect.y = player_spawn_coordinates[player][1]
                                players[player][0] = player_spawn_coordinates[player][0]
                                players[player][1] = player_spawn_coordinates[player][1]
                                players[player][15] = 100
                                if player == 1:
                                    player2_ammo += gun_reload_box_values[players[player][7]]
                                    player2_health = 100
                                    player1_kill_count += 1
                                else:
                                    player1_ammo += gun_reload_box_values[players[player][7]]
                                    player1_health = 100
                                    player2_kill_count += 1
                                players[player][9] += gun_reload_box_values[players[player][7]]

                            bullet_position_list.clear()
                            for bullet in bullet_list:
                                gun_selection = 0
                                if bullet.type == 2:
                                    gun_selection = players[0][7]
                                elif bullet.type == 3:
                                    gun_selection = players[1][7]
                                if bullet.angle < 0:
                                    bullet.angle = bullet.angle + 2 * math.pi
                                if gun_selection == 2 and bullet.count > gun_range_list[gun_selection]:
                                    bullet.angle = bullet.angle + 2 * math.pi
                                if gun_selection == 2 and bullet.count < 6:
                                    bullet.angle = bullet.angle + 4 * math.pi
                                bullet_position_list.append((bullet.rect.x, bullet.rect.y, bullet.angle, bullet.type))
                                if gun_selection == 2 and bullet.count < 6:
                                    bullet.angle = bullet.angle - 4 * math.pi
                            #######################################################################################

                            for explosion in explosion_list:
                                explosion_position_list.append([explosion.rect.x, explosion.rect.y, explosion.count])
                                explosion.count += 1
                                if explosion.rect.colliderect(player2_hitbox):
                                    players[1][15] -= 100
                                    heal_timer_1 = 0
                                if explosion.rect.colliderect(player1_hitbox):
                                    players[0][15] -= 100
                                    heal_timer_2 = 0
                                if explosion.count > 0:
                                    explosion.kill()
                            for explosion_pos in explosion_position_list:
                                explosion_pos[2] += 1
                                if explosion_pos[2] > 20:
                                    explosion_position_list.remove(explosion_pos)

                            gravity_strength = 40 * round(players[player][14], 4)
                            if timer > 1:
                                # print(player_x_velocity)
                                # player[5] += gravity_strength
                                if player == 1:
                                    player2_y_velocity += gravity_strength
                                if player == 0:
                                    player1_y_velocity += gravity_strength
                                player_y_velocity += gravity_strength
                                if 0 < player_y_velocity < 1:
                                    player_y_velocity += 1
                                # print(player_y_velocity)
                                # player[1] += player_y_velocity
                                # player[0] += player_x_velocity * players[player][14] * 70
                                player_hitboxes[player].rect.x += player_x_velocity * players[player][14] * 70
                                player_hitboxes[player].rect.y += player_y_velocity

                            if player1_y_velocity > 5:
                                player1_jumping = True
                            if player2_y_velocity > 5:
                                player2_jumping = True

                            if reload_box_timer == 720:
                                a_reload_box_hitbox = Hitbox(100, 60, reload_box_pos_list[map_selection][0],
                                                             reload_box_pos_list[map_selection][1], gray, 5, 0)

                            for reload_box_hitbox in reload_box_list:
                                if player1_hitbox.rect.colliderect(reload_box_hitbox.rect):
                                    player1_reserve_ammo += gun_reload_box_values[gun_choice1]
                                    reload_box_hitbox.kill()
                                    reload_box_timer = 0
                                if player2_hitbox.rect.colliderect(reload_box_hitbox.rect):
                                    player2_reserve_ammo += gun_reload_box_values[gun_choice2]
                                    reload_box_hitbox.kill()
                                    reload_box_timer = 0
                            reload_box_timer += 1

                            reload_box_sent_pos_list.clear()
                            for box in reload_box_list:
                                reload_box_sent_pos_list.append((box.rect.x, box.rect.y))

                            if player_hitboxes[player].rect.colliderect(left_border_hitbox.rect):
                                if player == 1:
                                    player2_x_velocity = 0
                                if player == 0:
                                    player1_x_velocity = 0
                                player_x_velocity = 0
                                players[player][4] = 0
                                player_hitboxes[player].rect.x = left_border_hitbox.rect.right
                                players[player][0] = player_hitboxes[player].rect.x
                            if player_hitboxes[player].rect.colliderect(rightborder_hitbox):
                                if player == 1:
                                    player2_x_velocity = 0
                                if player == 0:
                                    player1_x_velocity = 0
                                players[player][4] = 0
                                player_x_velocity = 0
                                player_hitboxes[player].rect.x = rightborder_hitbox.rect.left - 50
                                players[player][0] = player_hitboxes[player].rect.x

                            if player_hitboxes[player].rect.colliderect(ground_hitbox):
                                # print('ground_colliude')
                                if player == 1:
                                    player2_y_velocity = 0
                                    player2_jumping = False
                                if player == 0:
                                    player1_y_velocity = 0
                                    player1_jumping = False
                                players[player][5] = 0
                                player_y_velocity = 0
                                # player1_hitbox.rect.y = 900 - player_hitbox_height
                                player_hitboxes[player].rect.y = ground_hitbox.rect.top - player_hitbox_height
                                players[player][1] = ground_hitbox.rect.top - player_hitbox_height
                                players[player][2] = False
                            if player_hitboxes[player].rect.colliderect(cieling_hitbox):
                                if player_y_velocity < 0:
                                    if player == 1:
                                        player2_y_velocity = player_y_velocity * -0.25
                                    if player == 0:
                                        player1_y_velocity = player_y_velocity * -0.25
                                    players[player][5] = player_y_velocity * -0.25
                                    player_y_velocity = player_y_velocity * -0.25
                            for platform in platform_list:
                                if player_hitboxes[player].rect.colliderect(platform) and not player_descending:
                                    if platform.rect.top - 30 < player_hitboxes[player].rect.bottom < platform.rect.top + 30:
                                        if player_y_velocity > 0:
                                            if player == 1:
                                                player2_y_velocity = 0
                                                player2_jumping = False
                                            if player == 0:
                                                player1_y_velocity = 0
                                                player1_jumping = False
                                            player_y_velocity = 0
                                            players[player][5] = 0
                                            player_hitboxes[player].rect.y = platform.rect.top - player_hitbox_height
                                            players[player][1] = player_hitboxes[player].rect.y
                                            players[player][2] = False
                            for pyramid_piece in pyramid_hitbox:
                                # if player1_hitbox.rect.colliderect(pyramid_piece):
                                if player_hitboxes[player].rect.colliderect(pyramid_piece):
                                    if pyramid_piece.rect.bottom - 30 < player_hitboxes[player].rect.top < pyramid_piece.rect.bottom + 30:
                                        if player_y_velocity < 0:
                                            if player == 1:
                                                player2_y_velocity = player_y_velocity * -0.25
                                            if player == 0:
                                                player1_y_velocity = player_y_velocity * -0.25
                                            players[player][5] = player_y_velocity * -0.25
                                            player_y_velocity = player_y_velocity * -0.25
                                    if pyramid_piece.rect.top - 30 < player_hitboxes[player].rect.bottom < pyramid_piece.rect.top + 30:
                                        if player_y_velocity >= 0:
                                            if player == 1:
                                                player2_y_velocity = 0
                                                player2_jumping = False
                                            if player == 0:
                                                player1_jumping = False
                                                player1_y_velocity = 0
                                            player_y_velocity = 0
                                            players[player][5] = 0
                                            player_hitboxes[player].rect.y = pyramid_piece.rect.top - player_hitbox_height
                                            players[player][1] = player_hitboxes[player].rect.y
                                            players[player][2] = False
                                # players[player][1] = player_hitboxes[player].rect.y
                                # players[player][0] = player_hitboxes[player].rect.x
                            # if -1 < players[player][4] < 1:
                            #     players[player][4] = 0
                            # if players[player][4] > 1 and not player1_jumping:
                            #     players[player][4] -= 1
                            # if players[player][4] < 1 and not player1_jumping:
                            #     players[player][4] += 1
                            # print(players[player])
                            # reply = players[player]
                            # print([players[player][5]])
                            # print(players[player][4])
                            # for val in range(0, 21):
                            #     if player == 0:
                            #         players[player][val] = player1_info_list[val]
                            #     if player == 1:
                            #         players[player][val] = player2_info_list[val]
                            # players[0][0] = player1_hitbox.rect.x
                            # players[1][0] = player2_hitbox.rect.x
                            # players[0][1] = player1_hitbox.rect.y
                            # players[1][1] = player2_hitbox.rect.y
                            players[0][2] = player1_jumping
                            players[1][2] = player2_jumping
                            players[0][3] = player1_descending
                            players[1][3] = player2_descending
                            players[0][4] = player1_x_velocity
                            players[1][4] = player2_x_velocity
                            players[0][5] = player1_y_velocity
                            players[1][5] = player2_y_velocity
                            players[0][9] = player1_ammo
                            players[1][9] = player2_ammo
                            players[0][10] = player1_reserve_ammo
                            players[1][10] = player2_reserve_ammo
                            players[0][15] = player1_health
                            players[1][15] = player2_health

                            if player == 1:
                                reply = players[0]
                            if player == 0:
                                reply = players[1]
                            # print(reply[15])
                            conn.sendall(pickle.dumps([players[player], reply, bullet_position_list, explosion_position_list, map_selection, reload_box_sent_pos_list]))
                    except Exception as e:
                        print('broke')
                        print(e)
                        break
                if player == 1:
                    reply = players[0]
                if player == 0:
                    reply = players[1]
                conn.sendall(pickle.dumps([players[player], reply, bullet_position_list, explosion_position_list,
                                           map_selection, reload_box_sent_pos_list]))
        except:
            break

    print("Lost connection")
    # try:
    #     del games[gameId]
    #     print("Closing Game", gameId)
    # except:
    #     pass
    # idCount -= 1
    conn.close()

idCount = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    if not idCount > 1:
        start_new_thread(threaded_client, (conn, idCount))
    idCount += 1