import pygame
import random
import time
import math

pygame.init()

player_image = pygame.image.load('player_image_2.png')
reload_box_image = pygame.image.load('reload_box.png')
platform_image_1 = pygame.image.load('platform_1_1.png')
platform_image_2 = pygame.image.load('platform_2.png')
center_base_image = pygame.image.load('center_base.png')
ground_piece_1_image = pygame.image.load('ground_piece_1_1.png')
ground_piece_2_image = pygame.transform.flip(ground_piece_1_image, True, False)
ground_piece_3_image = pygame.image.load('ground_piece_3.png')
floating_platform_1_image = pygame.transform.scale(pygame.image.load('floating_platform_1.png'), (220, 110))
floating_platform_2_image = pygame.image.load('floating_platform_2.png')
floating_platform_3_image = pygame.image.load('floating_platform_3.png')
floating_platform_4_image = pygame.image.load('floating_platform_4.png')
city_ground_main_image = pygame.image.load('city_ground_main.png')
city_ground_piece_1_image = pygame.image.load('city_ground_piece_1j.png')
city_ground_piece_2_image = pygame.transform.flip(city_ground_piece_1_image, True, False)
city_structure_piece_1_image = pygame.image.load('city_structure_piece_1b.png')
city_structure_piece_2_image = pygame.transform.flip(city_structure_piece_1_image, True, False)
city_structure_piece_3_image = pygame.image.load('city_structure_piece_2.png')
city_structure_piece_4_image = pygame.transform.flip(city_structure_piece_3_image, False, True)
city_cieling_piece_1_image = pygame.image.load('city_cieling_piece_1.png')
city_cieling_piece_2_image = pygame.transform.flip(city_cieling_piece_1_image, True, False)
city_cieling_piece_3_image = pygame.image.load('city_cieling_piece_2.png')
city_platform_image = pygame.image.load('city_platform.png')

basic_bullet_image = pygame.image.load('basic_bullet_sprite.png')
sniper_bullet_image = pygame.image.load('sniper_bullet_sprite.png')
rocket_bullet_image = pygame.image.load('altsniper_bullet_sprite.png')
sword_attack_image = pygame.image.load('sword_slash_effect.png')
rocket_image = pygame.image.load('rocket.png')
explosion_image = pygame.image.load('explosion_image.png')
energy_ball_image = pygame.image.load("energy_ball_sprite.png")
fireball_image = pygame.image.load('fire5.png')
end_fireball_image = pygame.image.load('fire6.png')
assault_rifle_image = pygame.image.load("pixil-frame-0 (42).png")
assault_rifle_firing_image = pygame.image.load("Assault_Rifle_firing.png")
best_gun_image = pygame.image.load("pixil-frame-0 (47).png")
assault_rifle_images = [assault_rifle_image, assault_rifle_firing_image]
flamethrower_image = pygame.image.load("flamethrower2.png")
sniper_rifle_image = pygame.image.load("sniper_rifle.png")
sniper_rifle_firing_image = pygame.image.load("sniper_rifle_firing.png")
sniper_rifle_images = [sniper_rifle_image, sniper_rifle_firing_image]
smg_image = pygame.image.load("smg.png")
smg_firing_image = pygame.image.load("smg_firing.png")
smg_images = [smg_image, smg_firing_image]
semi_auto_image = pygame.image.load("semi_auto.png")
semi_auto_firing_image = pygame.image.load("semi_auto_firing.png")
semi_auto_images = [semi_auto_image, semi_auto_firing_image]
lmg_image = pygame.image.load("lmg.png")
lmg_firing_image = pygame.image.load("lmg_firing.png")
lmg_images = [lmg_image, lmg_firing_image]
rpg_image = pygame.image.load("rpg.png")
rpg_firing_image = pygame.image.load("rpg_firing.png")
rpg_empty_image = pygame.image.load("rpg_empty.png")
rpg_images = [rpg_image, rpg_firing_image, rpg_empty_image]
sword_image = pygame.image.load("sword2.png")
sword_attack_image1 = pygame.image.load("sword2_attack_1.png")
sword_attack_image2 = pygame.image.load("sword2_attack_2.png")
sword_attack_image3 = pygame.image.load("sword2_attack_3.png")
sword_attack_image4 = pygame.image.load("sword2_attack_4.png")
sword_attack_image5 = pygame.image.load("sword2_attack_5.png")
sword_attack_image6 = pygame.image.load("sword2_attack_6.png")
sword_images = [sword_image, sword_attack_image1, sword_attack_image2, sword_attack_image3, sword_attack_image4,
                sword_attack_image5, sword_attack_image6]
shotgun_image = pygame.image.load("shotgun.png")
shotgun_firing_image = pygame.image.load("shotgun_firing.png")
shotgun_images = [shotgun_image, shotgun_firing_image]

# fireball_image = pygame.transform.scale(fireball_image, [13, 13])

# Define colors and fonts
black = (0, 0, 0)
black2 = (1, 1, 1)
white = (255, 255, 255)
white2 = (50, 50, 155)
# white2 = (100, 100, 205)
# white2 = (205, 100, 0)
# white2 = (150, 150, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 120, 0)
violet = (148, 0, 211)
# orange = (255, 165, 0)
orange = (205, 115, 0)
yellow = (255, 255, 0)
gray = (50, 50, 50)
gray2 = (100, 100, 100)
gray3 = (240, 240, 240)
gray4 = (20, 20, 20)
purple = (38, 0, 65)

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)

# Create the window
dis_width = 1920
dis_height = 1080

dis = pygame.display.set_mode((dis_width, dis_height), pygame.FULLSCREEN)
pygame.display.set_caption('Arena Shooter')


clock = pygame.time.Clock()

sky_background = pygame.image.load('cool_sky_background.jpg')
cool_landscape_1 = pygame.image.load('wallpapersden.com_artistic-orange-landscape_1920x1080.jpg')
pyramid_background_image = pygame.image.load('background_image_option.jpg')
cave_background_image = pygame.image.load('test_background.jpg')
map_1_background_image = pygame.image.load('map_1_background.png')
map_2_background_image = pygame.image.load('map_2_background.png')
map_3_background_image = pygame.image.load('map_3_background.png')
map_4_background_image = pygame.image.load('map_4_background.png')

background_images = [map_1_background_image, map_2_background_image, map_3_background_image, map_4_background_image]
pyramid_piece_bottom_image_1 = pygame.image.load('pyramid_bottom_piece_1_f.png')
pyramid_piece_bottom_image_2 = pygame.image.load('pyramid_bottom_piece_2_f.png')
pyramid_piece_mid_image = pygame.image.load('pyramid_piece_mid.png')
pyramid_piece_top_image = pygame.image.load('pyramid_top_piece_f.png')
pyramid_piece_1_image = pygame.image.load('pyramid_piece_111.png')
pyramid_piece_2_image = pygame.image.load('pyramid_piece_222.png')
pyramid_platform_image = pygame.image.load('pyramid_platform_4.png')
pyramid_upper_platform_image = pygame.image.load('pyramid_upper_platform_f.png')
pyramid_ground_image = pygame.image.load('pyramid_ground.png')
fix_image = pygame.image.load('fix_piece.png')
difficulty_menu_button_main_image = pygame.image.load('difficulty_button_main.png')
difficulty_menu_button_side_image = pygame.image.load('difficulty_button_side.png')
loadout_menu_button_main_image = pygame.image.load('loadout_button_main.png')
loadout_menu_button_side_image = pygame.image.load('loadout_button_side.png')
map_menu_button_main_image = pygame.image.load('map_button_main.png')
map_menu_button_side_image = pygame.image.load('map_button_side.png')
play_menu_button_main_image = pygame.image.load('play_button_main.png')
play_menu_button_side_image = pygame.image.load('play_button_side.png')

main_menu_image = pygame.image.load('main_menu_image.png')
map_menu_image = pygame.image.load('map_menu_image.png')
gun_menu_image = pygame.image.load('gun_menu_image.png')


def dis_update(type):
    if type == 0:
        angle = angle1
        player_hitbox = player1_hitbox
        gun_state = P1_gun_state
        gun_choice = gun_choice1
        # dis.fill(gray3)
        dis.blit(background_images[map_selection], (0, 0))
        # pygame.draw.rect(dis, gray4, [257, 0, 320, dis_width])
        # pygame.draw.rect(dis, gray4, [1345, 0, 320, dis_width])
        # pygame.draw.rect(dis, gray4, [740, 0, 440, dis_width])
        # pygame.draw.line(dis, black, [257, 0], (257, dis_height), 15)
        # pygame.draw.line(dis, black, [572, 0], (572, dis_height), 15)
        # pygame.draw.line(dis, black, [dis_width - 573, 0], (dis_width - 573, dis_height), 15)
        # pygame.draw.line(dis, black, [dis_width - 258, 0], (dis_width - 258, dis_height), 15)
        # pygame.draw.line(dis, black, [dis_width / 2 - 1, 0], (dis_width / 2 - 1, dis_height), 20)
        # pygame.draw.line(dis, black, [dis_width / 2 - 223, 0], (dis_width / 2 - 223, dis_height), 15)
        # pygame.draw.line(dis, black, [dis_width / 2 + 222, 0], (dis_width / 2 + 222, dis_height), 15)
        # #
        # pygame.draw.line(dis, white2, [257, 0], (257, dis_height), 3)
        # pygame.draw.line(dis, white2, [572, 0], (572, dis_height), 3)
        # pygame.draw.line(dis, white2, [dis_width - 573, 80], (dis_width - 573, dis_height), 3)
        # pygame.draw.line(dis, white2, [dis_width - 258, 0], (dis_width - 258, dis_height), 3)
        # pygame.draw.line(dis, white2, [dis_width / 2-1, 0], (dis_width / 2-1, dis_height), 4)
        # pygame.draw.line(dis, white2, [dis_width / 2 - 223, 0], (dis_width / 2 - 223, dis_height), 3)
        # pygame.draw.line(dis, white2, [dis_width / 2 + 222, 0], (dis_width / 2 + 222, dis_height), 3)

        # pygame.draw.line(dis, orange, [0, 1000], (dis_width, 1000), 10)

        # all_gameplay_sprites.draw(dis)
        # pygame.draw.rect(dis, black, [250, 0, 330, 69])
        # pygame.draw.rect(dis, black, [1350, 0, 330, 69])
        # dis.blit(city_ground_main_image, (0, 1000))
        # dis.blit(city_ground_main_image, (700, 1000))
        # dis.blit(city_ground_main_image, (1400, 1000))
        # dis.blit(city_ground_piece_1_image, (225, 780))
        # dis.blit(city_ground_piece_2_image, (dis_width - 825, 780))
        # dis.blit(city_structure_piece_1_image, (dis_width - 580, 315))
        # dis.blit(city_structure_piece_2_image, (250, 320))
        # dis.blit(city_structure_piece_3_image, (dis_width/2 - 230, 220))
        # dis.blit(city_structure_piece_4_image, (dis_width/2 - 230, 640))
        # dis.blit(city_cieling_piece_2_image, (dis_width - 580, 69))
        # dis.blit(city_cieling_piece_1_image, (250, 69))
        # dis.blit(city_cieling_piece_3_image, (0, -101))
        # dis.blit(city_cieling_piece_3_image, (dis_width-250, -101))
        # dis.blit(city_cieling_piece_3_image, (580, -311))
        # dis.blit(city_cieling_piece_3_image, (dis_width - 250 - 580, -311))
        # dis.blit(city_cieling_piece_3_image, (830, -311))
        # dis.blit(city_cieling_piece_3_image, (dis_width - 250 - 830, -311))
        # dis.blit(city_platform_image, (0, 710))
        # dis.blit(city_platform_image, (dis_width - 100, 710))

        # pygame.draw.line(dis, orange, [1340, 550], (1340, 540), 1)
        # pygame.draw.line(dis, orange, [1340, 540], (1770, 540), 1)


        # if map_selection == 1:
        #     # dis.blit(pyramid_piece_1_image, (260, 230))
        #     # dis.blit(pyramid_piece_2_image, (dis_width/2, 230))
        #     # dis.blit(pyramid_piece_1_image, (190, 300))
        #     # dis.blit(pyramid_piece_2_image, (dis_width / 2+70, 300))
        #     # dis.blit(pyramid_piece_2_image, (800, 400))\
        #     dis.blit(pyramid_piece_bottom_image_1, (190, 790))
        #     dis.blit(pyramid_piece_bottom_image_1, (970, 790))
        #     dis.blit(pyramid_piece_bottom_image_2, (540, 790))
        #     dis.blit(pyramid_piece_bottom_image_2, (1320, 790))
        #     dis.blit(pyramid_piece_mid_image, (580, 440))
        #     dis.blit(pyramid_piece_mid_image, (1000, 440))
        #     dis.blit(pyramid_piece_top_image, (dis_width/2-110, 230))
        #     dis.blit(pyramid_upper_platform_image, (180, 250))
        #     dis.blit(pyramid_upper_platform_image, (1450, 250))
        #     dis.blit(pyramid_ground_image, (0, 1000))
        #     dis.blit(pyramid_ground_image, (700, 1000))
        #     dis.blit(pyramid_ground_image, (1400, 1000))
        #     dis.blit(fix_image, (191, 1000))
        #     dis.blit(fix_image, (971, 1000))
        #     dis.blit(fix_image, (190 + 760 - 8, 1000))
        #     dis.blit(fix_image, (970 + 760 - 8, 1000))
        #     dis.blit(fix_image, (190, 1001))
        #     dis.blit(fix_image, (970, 1001))
        #     dis.blit(fix_image, (190 + 760 - 7, 1001))
        #     dis.blit(fix_image, (970 + 760 - 7, 1001))
        #     for platform in platform_list:
        #         dis.blit(pyramid_platform_image, (platform.rect.x, platform.rect.y))
        #
        #
        # platform_list.draw(dis)
        # mouse_pointer = (50*math.cos(angle)+player1_hitbox.rect.centerx, 50*math.sin(angle)*-1+player1_hitbox.rect.centery)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, mouse_pointer, 3)
        # pygame.draw.line(dis, yellow, (dis_width / 2, 0), (dis_width / 2, dis_height), 3)
        # pygame.draw.line(dis, yellow, (dis_width/2, 230), (dis_width/2, 340), 3)
        # pygame.draw.line(dis, yellow, (dis_width/2-110, 340), (dis_width/2+110, 340), 3)
        # pygame.draw.line(dis, yellow, (550, 790), (550, 1000), 3)
        # pygame.draw.line(dis, yellow, (400, 790), (740, 790), 3)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (player1_hitbox.rect.centerx, mouse_pos[1]), 2)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (mouse_pos[0], player1_hitbox.rect.centery), 2)

        player1_ammo_message = font3.render(f"{player1_ammo}/{player1_reserve_ammo}", False, gray3)
        dis.blit(player1_ammo_message, (1000, 10))
        pygame.draw.rect(dis, red, [player2_hitbox.rect.centerx-50, player2_hitbox.rect.y-20, player2_health, 5])
        pygame.draw.rect(dis, red, [player1_hitbox.rect.centerx - 50, player1_hitbox.rect.y - 20, player1_health, 5])
        player1_kill_count_message = font3.render(f"Kills {player1_kill_count}", False, gray3)
        dis.blit(player1_kill_count_message, (10, 10))
        player2_kill_count_message = font3.render(f"Deaths {player2_kill_count}", False, gray3)
        dis.blit(player2_kill_count_message, (300, 10))

        # if map_selection == 0:
        #     for platform in platform_list:
        #         if platform.rect.width == 300:
        #             dis.blit(platform_image_1, (platform.rect.x, platform.rect.y))
        #         if platform.rect.width == 200:
        #             dis.blit(platform_image_2, (platform.rect.x, platform.rect.y))
        #     dis.blit(center_base_image, (610, 710))
        #     dis.blit(ground_piece_1_image, (0, 900))
        #     dis.blit(ground_piece_2_image, (1291, 900))
        #     dis.blit(ground_piece_3_image, (629, 900))
        # if map_selection == 3:
        #     dis.blit(floating_platform_1_image, (60, 910))
        #     dis.blit(floating_platform_1_image, (dis_width - 270, 910))
        #     dis.blit(floating_platform_1_image, (dis_width / 2 - 110, 810))
        #     dis.blit(floating_platform_2_image, (0, 540))
        #     dis.blit(floating_platform_2_image, (dis_width - 160, 540))
        #     dis.blit(floating_platform_3_image, (340, 650))
        #     dis.blit(floating_platform_3_image, (dis_width - 670, 650))
        #     dis.blit(floating_platform_3_image, (180, 250))
        #     dis.blit(floating_platform_3_image, (dis_width - 510, 250))
        #     dis.blit(floating_platform_4_image, (dis_width/2-250, 360))

        for reload_box in reload_box_list:
            dis.blit(reload_box_image, (reload_box.rect.x, reload_box.rect.y))

        for bullet_i in bullet_position_list:
            gun_decision = 0
            if bullet_i[3] == 2:
                gun_decision = gun_choice
            if bullet_i[3] == 3:
                gun_decision = gun_choice2
            bullet_img = pygame.transform.rotate(ammo_image_list[gun_decision], math.degrees(bullet_i[2]))
            if gun_decision == 2:
                if 4*math.pi > bullet_i[2] > 2*math.pi:
                    bullet_img = pygame.transform.rotate(end_fireball_image, math.degrees(bullet_i[2]))
                if 4*math.pi < bullet_i[2]:
                    bullet_img = pygame.transform.rotate(pygame.Surface([0, 0]), math.degrees(bullet_i[2]))
                dis.blit(bullet_img, (((bullet_i[0])-13), ((bullet_i[1])-13)))
            elif gun_decision == 5 or gun_decision == 9:
                bullet_img = pygame.transform.flip(bullet_img, True, True)
                if 0 < angle <= math.pi/2:
                    dis.blit(bullet_img, ((bullet_i[0]-2-18*math.cos(angle)), (bullet_i[1]-2) - 22 * math.sin(angle)))
                elif math.pi/2 <= angle <= math.pi:
                    dis.blit(bullet_img, ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] - 2) - 22 * math.sin(angle)))
                elif math.pi < angle <= 3*math.pi/2:
                    dis.blit(bullet_img, ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
                elif -1*math.pi < angle <= 0:
                    dis.blit(bullet_img, ((bullet_i[0] - 2 - 18 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
            else:
                dis.blit(bullet_img, ((bullet_i[0]), (bullet_i[1])))
        for explosion_i in explosion_position_list:
            explosion_img = pygame.transform.scale(explosion_image, [14*explosion_i[2], 14*explosion_i[2]])
            explosion_img = pygame.transform.rotate(explosion_img, math.degrees(explosion_i[3]))
            dis.blit(explosion_img, (explosion_i[0]+(125-7*explosion_i[2]), explosion_i[1]+(125-7*explosion_i[2])))

        for i in range(0, 2):
            if i == 0:
                angle = angle1
                player_hitbox = player1_hitbox
                gun_state = P1_gun_state
                gun_choice = gun_choice1
            if i == 1:
                angle = angle2
                player_hitbox = player2_hitbox
                gun_state = P2_gun_state
                gun_choice = gun_choice2

            if 0 < angle <= (math.pi/2):
                dis.blit(player_image, (player_hitbox.rect.x, player_hitbox.rect.y - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox.rect.centerx-20 -
                                      (5*math.cos(angle)*gun_state), player_hitbox.rect.centery-20 - 100*math.sin(angle)))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-20 -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 16 - 145 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-10-10*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 6 - 145 * math.sin(angle)))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx-10 - 25*math.cos(angle) -
                                           (35*math.cos(angle)*gun_state),
                                           player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30*math.sin(angle)*gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx - 10 - 25*math.cos(angle),
                                           player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30 * math.sin(angle)))

                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx - 80 + 110 * math.cos(angle),
                                       player_hitbox.rect.centery - 80 - 80 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 18*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
            elif (math.pi/2) < angle <= (math.pi):
                dis.blit(pygame.transform.flip(player_image, True, False), (player_hitbox.rect.x, player_hitbox.rect.y - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox.rect.centerx - 40 + 80 * math.cos(angle) +
                                      (15*math.cos(angle)*gun_state),
                                      player_hitbox.rect.centery - 20 - 100 * math.sin(angle)))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-30+120*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 16 - 145 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-45 +115*math.cos(angle) -
                                      (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 6 - 145 * math.sin(angle)))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-30+45*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-20+110*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx - 30 + 105 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx - 30 + 105 * math.cos(angle) - 30*math.cos(angle),
                                           player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30*math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-20+110*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx - 20 + 120 * math.cos(angle),
                                       player_hitbox.rect.centery - 80 - 80 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-30+35*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
            elif (math.pi) < angle <= ((3*math.pi)/2):
                dis.blit(pygame.transform.flip(player_image, True, False), (player_hitbox.rect.x, player_hitbox.rect.y - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox.rect.centerx-20 + 100*math.cos(angle) +
                                      (15*math.cos(angle)*gun_state), player_hitbox.rect.centery-20))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-16+134*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 16 + 15 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-12 + 148*math.cos(angle) -
                                      (5*math.cos(angle)*gun_state), player_hitbox.rect.centery-6))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-5+70*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-10+120*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx - 10 + 125 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox.rect.centery - 7 + 24 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx - 10 + 125 * math.cos(angle) - 30 * math.cos(angle),
                                           player_hitbox.rect.centery - 7 + 24 * math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-10+120*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx - 80 + 60 * math.cos(angle),
                                       player_hitbox.rect.centery - 80 - 100 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-5+60*math.cos(angle) +
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 + 14 * math.sin(angle)))
            elif (-1*math.pi/2) < angle <= 0:
                dis.blit(player_image, (player_hitbox.rect.x, player_hitbox.rect.y - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox.rect.centerx - 35 + 15*math.cos(angle) -
                              (5*math.cos(angle)*gun_state), player_hitbox.rect.centery - 20))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 5*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 16 + 15 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx - 40 + 20 * math.cos(angle) -
                                      (5 * math.cos(angle) * gun_state), player_hitbox.rect.centery-6))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-30 + 20*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 15 * math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 5 or gun_choice == 9:
                    # angle += 2*math.pi
                    # print(int(gun_state))
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx-30 - 5*math.cos(angle) -
                                           (35*math.cos(angle)*gun_state),
                                           player_hitbox.rect.centery - 7 + 24 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img, (player_hitbox.rect.centerx-30 - 5*math.cos(angle),
                                           player_hitbox.rect.centery - 7 + 24 * math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 15 * math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx - 20 + 50 * math.cos(angle),
                                       player_hitbox.rect.centery - 80 - 100 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox.rect.centerx-30 + 5*math.cos(angle) -
                                       (5*math.cos(angle)*gun_state),
                                       player_hitbox.rect.centery - 8 + 14 * math.sin(angle)))
    if type == 1:
        dis.blit(main_menu_image, [0, 0])
        # dis.fill(white)
        # all_main_menu_sprites.draw(dis)
        # dis.blit(difficulty_menu_button_side_image, (410, 565))
        # dis.blit(pygame.transform.flip(difficulty_menu_button_side_image, True, False), (1310, 565))
        # dis.blit(difficulty_menu_button_main_image, (610, 565))
        # dis.blit(loadout_menu_button_side_image, (410, 815))
        # dis.blit(pygame.transform.flip(loadout_menu_button_side_image, True, False), (1310, 815))
        # dis.blit(loadout_menu_button_main_image, (610, 815))
        # dis.blit(map_menu_button_side_image, (410, 315))
        # dis.blit(pygame.transform.flip(map_menu_button_side_image, True, False), (1310, 315))
        # dis.blit(map_menu_button_main_image, (610, 315))
        # dis.blit(play_menu_button_side_image, (410, 65))
        # dis.blit(pygame.transform.flip(play_menu_button_side_image, True, False), (1310, 65))
        # dis.blit(play_menu_button_main_image, (610, 65))

    if type == 2:
        dis.blit(map_menu_image, [0, 0])
        # dis.fill(white)
        # # all_map_menu_sprites.draw(dis)
        # valu = -1
        # for m_button in all_map_menu_sprites:
        #     valu += 1
        #     img = pygame.transform.scale(background_images[valu], [192*4, 108*4])
        #     dis.blit(img, (m_button.rect.x, m_button.rect.y))
        valu = -1
        for n in range(0, 2):
            for i in range(0, 2):
                valu += 1
                if valu == map_selection:
                    pygame.draw.rect(dis, yellow, (150 + 852 * i, 80 + 488 * n, 192 * 4, 108 * 4), 10)
    if type == 3:
        dis.blit(gun_menu_image, [0, 0])
        # dis.fill(white)
        # valu = -1
        # for m_button in all_loudout_menu_sprites:
        #     valu += 1
        #     if valu != 3 and valu != 8 and valu != 7:
        #         img = pygame.transform.scale(gun_image_list[valu], [gun_image_list[valu].get_width()*2,
        #                                                             gun_image_list[valu].get_height()*2])
        #     else:
        #         img = pygame.transform.scale(gun_image_list[valu], [gun_image_list[valu].get_width() * 3,
        #                                                             gun_image_list[valu].get_height() * 3])
        #     if valu != 7:
        #         dis.blit(img, (m_button.rect.x + 100, m_button.rect.y + 100))
        #     else:
        #         dis.blit(img, (m_button.rect.x + 100, m_button.rect.y - 125))
        # # all_loudout_menu_sprites.draw(dis)
        valu = -1
        for n in range(0, 3):
            for i in range(0, 3):
                valu += 1
                if valu == gun_choice1:
                    pygame.draw.rect(dis, yellow, (150 + 550 * i, 40 + 350 * n, 250 * 2, 150 * 2), 10)
    if type == 4:
        dis.fill(white)
        all_start_menu_sprites.draw(dis)
    pygame.display.flip()


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
ground_y = 900
player_hitbox_height = 100
all_start_menu_sprites = pygame.sprite.Group()
all_main_menu_sprites = pygame.sprite.Group()
all_map_menu_sprites = pygame.sprite.Group()
all_loudout_menu_sprites = pygame.sprite.Group()
all_gameplay_sprites = pygame.sprite.Group()
platform_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
reload_box_list = pygame.sprite.Group()
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

map_selection = 0
difficulty_selection = 0
gun_choice1 = 0
gun_choice2 = 7
gun_name_list = ["Assault Rifle", "Sniper", "Flamethrower", "Sub Machine Gun", "Semi-Auto", "Rocket Launcher",
                 "Light Machine Gun", "Sword", "Shotgun", "full auto rocket launcher"]
gun_damage_list = [12, 100, 2, 10, 20, 100, 16, 30, 15, 100]
gun_fire_rate_list = [8, 150, 0, 4, 12, 300, 12, 5, 40, 0]
gun_reload_speed_list = [80, 150, 0, 70, 90, 300, 130, 0, 40, 0]
gun_range_list = [60, 200, 15, 25, 100, 150,80, 4, 15, 200]
gun_ammo_list = [(30, 90), (1, 9), (650, 0), (45, 90), (15, 30), (1, 5), (100, 100), (99999, 0), (1, 24), (99999, 0)]
gun_reload_box_values = [20, 2, 150, 30, 10, 1, 50, 0, 4, 100]
# (start, reserve)
gun_fire_type = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
# Auto = 0  Semi = 1 Single Fire = 2
gun_image_list = [assault_rifle_image, sniper_rifle_image, flamethrower_image, smg_image, semi_auto_image, rpg_image, lmg_image, sword_attack_image6, shotgun_image]
ammo_image_list = [basic_bullet_image, sniper_bullet_image, fireball_image, basic_bullet_image, basic_bullet_image,
                   rocket_image, basic_bullet_image, pygame.Surface([0, 0]), energy_ball_image, rocket_image]
in_start_menu = True
while in_start_menu:
    in_main_menu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_start_menu = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                in_start_menu = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            i = 0
            for s in all_start_menu_sprites:
                if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    if i == 0:
                        in_main_menu = True
                    if i == 1:
                        in_multiplayer_menu = True
                i += 1
    while in_main_menu:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_g] and keys[pygame.K_o] and keys[pygame.K_d] and keys[pygame.K_u] and keys[pygame.K_n] and \
                not keys[pygame.K_h] and not keys[pygame.K_j] and not keys[pygame.K_k] and not keys[pygame.K_f]:
            gun_choice1 = 9
        playing = False
        map_selection_menu = False
        loudout_menu = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_main_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_main_menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                i = 0
                for s in all_main_menu_sprites:
                    if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                        if i == 0:
                            playing = True
                        if i == 1:
                            map_selection_menu = True
                        if i == 2:
                            difficulty_selection += 1
                        if i == 3:
                            loudout_menu = True
                    i += 1
        all_gameplay_sprites = pygame.sprite.Group()
        platform_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()
        all_gameplay_sprites.empty()
        platform_list.empty()
        bullet_list.empty()
        pyramid_hitbox.empty()
        reload_box_list.empty()
        explosion_position_list = []

        timer = 0
        player1_shot_timer = 500
        player2_shot_timer = 500
        gun_choice2 = random.randint(0, 8)

        player1_ammo = gun_ammo_list[gun_choice1][0]
        player1_reserve_ammo = gun_ammo_list[gun_choice1][1]
        player2_ammo = gun_ammo_list[gun_choice2][0]
        player2_reserve_ammo = gun_ammo_list[gun_choice2][1]
        player1_reload_speed = gun_reload_speed_list[gun_choice1]
        player2_reload_speed = gun_reload_speed_list[gun_choice2]
        current_player1_ammo = 0
        current_player2_ammo = 0

        timer3 = 0
        timer4 = 0
        reload_box_timer = 10000
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
        mouse_clicked = False
        shot_fired = False
        p2_fall_death = False
        p1_fall_death = False
        P1_gun_state = 0
        P2_gun_state = 0


        bot_movement_decision_timer = 0
        bot_movement_direction = -1
        bot_jump_decision = 0
        bot_aim_timer = 500

        while map_selection_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    map_selection_menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        map_selection_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    i = 0
                    for s in all_map_menu_sprites:
                        if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            map_selection = i
                        i += 1
            dis_update(2)
            clock.tick(60)
        reload_box_pos_list = [(dis_width/2 - 50, 650), (dis_width / 2 - 50, 940), (dis_width / 2 - 50, 580),
                               (dis_width / 2 - 50, 300)]
        if map_selection == 0:

            player1_hitbox = Hitbox(50, player_hitbox_height, 100, 800, blue, 0, 0)
            player2_hitbox = Hitbox(50, player_hitbox_height, dis_width - 150, 800, orange, 0, 0)
            ground_hitbox = Hitbox(dis_width, 1080 - ground_y, 0, ground_y, black, 0, 0)
            cieling_hitbox = Hitbox(dis_width, 80, 0, -200, black, 0, 0)
            left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
            rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
            platform1_hitbox = Hitbox(300, 20, 300, 600, gray, 1, 0)
            platform2_hitbox = Hitbox(300, 20, dis_width - 600, 600, gray, 1, 0)
            platform3_hitbox = Hitbox(300, 20, dis_width / 2 - 150, 400, gray, 1, 0)
            platform4_hitbox = Hitbox(200, 20, 350, 300, gray, 1, 0)
            platform5_hitbox = Hitbox(200, 20, dis_width - 550, 300, gray, 1, 0)
            reload_box_1_hitbox = Hitbox(100, 60, dis_width/2 - 50, 650, gray, 5, 0)

            for i in range(0, 20):
                pyramid_hitbox_piece = Hitbox(700 - i * 20, 10, 610 + i * 10, 900 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

        if map_selection == 1:
            player1_hitbox = Hitbox(50, player_hitbox_height, 100, 800, blue, 0, 0)
            player2_hitbox = Hitbox(50, player_hitbox_height, dis_width - 150, 800, orange, 0, 0)
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
                pyramid_hitbox_piece = Hitbox(320 - i * 20, 10, dis_width-320-590 + i * 10, 600 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

            for i in range(0, 14):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 320 - i * 10, 380 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width-10-320 - i * 10, 380 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

            for i in range(0, 11):
                pyramid_hitbox_piece = Hitbox(200 - i * 20, 10, dis_width/2-100 + i * 10, 330 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

            for i in range(0, 22):
                pyramid_hitbox_piece = Hitbox(760 - i * 20, 10, 190 + i * 10, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(760 - i * 20, 10, dis_width-760-190 + i * 10, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                # pyramid_hitbox_piece = Hitbox(460 - i * 20, 10, 730 + i * 10, 600 - i * 10, white, 0, 0)
                # pyramid_hitbox.add(pyramid_hitbox_piece)
            platform1_hitbox = Hitbox(100, 20, 0, 700, gray, 1, 0)
            platform2_hitbox = Hitbox(100, 20, 0, 400, gray, 1, 0)
            platform3_hitbox = Hitbox(100, 20, dis_width-100, 700, gray, 1, 0)
            platform4_hitbox = Hitbox(100, 20, dis_width-100, 400, gray, 1, 0)
            # for i in range(0, 70):
            #     pyramid_hitbox_piece = Hitbox(700 - i * 10, 10, 610 + i * 5, 1000 - i * 5, black, 0, 0)
            #     pyramid_hitbox.add(pyramid_hitbox_piece)

        if map_selection == 2:
            player1_hitbox = Hitbox(50, player_hitbox_height, 100, 800, blue, 0, 0)
            player2_hitbox = Hitbox(50, player_hitbox_height, dis_width - 150, 800, orange, 0, 0)
            ground_hitbox = Hitbox(dis_width, 1080 - 1000, 0, 1000, black, 0, 0)
            cieling_hitbox = Hitbox(dis_width, 80, 0, 0, black, 0, 0)
            left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
            rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
            platform1_hitbox = Hitbox(100, 20, 0, 710, gray, 1, 0)
            platform2_hitbox = Hitbox(100, 20, dis_width - 100, 710, gray, 1, 0)
            reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 580, gray, 5, 0)
            for i in range(0, 22):
                pyramid_hitbox_piece = Hitbox(440 - i * 20, 10, dis_width/2-220 + i * 10, 440 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox((1+i) * 20, 10, dis_width/2-10 - i * 10, 850 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250 + i * 15, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width-330-250, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(220 - i * 10, 10, dis_width-330-250-220 + i * 10, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(220 - i * 10, 10, 330+250, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250 + i * 15, 540 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width - 330 - 250, 540 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, dis_width - 330 - 250 + i * 15, 540 + i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(330 - i * 15, 10, 250, 540 + (i+1) * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

                pyramid_hitbox_piece = Hitbox(630 - i * 15, 10, dis_width - 330 - 250 + i * 15, 80 + i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(580 - i * 15, 10, 0, 80 + i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
        if map_selection == 3:
            player1_hitbox = Hitbox(50, player_hitbox_height, 100, 800, blue, 0, 0)
            player2_hitbox = Hitbox(50, player_hitbox_height, dis_width - 150, 800, orange, 0, 0)
            ground_hitbox = Hitbox(dis_width, 1080 - ground_y, 0, ground_y+200, black, 0, 0)
            cieling_hitbox = Hitbox(dis_width, 80, 0, -200, black, 0, 0)
            left_border_hitbox = Hitbox(5, dis_height + 200, -5, -200, black, 0, 0)
            rightborder_hitbox = Hitbox(5, dis_height + 200, dis_width, -200, black, 0, 0)
            reload_box_1_hitbox = Hitbox(100, 60, dis_width / 2 - 50, 300, gray, 5, 0)
            for i in range(0, 16):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 340 - i * 10, 400 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width-10-340 - i * 10, 400 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
            for i in range(0, 10):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 160 - i * 10, 1000 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 160 - i * 10, 1000 - i * 10, black,
                                              0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
            for i in range(0, 16):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 500 - i * 10, 800 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 500 - i * 10, 800 - i * 10, black,
                                              0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
            for i in range(0, 10):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width/2-10 - i * 10, 900 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
            for i in range(0, 7):
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, 70 - i * 10, 600 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
                pyramid_hitbox_piece = Hitbox(20 + i * 20, 10, dis_width - 10 - 80 - i * 10, 600 - i * 10, black,
                                              0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)
            for i in range(0, 30):
                pyramid_hitbox_piece = Hitbox(20 + i * 16, 10, dis_width/2-10 - i * 8, 650 - i * 10, black, 0, 0)
                pyramid_hitbox.add(pyramid_hitbox_piece)

        while loudout_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loudout_menu = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loudout_menu = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    i = 0
                    for s in all_loudout_menu_sprites:
                        if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                            gun_choice1 = i
                            player1_reload_speed = gun_reload_speed_list[gun_choice1]
                            player1_ammo = gun_ammo_list[gun_choice1][0]
                            player1_reserve_ammo = gun_ammo_list[gun_choice1][1]
                        i += 1
            dis_update(3)
            clock.tick(60)

        player1_y_velocity = 0
        player1_x_velocity = 0
        player2_y_velocity = 0
        player2_x_velocity = 0
        reload_sequence = 1000

        while playing:
            now = time.time()
            dt = now - prev_time
            prev_time = now


            # bot 1 code difficulty easy


            if bot_movement_decision_timer > 30:
                bot_movement_direction = random.randint(-1, 1)
                bot_jump_decision = random.randint(1, 5)
                bot_movement_decision_timer = 0
            if player2_ammo == 0 and player2_reserve_ammo == 0 and not map_selection == 2:
                if reload_box_pos_list[map_selection][0] < player2_hitbox.rect.x:
                    bot_movement_direction = -1
                if reload_box_pos_list[map_selection][0] > player2_hitbox.rect.x:
                    bot_movement_direction = 1
                if reload_box_pos_list[map_selection][1] > player2_hitbox.rect.y:
                    player2_descending = True
            if player2_ammo == 0 and player2_reserve_ammo == 0 and map_selection == 2:
                if player2_hitbox.rect.x == 400:
                    reload_sequence = 0
                if 400 < player2_hitbox.rect.x:
                    bot_movement_direction = -1
                if 400 > player2_hitbox.rect.x:
                    bot_movement_direction = 1
                if 700 > player2_hitbox.rect.y:
                    bot_movement_direction = -1
                    player2_descending = True
                if reload_sequence < 150:
                    bot_movement_direction = 1
                    if reload_sequence < 30:
                        bot_jump_decision = 5
                    else:
                        bot_jump_decision = 1
            reload_sequence += 1
            if not player2_jumping:
                if player2_x_velocity > -12 and bot_movement_direction == -1:
                    player2_x_velocity -= 1.3
                if player2_x_velocity < 12 and bot_movement_direction == 1:
                    player2_x_velocity += 1.3
                if bot_jump_decision == 1:
                    player2_jumping = True
                    player2_y_velocity = -21

            bot_movement_decision_timer += 1

            if bot_aim_timer > 180:
                # error = random.uniform(-0.3, 0.3)
                if not (player1_hitbox.rect.centerx - player2_hitbox.rect.centerx) == 0:
                    if (player1_hitbox.rect.centerx - player2_hitbox.rect.centerx) > 0:
                        angle2 = math.atan((player2_hitbox.rect.centery - player1_hitbox.rect.centery) /
                                           (player1_hitbox.rect.centerx - player2_hitbox.rect.centerx))
                    elif (player1_hitbox.rect.centerx - player2_hitbox.rect.centerx) < 0:
                        angle2 = math.atan(
                            (player2_hitbox.rect.centery - player1_hitbox.rect.centery) /
                            (player1_hitbox.rect.centerx - player2_hitbox.rect.centerx)) + math.pi
                elif (player2_hitbox.rect.centery - player1_hitbox.rect.centery) > 0:
                    angle2 = math.pi/2
                elif (player2_hitbox.rect.centery - player1_hitbox.rect.centery) < 0:
                    angle2 = math.pi/2 + math.pi
                # angle2 += error

            distance_to_player = math.dist((player1_hitbox.rect.centerx, player1_hitbox.rect.centery),
                                           (player2_hitbox.rect.centerx, player2_hitbox.rect.centery))

            if player2_shot_timer > gun_fire_rate_list[gun_choice2] and player2_ammo > 0 and not player2_reload and \
                    timer > 10 and distance_to_player < gun_range_list[gun_choice2]*40:
                P2_gun_state = 1
                if gun_choice2 == 7 or gun_choice2 == 8:
                    for i in range(0, 5):
                        bullet_hitbox = Hitbox(10, 10, player2_hitbox.rect.centerx, player2_hitbox.rect.centery, red, 3,
                                               angle2 + i*(math.pi / (9*5)))
                        bullet_hitbox = Hitbox(10, 10, player2_hitbox.rect.centerx, player2_hitbox.rect.centery, red, 3,
                                               angle2 -i * (math.pi / (9*5)))
                player2_shot_timer = 0
                player2_ammo -= 1
                bullet_hitbox = Hitbox(10, 10, player2_hitbox.rect.centerx, player2_hitbox.rect.centery, red, 3,
                                       angle2)

            if player2_ammo < 1:
                player2_reload = True
                current_player2_ammo = player2_ammo

            if player2_reload:
                if player2_reserve_ammo > 0:
                    player2_reload_speed -= 1
                    if player2_reload_speed <= 0:
                        if player2_reserve_ammo - gun_ammo_list[gun_choice2][0] + current_player2_ammo > 0:
                            player2_ammo = (gun_ammo_list[gun_choice2][0])
                            player2_reserve_ammo -= gun_ammo_list[gun_choice2][0] - current_player2_ammo
                        else:
                            player2_ammo += player2_reserve_ammo
                            player2_reserve_ammo -= player2_reserve_ammo
                        player2_reload_speed = gun_reload_speed_list[gun_choice2]
                        player2_reload = False
                else:
                    player2_reload = False

            bot_aim_timer += 1

            ############End Bot Code#############

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True

            keys = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            # Player 1 movement controls

            mouse = pygame.mouse.get_pressed()

            if not (mouse_pos[0]-player1_hitbox.rect.centerx) == 0:
                if (mouse_pos[0]-player1_hitbox.rect.centerx) > 0:
                    angle1 = math.atan((player1_hitbox.rect.centery - mouse_pos[1]) / (mouse_pos[0] - player1_hitbox.rect.centerx))
                elif (mouse_pos[0] - player1_hitbox.rect.centerx) < 0:
                    angle1 = math.atan(
                        (player1_hitbox.rect.centery - mouse_pos[1]) / (mouse_pos[0] - player1_hitbox.rect.centerx)) + \
                             math.pi

            elif (player1_hitbox.rect.centery - mouse_pos[1]) > 0:
                angle1 = math.pi / 2
            elif (player1_hitbox.rect.centery - mouse_pos[1]) < 0:
                angle1 = math.pi / 2 + math.pi

            if player1_shot_timer > 5 and gun_choice1 != 7:
                P1_gun_state = 0
                if gun_choice1 == 5 and player1_ammo == 0:
                    P1_gun_state = 2
            if gun_choice1 == 7:
                if player1_shot_timer < 6:
                    P1_gun_state = player1_shot_timer
                if player1_shot_timer > 6:
                    P1_gun_state -= 1
                    if P1_gun_state < 0:
                        P1_gun_state = 0
            if player2_shot_timer > 5 and gun_choice2 != 7:
                P2_gun_state = 0
                if gun_choice2 == 5 and player2_ammo == 0:
                    P2_gun_state = 2
            if gun_choice2 == 7:
                if player2_shot_timer < 6:
                    P2_gun_state = player2_shot_timer
                if player2_shot_timer > 6:
                    P2_gun_state -= 1
                    if P2_gun_state < 0:
                        P2_gun_state = 0

            shot_fired = False
            if player1_shot_timer > gun_fire_rate_list[gun_choice1] and player1_ammo > 0 and not player1_reload \
                    and timer > 10:
                if mouse[0] and gun_fire_type[gun_choice1] == 0:
                    shot_fired = True
                elif gun_fire_type[gun_choice1] == 1 and mouse_clicked:
                    shot_fired = True
                    mouse_clicked = False
                if shot_fired:
                    P1_gun_state = 1
                    if gun_choice1 == 7 or gun_choice1 == 8:
                        for i in range(0, 5):
                            bullet_hitbox = Hitbox(10, 10, player1_hitbox.rect.centerx, player1_hitbox.rect.centery, red, 2,
                                                   angle1 + i * (math.pi / (9 * 5)))
                            bullet_hitbox = Hitbox(10, 10, player1_hitbox.rect.centerx, player1_hitbox.rect.centery, red, 2,
                                                   angle1 - i * (math.pi / (9 * 5)))
                    player1_shot_timer = 0
                    player1_ammo -= 1
                    bullet_hitbox = Hitbox(10, 10, player1_hitbox.rect.centerx, player1_hitbox.rect.centery, red, 2,
                                           angle1)
                    shot_fired = False


            for bullet in bullet_list:
                gun_selection = 0
                if bullet.type == 2:
                    gun_selection = gun_choice1
                if bullet.type == 3:
                    gun_selection = gun_choice2
                if bullet.count > gun_range_list[gun_selection]:
                    bullet.kill()
                bullet.count += 1
                if gun_selection == 5:
                    bullet.rect.y -= (500 * math.sin(bullet.angle) / 20 * dt * 70)/(1.1)
                    bullet.rect.x += (500 * math.cos(bullet.angle) / 20 * dt * 70)/(1.1)
                else:
                    bullet.rect.y -= 500 * math.sin(bullet.angle) / 20 * dt * 70
                    bullet.rect.x += 500 * math.cos(bullet.angle) / 20 * dt * 70
                for p in platform_list:
                    if bullet.rect.colliderect(p):

                        if gun_selection == 5 or gun_selection == 9:
                            explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125, \
                                                      red, 4, 0)
                        bullet.kill()
                for pp in pyramid_hitbox:
                    if bullet.rect.colliderect(pp):

                        if gun_selection == 5 or gun_selection == 9:
                            explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
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
                    player2_health -= gun_damage_list[gun_choice1]
                    if gun_choice1 == 5 or gun_selection == 9:
                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                  red, 4, 0)
                    bullet.kill()
                    timer3 = 0
                if bullet.rect.colliderect(player1_hitbox) and bullet.type == 3:
                    bullet.kill()
                    player1_health -= gun_damage_list[gun_choice2]
                    if gun_choice2 == 5 or gun_selection == 9:
                        explosion_hitbox = Hitbox(250, 250, bullet.rect.centerx - 125, bullet.rect.centery - 125,
                                                  red, 4, 0)
                    timer4 = 0

            for explosion in explosion_list:
                explosion_position_list.append([explosion.rect.x, explosion.rect.y, explosion.count, random.randint(0, 360)])
                explosion.count += 1
                if explosion.rect.colliderect(player2_hitbox):
                    player2_health -= gun_damage_list[gun_choice1]
                    timer3 = 0
                if explosion.rect.colliderect(player1_hitbox):
                    player1_health -= gun_damage_list[gun_choice1]
                    timer4 = 0
                if explosion.count > 0:
                    explosion.kill()
            for explosion_pos in explosion_position_list:
                explosion_pos[2] += 1
                if explosion_pos[2] > 20:
                    explosion_position_list.remove(explosion_pos)

            if keys[pygame.K_r]:
                player1_reload = True
                current_player1_ammo = player1_ammo

            if player1_reload:
                mouse_clicked = False
                if player1_reserve_ammo > 0:
                    player1_reload_speed -= 1
                    if player1_reload_speed <= 0:
                        if player1_reserve_ammo - gun_ammo_list[gun_choice1][0] + current_player1_ammo > 0:
                            player1_ammo = (gun_ammo_list[gun_choice1][0])
                            player1_reserve_ammo -= gun_ammo_list[gun_choice1][0] - current_player1_ammo
                        else:
                            player1_ammo += player1_reserve_ammo
                            player1_reserve_ammo -= player1_reserve_ammo
                        player1_reload_speed = gun_reload_speed_list[gun_choice1]
                        player1_reload = False
                else:
                    player1_reload = False

            if keys[pygame.K_w] and not player1_jumping:
                player1_jumping = True
                player1_y_velocity = -21
            player1_descending = False
            if keys[pygame.K_s]:
                player1_descending = True
            if keys[pygame.K_d] and not player1_jumping:
                if player1_x_velocity < 12:
                    player1_x_velocity += 1.3
            if keys[pygame.K_a] and not player1_jumping:
                if player1_x_velocity > -12:
                    player1_x_velocity -= 1.3
            if -1 < player1_x_velocity < 1 and not keys[pygame.K_d] and not keys[pygame.K_a]:
                player1_x_velocity = 0
            if player1_x_velocity > 0 and not player1_jumping:
                player1_x_velocity -= 1
            if player1_x_velocity < 0 and not player1_jumping:
                player1_x_velocity += 1
            if -1 < player2_x_velocity < 1 and not keys[pygame.K_h] and not keys[pygame.K_j]:
                player2_x_velocity = 0
            if player2_x_velocity > 0 and not player2_jumping:
                player2_x_velocity -= 1
            if player2_x_velocity < 0 and not player2_jumping:
                player2_x_velocity += 1

            gravity_strength = 40 * round(dt, 4)
            # if player1_hitbox.rect.y < ground_y - player_hitbox_height and timer > 1:
            if timer > 1:
                player1_y_velocity += gravity_strength
                player1_hitbox.rect.y += player1_y_velocity
                player1_hitbox.rect.x += player1_x_velocity * dt * 70
                player2_y_velocity += gravity_strength
                player2_hitbox.rect.y += player2_y_velocity
                player2_hitbox.rect.x += player2_x_velocity * dt * 70
            # if player1_hitbox.rect.y > ground_y - player_hitbox_height:
            #     player1_hitbox.rect.y = 900-player_hitbox_height
            #     Player1_jumping = False
            if player2_health > 100:
                player2_health = 100
            if player2_health < 100 and timer3 > 120:
                player2_health += 10
                timer3 = 90
            if player2_health <= 0:
                player2_hitbox.rect.x = dis_width - 150
                player2_hitbox.rect.y = 800
                player2_health = 100
                player2_ammo += gun_reload_box_values[gun_choice2]
                if not p2_fall_death:
                    player1_kill_count += 1
                p2_fall_death = False
            if player1_health > 100:
                player1_health = 100
            if player1_health < 100 and timer4 > 120:
                player1_health += 10
                timer4 = 90
            if player1_health <= 0:
                player1_hitbox.rect.x = 100
                player1_hitbox.rect.y = 800
                player1_health = 100
                player1_ammo += gun_reload_box_values[gun_choice1]
                player2_kill_count += 1

            if reload_box_timer == 360:
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

            if player1_y_velocity > 5:
                player1_jumping = True
            if player2_y_velocity > 5:
                player2_jumping = True

            if player1_hitbox.rect.colliderect(left_border_hitbox.rect) or \
                    player1_hitbox.rect.colliderect(rightborder_hitbox):
                player1_x_velocity = 0
            if player2_hitbox.rect.colliderect(left_border_hitbox.rect) or \
                    player2_hitbox.rect.colliderect(rightborder_hitbox):
                player2_x_velocity = 0
                bot_movement_direction = bot_movement_direction * -1
            if player1_hitbox.rect.colliderect(ground_hitbox):
                if map_selection == 3:
                    player1_health = 0
                player1_y_velocity = 0
                # player1_hitbox.rect.y = 900 - player_hitbox_height
                player1_hitbox.rect.y = ground_hitbox.rect.top - player_hitbox_height
                p1_fall_death = True
                player1_jumping = False
            if player2_hitbox.rect.colliderect(ground_hitbox):
                if map_selection == 3:
                    player2_health = 0
                    p2_fall_death = True
                player2_y_velocity = 0
                player2_hitbox.rect.y = ground_hitbox.rect.top - player_hitbox_height
                player2_jumping = False
            if player1_hitbox.rect.colliderect(cieling_hitbox):
                if player1_y_velocity < 0:
                    player1_y_velocity = player1_y_velocity * -0.25
            if player2_hitbox.rect.colliderect(cieling_hitbox):
                if player2_y_velocity < 0:
                    player2_y_velocity = player2_y_velocity * -0.25
            for platform in platform_list:
                if player1_hitbox.rect.colliderect(platform) and not player1_descending:
                    if platform.rect.top-30 < player1_hitbox.rect.bottom < platform.rect.top+30:
                        if player1_y_velocity > 0:
                            player1_y_velocity = 0
                            player1_hitbox.rect.y = platform.rect.top - player_hitbox_height
                            player1_jumping = False
                if player2_hitbox.rect.colliderect(platform) and not player2_descending:
                    if platform.rect.top-30 < player2_hitbox.rect.bottom < platform.rect.top+30:
                        if player2_y_velocity > 0:
                            player2_y_velocity = 0
                            player2_hitbox.rect.y = platform.rect.top - player_hitbox_height
                            player2_jumping = False
            for pyramid_piece in pyramid_hitbox:
                # if player1_hitbox.rect.colliderect(pyramid_piece):
                if player1_hitbox.rect.colliderect(pyramid_piece):
                    if pyramid_piece.rect.bottom - 30 < player1_hitbox.rect.top < pyramid_piece.rect.bottom + 30:
                        if player1_y_velocity < 0:
                            player1_y_velocity = player1_y_velocity * -0.25
                    if pyramid_piece.rect.top - 30 < player1_hitbox.rect.bottom < pyramid_piece.rect.top + 30:
                        if player1_y_velocity > 0:
                            player1_y_velocity = 0
                            player1_hitbox.rect.y = pyramid_piece.rect.top - player_hitbox_height
                            player1_jumping = False
                if player2_hitbox.rect.colliderect(pyramid_piece):
                    if pyramid_piece.rect.bottom - 30 < player2_hitbox.rect.top < pyramid_piece.rect.bottom + 30:
                        if player2_y_velocity < 0:
                            player2_y_velocity = player2_y_velocity * -0.25
                    if pyramid_piece.rect.top - 30 < player2_hitbox.rect.bottom < pyramid_piece.rect.top + 30:
                        if player2_y_velocity > 0:
                            player2_y_velocity = 0
                            player2_hitbox.rect.y = pyramid_piece.rect.top - player_hitbox_height
                            player2_jumping = False
            bullet_position_list.clear()
            for bullet in bullet_list:
                gun_selection = 0
                if bullet.type == 2:
                    gun_selection = gun_choice1
                elif bullet.type == 3:
                    gun_selection = gun_choice2
                if bullet.angle < 0:
                    bullet.angle = bullet.angle + 2 * math.pi
                if gun_selection == 2 and bullet.count > gun_range_list[gun_selection]:
                    bullet.angle = bullet.angle + 2*math.pi
                if gun_selection == 2 and bullet.count < 6:
                    bullet.angle = bullet.angle + 4*math.pi
                bullet_position_list.append((bullet.rect.x, bullet.rect.y, bullet.angle, bullet.type))
                if gun_selection == 2 and bullet.count < 6:
                    bullet.angle = bullet.angle - 4*math.pi
            dis_update(0)
            timer += 1
            player1_shot_timer += 1
            player2_shot_timer += 1
            timer3 += 1
            timer4 += 1
            clock.tick(60)
        dis_update(1)
        clock.tick(60)
    dis_update(4)
    clock.tick(60)

pygame.quit()
