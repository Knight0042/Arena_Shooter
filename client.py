import pygame
from network import Network
import time
import pickle
pygame.font.init()
pygame.init()
import math

player_image = pygame.image.load("player_image_2.png")

# width = 700
# height = 700
# win = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Client")

# dis_width = 1920
# dis_height = 1080
#
# # dis = pygame.display.set_mode((dis_width, dis_height), pygame.FULLSCREEN)
# dis = pygame.display.set_mode((dis_width, dis_height), pygame.FULLSCREEN)
# pygame.display.set_caption('Arena Shooter')


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

font1 = pygame.font.SysFont("bahnschrift", 300)
font2 = pygame.font.SysFont("bahnschrift", 50)
font3 = pygame.font.SysFont("bahnschrift", 45)
font4 = pygame.font.SysFont("bahnschrift", 30)
font5 = pygame.font.SysFont("bahnschrift", 200)

reload_box_image = pygame.image.load('reload_box.png')

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

sky_background = pygame.image.load('cool_sky_background.jpg')
cool_landscape_1 = pygame.image.load('wallpapersden.com_artistic-orange-landscape_1920x1080.jpg')
pyramid_background_image = pygame.image.load('background_image_option.jpg')
cave_background_image = pygame.image.load('cave_background.png')
map_1_background_image = pygame.image.load('map_1_background.png')
map_2_background_image = pygame.image.load('map_2_background.png')
map_3_background_image = pygame.image.load('map_3_background.png')
map_4_background_image = pygame.image.load('map_4_background.png')

background_images = [map_1_background_image, map_2_background_image, map_3_background_image, map_4_background_image]
pyramid_piece_1_image = pygame.image.load('pyramid_piece_111.png')
pyramid_piece_2_image = pygame.image.load('pyramid_piece_222.png')

gun_image_list = [basic_bullet_image, sniper_bullet_image, fireball_image, basic_bullet_image, basic_bullet_image,
                  rocket_image, basic_bullet_image, pygame.Surface([0, 0]), energy_ball_image, rocket_image]

main_menu_image = pygame.image.load('main_menu_image.png')
map_menu_image = pygame.image.load('map_menu_image.png')
gun_menu_image = pygame.image.load('gun_menu_image.png')


def dis_update(type, p, p2):
    # if type == 0:
    #     angle = angle1
    #     player_hitbox = player1_hitbox
    #     gun_state = P1_gun_state
    #     gun_choice = gun_choice1
    #     dis.fill(gray3)
    #     all_gameplay_sprites.draw(dis)
    #     # mouse_pointer = (50*math.cos(angle)+player1_hitbox.rect.centerx, 50*math.sin(angle)*-1+player1_hitbox.rect.centery)
    #     # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, mouse_pointer, 3)
    #     # pygame.draw.line(dis, yellow, (dis_width/2, 0), (dis_width/2, dis_height), 3)
    #     # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (player1_hitbox.rect.centerx, mouse_pos[1]), 2)
    #     # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (mouse_pos[0], player1_hitbox.rect.centery), 2)
    #     player1_ammo_message = font3.render(f"{player1_ammo}/{player1_reserve_ammo}", False, gray2)
    #     dis.blit(player1_ammo_message, (1000, 10))
    #     pygame.draw.rect(dis, red, [player2_hitbox.rect.centerx-50, player2_hitbox.rect.y-10, player2_health, 5])
    #     pygame.draw.rect(dis, red, [player1_hitbox.rect.centerx - 50, player1_hitbox.rect.y - 10, player1_health, 5])
    #     player1_kill_count_message = font3.render(f"Kills {player1_kill_count}", False, gray2)
    #     dis.blit(player1_kill_count_message, (10, 10))
    #     player2_kill_count_message = font3.render(f"Deaths {player2_kill_count}", False, gray2)
    #     dis.blit(player2_kill_count_message, (300, 10))
    #     for bullet_i in bullet_position_list:
    #         gun_decision = 0
    #         if bullet_i[3] == 2:
    #             gun_decision = gun_choice
    #         if bullet_i[3] == 3:
    #             gun_decision = gun_choice2
    #         bullet_img = pygame.transform.rotate(gun_image_list[gun_decision], math.degrees(bullet_i[2]))
    #         if gun_decision == 2:
    #             if 4*math.pi > bullet_i[2] > 2*math.pi:
    #                 bullet_img = pygame.transform.rotate(end_fireball_image, math.degrees(bullet_i[2]))
    #             if 4*math.pi < bullet_i[2]:
    #                 bullet_img = pygame.transform.rotate(pygame.Surface([0, 0]), math.degrees(bullet_i[2]))
    #             dis.blit(bullet_img, (((bullet_i[0])-13), ((bullet_i[1])-13)))
    #         elif gun_decision == 5:
    #             bullet_img = pygame.transform.flip(bullet_img, True, True)
    #             if 0 < angle <= math.pi/2:
    #                 dis.blit(bullet_img, ((bullet_i[0]-2-18*math.cos(angle)), (bullet_i[1]-2) - 22 * math.sin(angle)))
    #             elif math.pi/2 <= angle <= math.pi:
    #                 dis.blit(bullet_img, ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] - 2) - 22 * math.sin(angle)))
    #             elif math.pi < angle <= 3*math.pi/2:
    #                 dis.blit(bullet_img, ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
    #             elif -1*math.pi < angle <= 0:
    #                 dis.blit(bullet_img, ((bullet_i[0] - 2 - 18 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
    #         else:
    #             dis.blit(bullet_img, ((bullet_i[0]), (bullet_i[1])))
    #     for explosion_i in explosion_position_list:
    #         explosion_img = pygame.transform.scale(explosion_image, [14*explosion_i[2], 14*explosion_i[2]])
    #         dis.blit(explosion_img, (explosion_i[0]+(125-7*explosion_i[2]), explosion_i[1]+(125-7*explosion_i[2])))
    #
    #     for i in range(0, 2):
    #         if i == 0:
    #             angle = angle1
    #             player_hitbox = player1_hitbox
    #             gun_state = P1_gun_state
    #             gun_choice = gun_choice1
    #         if i == 1:
    #             angle = angle2
    #             player_hitbox = player2_hitbox
    #             gun_state = P2_gun_state
    #             gun_choice = gun_choice2
    #
    #         if 0 <= angle <= (math.pi/2):
    #             if gun_choice == 0:
    #                 AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
    #                 AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
    #                 dis.blit(AR_img, (player_hitbox.rect.centerx-20 -
    #                                   (5*math.cos(angle)*gun_state), player_hitbox.rect.centery-20 - 100*math.sin(angle)))
    #             elif gun_choice == 1:
    #                 gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-20 -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 16 - 145 * math.sin(angle)))
    #             elif gun_choice == 2:
    #                 gun_img = pygame.transform.flip(flamethrower_image, True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-10-10*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 6 - 145 * math.sin(angle)))
    #             elif gun_choice == 3:
    #                 gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
    #             elif gun_choice == 4:
    #                 gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
    #             elif gun_choice == 5:
    #                 gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 if -1 < gun_state < 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx-10 - 25*math.cos(angle) -
    #                                        (35*math.cos(angle)*gun_state),
    #                                        player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30*math.sin(angle)*gun_state))
    #                 if P1_gun_state == 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx - 10 - 25*math.cos(angle),
    #                                        player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30 * math.sin(angle)))
    #
    #             elif gun_choice == 6:
    #                 gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 3*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
    #             elif gun_choice == 7:
    #                 gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx - 80 + 110 * math.cos(angle),
    #                                    player_hitbox.rect.centery - 80 - 80 * math.sin(angle)))
    #             elif gun_choice == 8:
    #                 gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-7 - 18*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
    #         elif (math.pi/2) < angle <= (math.pi):
    #             if gun_choice == 0:
    #                 AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
    #                 AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
    #                 dis.blit(AR_img, (player_hitbox.rect.centerx - 40 + 80 * math.cos(angle) +
    #                                   (15*math.cos(angle)*gun_state),
    #                                   player_hitbox.rect.centery - 20 - 100 * math.sin(angle)))
    #             elif gun_choice == 1:
    #                 gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-30+120*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 16 - 145 * math.sin(angle)))
    #             elif gun_choice == 2:
    #                 gun_img = pygame.transform.flip(flamethrower_image, True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-45 +115*math.cos(angle) -
    #                                   (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 6 - 145 * math.sin(angle)))
    #             elif gun_choice == 3:
    #                 gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-30+45*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
    #             elif gun_choice == 4:
    #                 gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-20+110*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
    #             elif gun_choice == 5:
    #                 gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 if -1 < gun_state < 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx - 30 + 105 * math.cos(angle) -
    #                                        (35 * math.cos(angle) * gun_state),
    #                                        player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 28 * math.sin(
    #                                            angle) * gun_state))
    #                 if gun_state == 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx - 30 + 105 * math.cos(angle) - 30*math.cos(angle),
    #                                        player_hitbox.rect.centery - 7 - 134 * math.sin(angle) + 30*math.sin(angle)))
    #             elif gun_choice == 6:
    #                 gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-20+110*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 125 * math.sin(angle)))
    #             elif gun_choice == 7:
    #                 gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx - 20 + 120 * math.cos(angle),
    #                                    player_hitbox.rect.centery - 80 - 80 * math.sin(angle)))
    #             elif gun_choice == 8:
    #                 gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-30+35*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 - 55 * math.sin(angle)))
    #         elif (math.pi) < angle <= ((3*math.pi)/2):
    #             if gun_choice == 0:
    #                 AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
    #                 AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
    #                 dis.blit(AR_img, (player_hitbox.rect.centerx-20 + 100*math.cos(angle) +
    #                                   (15*math.cos(angle)*gun_state), player_hitbox.rect.centery-20))
    #             elif gun_choice == 1:
    #                 gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-16+134*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 16 + 15 * math.sin(angle)))
    #             elif gun_choice == 2:
    #                 gun_img = pygame.transform.flip(flamethrower_image, True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-12 + 148*math.cos(angle) -
    #                                   (5*math.cos(angle)*gun_state), player_hitbox.rect.centery-6))
    #             elif gun_choice == 3:
    #                 gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-5+70*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 4:
    #                 gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-10+120*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 5:
    #                 gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 if -1 < gun_state < 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx - 10 + 125 * math.cos(angle) -
    #                                        (35 * math.cos(angle) * gun_state),
    #                                        player_hitbox.rect.centery - 7 + 24 * math.sin(angle) + 28 * math.sin(
    #                                            angle) * gun_state))
    #                 if gun_state == 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx - 10 + 125 * math.cos(angle) - 30 * math.cos(angle),
    #                                        player_hitbox.rect.centery - 7 + 24 * math.sin(angle)))
    #             elif gun_choice == 6:
    #                 gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-10+120*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 7:
    #                 gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx - 80 + 60 * math.cos(angle),
    #                                    player_hitbox.rect.centery - 80 - 100 * math.sin(angle)))
    #             elif gun_choice == 8:
    #                 gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-5+60*math.cos(angle) +
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 + 14 * math.sin(angle)))
    #         elif (-1*math.pi/2) < angle <= 0:
    #             if gun_choice == 0:
    #                 AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
    #                 AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
    #                 dis.blit(AR_img, (player_hitbox.rect.centerx - 35 + 15*math.cos(angle) -
    #                           (5*math.cos(angle)*gun_state), player_hitbox.rect.centery - 20))
    #             elif gun_choice == 1:
    #                 gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 5*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 16 + 15 * math.sin(angle)))
    #             elif gun_choice == 2:
    #                 gun_img = pygame.transform.flip(flamethrower_image, True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx - 40 + 20 * math.cos(angle) -
    #                                   (5 * math.cos(angle) * gun_state), player_hitbox.rect.centery-6))
    #             elif gun_choice == 3:
    #                 gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-30 + 20*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 4:
    #                 gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 15 * math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 5:
    #                 # angle += 2*math.pi
    #                 print(int(gun_state))
    #                 gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 if -1 < gun_state < 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx-30 - 5*math.cos(angle) -
    #                                        (35*math.cos(angle)*gun_state),
    #                                        player_hitbox.rect.centery - 7 + 24 * math.sin(angle) + 28 * math.sin(
    #                                            angle) * gun_state))
    #                 if gun_state == 2:
    #                     dis.blit(gun_img, (player_hitbox.rect.centerx-30 - 5*math.cos(angle),
    #                                        player_hitbox.rect.centery - 7 + 24 * math.sin(angle)))
    #             elif gun_choice == 6:
    #                 gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-25 + 15 * math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8))
    #             elif gun_choice == 7:
    #                 gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx - 20 + 50 * math.cos(angle),
    #                                    player_hitbox.rect.centery - 80 - 100 * math.sin(angle)))
    #             elif gun_choice == 8:
    #                 gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
    #                 gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
    #                 dis.blit(gun_img, (player_hitbox.rect.centerx-30 + 5*math.cos(angle) -
    #                                    (5*math.cos(angle)*gun_state),
    #                                    player_hitbox.rect.centery - 8 + 14 * math.sin(angle)))
    # if type == 1:
    #     dis.fill(white)
    #     all_main_menu_sprites.draw(dis)
    # if type == 2:
    #     dis.fill(white)
    #     all_map_menu_sprites.draw(dis)
    #     valu = -1
    #     for n in range(0, 2):
    #         for i in range(0, 2):
    #             valu += 1
    #             if valu == map_selection:
    #                 pygame.draw.rect(dis, yellow, (150 + 852 * i, 80 + 488 * n, 192 * 4, 108 * 4), 10)
    # if type == 3:
    #     dis.fill(white)
    #     all_loudout_menu_sprites.draw(dis)
    #     valu = -1
    #     for n in range(0, 3):
    #         for i in range(0, 3):
    #             valu += 1
    #             if valu == gun_choice1:
    #                 pygame.draw.rect(dis, yellow, (150 + 550 * i, 40 + 350 * n, 250 * 2, 150 * 2), 10)
    # if type == 4:
    #     dis.fill(white)
    #     all_start_menu_sprites.draw(dis)
    if type == 5:
        angle = angle1
        dis.fill(gray3)
        # p.draw(dis)
        # p2.draw(dis)
        # dis.blit(place_holder_img, (p[0], p[1]))
        # dis.blit(place_holder_img, (p2[0], p2[1]))
        dis.blit(background_images[map_selection], (0, 0))
        # mouse_pointer = (
        # 50 * math.cos(angle) + p[0]+25, 50 * math.sin(angle) * -1 + p[1]+50)
        # pygame.draw.line(dis, yellow, (p[0]+25, p[1]+50), mouse_pointer, 3)

        angle = angle1
        P1_gun_state = 0
        gun_state = P1_gun_state
        gun_choice = p[7]
        # all_gameplay_sprites.draw(dis)
        # platform_list.draw(dis)
        # mouse_pointer = (50*math.cos(angle)+player1_hitbox.rect.centerx, 50*math.sin(angle)*-1+player1_hitbox.rect.centery)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, mouse_pointer, 3)
        # pygame.draw.line(dis, yellow, (dis_width/2, 0), (dis_width/2, dis_height), 3)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (player1_hitbox.rect.centerx, mouse_pos[1]), 2)
        # pygame.draw.line(dis, yellow, player1_hitbox.rect.center, (mouse_pos[0], player1_hitbox.rect.centery), 2)
        player1_ammo_message = font3.render(f"{p[9]}/{p[10]}", False, gray3)
        dis.blit(player1_ammo_message, (1000, 10))
        pygame.draw.rect(dis, red, [p2[0]+25 - 50, p2[1] - 20, p2[15], 5])
        pygame.draw.rect(dis, red, [p[0]+25 - 50, p[1] - 20, p[15], 5])
        player1_kill_count_message = font3.render(f"Kills {p[16]}", False, gray3)
        dis.blit(player1_kill_count_message, (10, 10))
        player2_kill_count_message = font3.render(f"Deaths {p2[16]}", False, gray3)
        dis.blit(player2_kill_count_message, (300, 10))
        for box in reload_box_pos_list:
            print(box)
            dis.blit(reload_box_image, box)
        #
        for bullet_i in bullet_position_list:
            gun_decision = 0
            if bullet_i[3] == 2:
                if p[6] == 0:
                    gun_decision = p[7]
                if p[6] == 1:
                    gun_decision = p2[7]
            if bullet_i[3] == 3:
                if p[6] == 0:
                    gun_decision = p2[7]
                if p[6] == 1:
                    gun_decision = p[7]
            bullet_img = pygame.transform.rotate(gun_image_list[gun_decision], math.degrees(bullet_i[2]))
            if gun_decision == 2:
                if 4 * math.pi > bullet_i[2] > 2 * math.pi:
                    bullet_img = pygame.transform.rotate(end_fireball_image, math.degrees(bullet_i[2]))
                if 4 * math.pi < bullet_i[2]:
                    bullet_img = pygame.transform.rotate(pygame.Surface([0, 0]), math.degrees(bullet_i[2]))
                dis.blit(bullet_img, (((bullet_i[0]) - 13), ((bullet_i[1]) - 13)))
            elif gun_decision == 5 or gun_decision == 9:
                bullet_img = pygame.transform.flip(bullet_img, True, True)
                if 0 < angle <= math.pi / 2:
                    dis.blit(bullet_img,
                             ((bullet_i[0] - 2 - 18 * math.cos(angle)), (bullet_i[1] - 2) - 22 * math.sin(angle)))
                elif math.pi / 2 <= angle <= math.pi:
                    dis.blit(bullet_img,
                             ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] - 2) - 22 * math.sin(angle)))
                elif math.pi < angle <= 3 * math.pi / 2:
                    dis.blit(bullet_img,
                             ((bullet_i[0] - 2 + 22 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
                elif -1 * math.pi < angle <= 0:
                    dis.blit(bullet_img,
                             ((bullet_i[0] - 2 - 18 * math.cos(angle)), (bullet_i[1] + 2 + 22 * math.sin(angle))))
            else:
                dis.blit(bullet_img, ((bullet_i[0]), (bullet_i[1])))
        for explosion_i in explosion_position_list:
            explosion_img = pygame.transform.scale(explosion_image, [14 * explosion_i[2], 14 * explosion_i[2]])
            dis.blit(explosion_img,
                     (explosion_i[0] + (125 - 7 * explosion_i[2]), explosion_i[1] + (125 - 7 * explosion_i[2])))

        for i in range(0, 2):
            if i == 0:
                angle = angle1
                player_hitbox = p
                gun_state = p[12]
                gun_choice = p[7]
            if i == 1:
                angle = angle2
                player_hitbox = p2
                gun_state = p2[12]
                gun_choice = p2[7]

            if 0 < angle <= (math.pi / 2):
                dis.blit(player_image, (player_hitbox[0], player_hitbox[1] - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox[0]+25 - 20 -
                                      (5 * math.cos(angle) * gun_state),
                                      player_hitbox[1]+50 - 20 - 100 * math.sin(angle)))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 20 -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 16 - 145 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 10 - 10 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 6 - 145 * math.sin(angle)))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 7 - 3 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 55 * math.sin(angle)))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 7 - 3 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 125 * math.sin(angle)))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 10 - 25 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox[1]+50 - 7 - 134 * math.sin(angle) + 30 * math.sin(
                                               angle) * gun_state))
                    if P1_gun_state == 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 10 - 25 * math.cos(angle),
                                           player_hitbox[1]+50 - 7 - 134 * math.sin(angle) + 30 * math.sin(
                                               angle)))

                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 7 - 3 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 125 * math.sin(angle)))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 80 + 110 * math.cos(angle),
                                       player_hitbox[1]+50 - 80 - 80 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 7 - 18 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 55 * math.sin(angle)))
            elif (math.pi / 2) < angle <= (math.pi):
                dis.blit(pygame.transform.flip(player_image, True, False),
                         (player_hitbox[0], player_hitbox[1] - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox[0]+25 - 40 + 80 * math.cos(angle) +
                                      (15 * math.cos(angle) * gun_state),
                                      player_hitbox[1]+50 - 20 - 100 * math.sin(angle)))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 120 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 16 - 145 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 45 + 115 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 6 - 145 * math.sin(angle)))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 45 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 55 * math.sin(angle)))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 20 + 110 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 125 * math.sin(angle)))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 105 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox[1]+50 - 7 - 134 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img,
                                 (player_hitbox[0]+25 - 30 + 105 * math.cos(angle) - 30 * math.cos(angle),
                                  player_hitbox[1]+50 - 7 - 134 * math.sin(angle) + 30 * math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 20 + 110 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 125 * math.sin(angle)))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 20 + 120 * math.cos(angle),
                                       player_hitbox[1]+50 - 80 - 80 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 35 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 - 55 * math.sin(angle)))
            elif (math.pi) < angle <= ((3 * math.pi) / 2):
                dis.blit(pygame.transform.flip(player_image, True, False),
                         (player_hitbox[0], player_hitbox[1] - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, True)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox[0]+25 - 20 + 100 * math.cos(angle) +
                                      (15 * math.cos(angle) * gun_state), player_hitbox[1]+50 - 20))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 16 + 134 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 16 + 15 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 12 + 148 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state), player_hitbox[1]+50 - 6))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 5 + 70 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 10 + 120 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 5 or gun_choice == 9:
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 10 + 125 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox[1]+50 - 7 + 24 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img,
                                 (player_hitbox[0]+25 - 10 + 125 * math.cos(angle) - 30 * math.cos(angle),
                                  player_hitbox[1]-50 - 7 + 24 * math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 10 + 120 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 80 + 60 * math.cos(angle),
                                       player_hitbox[1]+50 - 80 - 100 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, True)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 5 + 60 * math.cos(angle) +
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 + 14 * math.sin(angle)))
            elif (-1 * math.pi / 2) < angle <= 0:
                dis.blit(player_image, (player_hitbox[0], player_hitbox[1] - 10))
                if gun_choice == 0:
                    AR_img = pygame.transform.flip(assault_rifle_images[gun_state], True, False)
                    AR_img = pygame.transform.rotate(AR_img, math.degrees(angle))
                    dis.blit(AR_img, (player_hitbox[0]+25 - 35 + 15 * math.cos(angle) -
                                      (5 * math.cos(angle) * gun_state), player_hitbox[1]+50 - 20))
                elif gun_choice == 1:
                    gun_img = pygame.transform.flip(sniper_rifle_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 25 + 5 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 16 + 15 * math.sin(angle)))
                elif gun_choice == 2:
                    gun_img = pygame.transform.flip(flamethrower_image, True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 40 + 20 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state), player_hitbox[1]+50 - 6))
                elif gun_choice == 3:
                    gun_img = pygame.transform.flip(smg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 20 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 4:
                    gun_img = pygame.transform.flip(semi_auto_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 25 + 15 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 5 or gun_choice == 9:
                    # angle += 2*math.pi
                    gun_img = pygame.transform.flip(rpg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    if -1 < gun_state < 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 30 - 5 * math.cos(angle) -
                                           (35 * math.cos(angle) * gun_state),
                                           player_hitbox[1]+50 - 7 + 24 * math.sin(angle) + 28 * math.sin(
                                               angle) * gun_state))
                    if gun_state == 2:
                        dis.blit(gun_img, (player_hitbox[0]+25 - 30 - 5 * math.cos(angle),
                                           player_hitbox[1]+50 - 7 + 24 * math.sin(angle)))
                elif gun_choice == 6:
                    gun_img = pygame.transform.flip(lmg_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 25 + 15 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8))
                elif gun_choice == 7:
                    gun_img = pygame.transform.flip(sword_images[gun_state], False, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 20 + 50 * math.cos(angle),
                                       player_hitbox[1]+50 - 80 - 100 * math.sin(angle)))
                elif gun_choice == 8:
                    gun_img = pygame.transform.flip(shotgun_images[gun_state], True, False)
                    gun_img = pygame.transform.rotate(gun_img, math.degrees(angle))
                    dis.blit(gun_img, (player_hitbox[0]+25 - 30 + 5 * math.cos(angle) -
                                       (5 * math.cos(angle) * gun_state),
                                       player_hitbox[1]+50 - 8 + 14 * math.sin(angle)))
    if type == 6:
        dis.blit(main_menu_image, [0, 0])
    if type == 7:
        dis.blit(map_menu_image, [0, 0])
        valu = -1
        for n in range(0, 2):
            for i in range(0, 2):
                valu += 1
                if valu == map_selection:
                    pygame.draw.rect(dis, yellow, (150 + 852 * i, 80 + 488 * n, 192 * 4, 108 * 4), 10)
    if type == 8:
        dis.blit(gun_menu_image, [0, 0])
        # dis.fill(white)
        # valu = -1
        # for m_button in all_loudout_menu_sprites:
        #     valu += 1
        #     if valu != 3 and valu != 8 and valu != 7:
        #         img = pygame.transform.scale(gun_image_list[valu], [gun_image_list[valu].get_width() * 2,
        #                                                             gun_image_list[valu].get_height() * 2])
        #     else:
        #         img = pygame.transform.scale(gun_image_list[valu], [gun_image_list[valu].get_width() * 3,
        #                                                             gun_image_list[valu].get_height() * 3])
        #     if valu != 7:
        #         dis.blit(img, (m_button.rect.x + 100, m_button.rect.y + 100))
        #     else:
        #         dis.blit(img, (m_button.rect.x + 100, m_button.rect.y - 125))
        # all_loudout_menu_sprites.draw(dis)
        valu = -1
        for n in range(0, 3):
            for i in range(0, 3):
                valu += 1
                if valu == p[7]:
                    pygame.draw.rect(dis, yellow, (150 + 550 * i, 40 + 350 * n, 250 * 2, 150 * 2), 10)



    pygame.display.flip()

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
#
# class MenuButton(pygame.sprite.Sprite):
#     def __init__(self, width, height, x, y, color, type, menu_number):
#         super().__init__()
#         rectangle = pygame.Surface([width, height])
#         rectangle.fill(color)
#         self.image = rectangle
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.type = type
#         if menu_number == 0:
#             all_main_menu_sprites.add(self)
#         if menu_number == 1:
#             all_map_menu_sprites.add(self)
#         if menu_number == 2:
#             all_loudout_menu_sprites.add(self)

ground_y = 900
player_hitbox_height = 100
all_main_menu_sprites = pygame.sprite.Group()
all_map_menu_sprites = pygame.sprite.Group()
all_loudout_menu_sprites = pygame.sprite.Group()
all_gameplay_sprites = pygame.sprite.Group()
platform_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
explosion_list = pygame.sprite.Group()
pyramid_hitbox = pygame.sprite.Group()
bullet_position_list = [(0, 0)]
bullet_position_list2 = [(0, 0)]
#
# for n in range(0, 4):
#     menu_button = MenuButton(1100, 200, 410, 65 + 250 * n, black, n, 0)
#
# for n in range(0, 2):
#     for i in range(0, 2):
#         menu_button = MenuButton(192 * 4, 108 * 4, 150 + 852 * i, 80 + 488 * n, black, (i, n), 1)
#
# for n in range(0, 3):
#     for i in range(0, 3):
#         menu_button = MenuButton(250 * 2, 150 * 2, 150 + 550 * i, 40 + 350 * n, black, (i, n), 2)

in_main_menu = True
map_selection = 0
difficulty_selection = 0
gun_choice = 0
gun_choice2 = 0
gun_name_list = ["Assault Rifle", "Sniper", "Flamethrower", "Sub Machine Gun", "Semi-Auto", "Rocket Launcher",
                 "Light Machine Gun", "Sword", "Shotgun"]
gun_damage_list = [10, 100, 2, 9, 20, 100, 14, 100, 15]
gun_fire_rate_list = [8, 150, 0, 4, 10, 300, 12, 3, 40]
gun_reload_speed_list = [80, 150, 0, 60, 90, 300, 130, 0, 40]
gun_range_list = [60, 200, 15, 20, 100, 60, 80, 4, 15]
gun_ammo_list = [(30, 90), (1, 9), (650, 0), (45, 90), (20, 40), (1, 5), (100, 100), (99999, 0), (1, 24)]
# (start, reserve)
gun_fire_type = [0, 1, 0, 0, 1, 1, 0, 1, 1]
# Auto = 0  Semi = 1 Single Fire = 2
# gun_image_list = [basic_bullet_image, sniper_bullet_image, fireball_image, basic_bullet_image, basic_bullet_image,
#                   rocket_image, basic_bullet_image, sword_attack_image, energy_ball_image]

# while in_main_menu:
#     playing = False
#     map_selection_menu = False
#     loudout_menu = False
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             in_main_menu = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 in_main_menu = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             i = 0
#             for s in all_main_menu_sprites:
#                 if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
#                     if i == 0:
#                         playing = True
#                     if i == 1:
#                         map_selection_menu = True
#                     if i == 2:
#                         difficulty_selection += 1
#                     if i == 3:
#                         loudout_menu = True
#                 i += 1



# class Button:
#     def __init__(self, text, x, y, color):
#         self.text = text
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = 150
#         self.height = 100
#
#     def draw(self, win):
#         pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
#         font = pygame.font.SysFont("comicsans", 40)
#         text = font.render(self.text, 1, (255,255,255))
#         win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
#
#     def click(self, pos):
#         x1 = pos[0]
#         y1 = pos[1]
#         if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
#             return True
#         else:
#             return False


# def redrawWindow(win, game, p):
#     win.fill((128,128,128))
#
#     if not(game.connected()):
#         font = pygame.font.SysFont("comicsans", 80)
#         text = font.render("Waiting for Player...", 1, (255,0,0), True)
#         win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
#     pygame.display.update()


# btns = [Button("Rock", 50, 500, (0,0,0)), Button("Scissors", 250, 500, (255,0,0)), Button("Paper", 450, 500, (0,255,0))]
# def main():
dis_width = 1920
dis_height = 1080

# dis = pygame.display.set_mode((dis_width, dis_height), pygame.FULLSCREEN)
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Arena Shooter')
# reload_box_pos_list = [(dis_width / 2 - 50, 650), (dis_width / 2 - 50, 940), (dis_width / 2 - 50, 580),
#                                        (dis_width / 2 - 50, 300)]
run = True
clock = pygame.time.Clock()
n = Network()
# print(player2)
# print("You are player", p)
player_angle = 0
timer = 0
prev_time = time.time()
while run:
    now = time.time()
    dt = now - prev_time
    prev_time = now
    player = n.getP()
    recieved_data = n.send(player)
    player1 = recieved_data[0]
    player2 = recieved_data[1]
    bullet_position_list = recieved_data[2]
    explosion_position_list = recieved_data[3]
    map_selection = recieved_data[4]
    reload_box_pos_list = recieved_data[5]
    player[0] = player1[0]
    player[1] = player1[1]
    player[2] = player1[2]
    player[3] = player1[3]
    player[4] = player1[4]
    player[5] = player1[5]
    player[7] = player1[7]
    player[9] = player1[9]
    player[10] = player1[10]
    player[11] = player1[11]
    player[12] = player1[12]
    player[13] = player1[13]
    player[14] = dt
    player[15] = player1[15]
    player[17] = player1[17]
    # player[17] += 1
    player[18] = player1[18]
    player[18] += 1
    player[19].clear()
    player[20] = player1[20]
    print(explosion_position_list)
    # print(player[17])
    # player2[15] = player2[15]
    # player2 = n.send(player)
    clock.tick(60)
    # try:
    #     game = n.send("get")
    # except:
    #     run = False
    #     print("Couldn't get game")
    #     break
    # player2 = n.send(player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                player[19].append('esc')
                # run = False
                # pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player[13] = True
        if event.type == pygame.MOUSEBUTTONUP:
            player[13] = False
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player[1] -= 5
    # if keys[pygame.K_s]:
    #     player[1] += 5
    # if keys[pygame.K_d]:
    #     player[0] += 5
    # if keys[pygame.K_a]:
    #     player[0] -= 5
    angle1 = player1[8]
    angle2 = player2[8]
    mouse_pos = pygame.mouse.get_pos()
    player[21] = mouse_pos
    if not (mouse_pos[0] - player[0]+25) == 0:
        if (mouse_pos[0] - player[0]+25) > 0:
            angle1 = math.atan(
                (player[1]+50 - mouse_pos[1]) / (mouse_pos[0] - player[0]+25))
        elif (mouse_pos[0] - player[0]+25) < 0:
            angle1 = math.atan(
                (player[1]+50 - mouse_pos[1]) / (mouse_pos[0] - player[0]+25)) + \
                     math.pi

    elif (player[1]+50 - mouse_pos[1]) > 0:
        angle1 = math.pi / 2
    elif (player[1]+50 - mouse_pos[1]) < 0:
        angle1 = math.pi / 2 + math.pi

    player[8] = angle1
    # player1_jumping = False
    #
    if keys[pygame.K_r]:
        player[19].append('r')
        # player[11] = True
        # current_player1_ammo = player1_ammo
    if keys[pygame.K_w] and not player[2]:
        # player[2] = True
        player[19].append('w')
        # player[5] = -21
    # player[3] = False
    if keys[pygame.K_s]:
        player[19].append('s')
        # player[3] = True
    if keys[pygame.K_d] and not player[2]:
        player[19].append('d')
        # if player[4] < 12:
        #     player[4] += 1.3
    if keys[pygame.K_a] and not player[2]:
        player[19].append('a')
        # if player[4] > -12:
        #     player[4] -= 1.3
    # if -1 < player[4] < 1 and not keys[pygame.K_d] and not keys[pygame.K_a]:
    #     player[4] = 0
    # if player[4] > 0 and not player[2]:
    #     player[4] -= 1
    # if player[4] < 0 and not player[2]:
    #     player[4] += 1

    # gravity_strength = 40 * round(dt, 4)
    # if player1_hitbox.rect.y < ground_y - player_hitbox_height and timer > 1:
    # if timer > 1:
    #     player[5] += gravity_strength
    #     player[1] += player[5]
    #     player[0] += player[4] * dt * 70



        #
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     for btn in btns:
        #         if btn.click(pos) and game.connected():
        #             if player == 0:
        #                 if not game.p1Went:
        #                     n.send(btn.text)
        #             else:
        #                 if not game.p2Went:
        #                     n.send(btn.text)
    timer += 1
    print(player[20])
    dis_update(player[20], player1, player2)
#
# def menu_screen():
#     run = True
#     in_main_menu = True
#     clock = pygame.time.Clock()
#     while in_main_menu:
#         playing = False
#         map_selection_menu = False
#         loudout_menu = False
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 in_main_menu = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     in_main_menu = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 i = 0
#                 for s in all_main_menu_sprites:
#                     if s.rect.collidepoint(mouse_pos[0], mouse_pos[1]):
#                         if i == 0:
#                             main()
#                             playing = True
#                         if i == 1:
#                             map_selection_menu = True
#                         if i == 2:
#                             difficulty_selection += 1
#                         if i == 3:
#                             loudout_menu = True
#                     i += 1
#         dis_update(0, 1)
#         clock.tick(60)

# while run:
#     clock.tick(60)
#     win.fill((128, 128, 128))
#     font = pygame.font.SysFont("comicsans", 60)
#     text = font.render("Click to Play!", 1, (255,0,0))
#     win.blit(text, (100,200))
#     pygame.display.update()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             run = False
#
# main()

