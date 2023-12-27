#Import libraries
import pygame, sys, time, pygame.gfxdraw

class Eris(pygame.sprite.Sprite):
    #Assign attributes to character
    def __init__(self):
        super().__init__()
        #Load sprites + music
        stand_left = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-stand-left.png').convert_alpha()
        stand_right = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-stand-right.png').convert_alpha()
        run_left_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_1-left.png').convert_alpha()
        run_left_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_2-left.png').convert_alpha()
        run_left_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_3-left.png').convert_alpha()
        run_right_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_1-right.png').convert_alpha()
        run_right_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_2-right.png').convert_alpha()
        run_right_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Stand_+_Run/av_1-run_3-right.png').convert_alpha()
        jump_left_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_1-left.png').convert_alpha()
        jump_left_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_2-left.png').convert_alpha()
        jump_left_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_3-left.png').convert_alpha()
        jump_left_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_4-left.png').convert_alpha()
        jump_left_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_5-left.png').convert_alpha()
        jump_right_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_1-right.png').convert_alpha()
        jump_right_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_2-right.png').convert_alpha()
        jump_right_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_3-right.png').convert_alpha()
        jump_right_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_4-right.png').convert_alpha()
        jump_right_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Jump/av_1-jump_5-right.png').convert_alpha()
        respawn_right_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_1-right.png').convert_alpha()
        respawn_right_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_2-right.png').convert_alpha()
        respawn_right_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_3-right.png').convert_alpha()
        respawn_left_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_1-left.png').convert_alpha()
        respawn_left_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_2-left.png').convert_alpha()
        respawn_left_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Respawn/av_1-respawn_3-left.png').convert_alpha()
        melee_left_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_1-left.png').convert_alpha()
        melee_left_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_2-left.png').convert_alpha()
        melee_left_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_4-left.png').convert_alpha()
        melee_left_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_5-left.png').convert_alpha()
        melee_left_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_6-left.png').convert_alpha()
        melee_left_6 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_8-left.png').convert_alpha()
        melee_left_7 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_10-left.png').convert_alpha()
        melee_right_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_1-right.png').convert_alpha()
        melee_right_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_2-right.png').convert_alpha()
        melee_right_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_4-right.png').convert_alpha()
        melee_right_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_5-right.png').convert_alpha()
        melee_right_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_6-right.png').convert_alpha()
        melee_right_6 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_8-right.png').convert_alpha()
        melee_right_7 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Melee/av_1-melee_10-right.png').convert_alpha()
        range_left_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_1-left.png').convert_alpha()
        range_left_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_2-left.png').convert_alpha()
        range_left_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_3-left.png').convert_alpha()
        range_left_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_4-left.png').convert_alpha()
        range_right_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_1-right.png').convert_alpha()
        range_right_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_2-right.png').convert_alpha()
        range_right_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_3-right.png').convert_alpha()
        range_right_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-range_4-right.png').convert_alpha()
        bullet_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_1.png').convert_alpha()
        bullet_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_2.png').convert_alpha()
        bullet_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_3.png').convert_alpha()
        bullet_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_5.png').convert_alpha()
        bullet_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_6.png').convert_alpha()
        bullet_6 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_7.png').convert_alpha()
        bullet_7 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_8.png').convert_alpha()
        bullet_8 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Long_Range/av_1-bullet_9.png').convert_alpha()
        explosion_1 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_1.png').convert_alpha()
        explosion_2 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_3.png').convert_alpha()
        explosion_3 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_4.png').convert_alpha()
        explosion_4 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_5.png').convert_alpha()
        explosion_5 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_6.png').convert_alpha()
        explosion_6 = pygame.image.load('Sprites/Eris_Goddess_of_Strife/Explosion_Animation/av_1-explosion_7.png').convert_alpha()
        heart_lives = pygame.image.load('Sprites/Game_Environment/heart_lives.png').convert_alpha()
        self.jump_effect = pygame.mixer.Sound('Sprites/Game_Environment/jump-sound.wav')
        self.sword_effect = pygame.mixer.Sound('Sprites/Game_Environment/sword-sound.wav')
        self.sword_effect.set_volume(0.5)
        self.long_range_effect = pygame.mixer.Sound('Sprites/Game_Environment/eris-long_range-sound.wav')
        self.long_range_effect.set_volume(4)

        #Categorize sprites for animation 
        self.stand = [stand_left, stand_right]
        self.run_left = [run_left_1, run_left_2, run_left_3]
        self.run_left_index = 0
        self.run_right = [run_right_1, run_right_2, run_right_3]
        self.run_right_index = 0
        self.jump_left = [jump_left_1, jump_left_2, jump_left_3, jump_left_4, jump_left_5]
        self.jump_left_index = 0
        self.jump_right = [jump_right_1, jump_right_2, jump_right_3, jump_right_4, jump_right_5]
        self.jump_right_index = 0
        self.respawn_left = [respawn_left_1, respawn_left_2, respawn_left_3, stand_left]
        self.respawn_right = [respawn_right_1, respawn_right_2, respawn_right_3, stand_right]
        self.respawn_index = 0
        self.melee_left = [melee_left_1, melee_left_2, melee_left_3, melee_left_4, melee_left_5, melee_left_6, melee_left_7]
        self.melee_right = [melee_right_1, melee_right_2, melee_right_3, melee_right_4, melee_right_5, melee_right_6, melee_right_7]
        self.melee_index = 0
        self.range_left = [range_left_1, range_left_2, range_left_3, range_left_4]
        self.range_right = [range_right_1, range_right_2, range_right_3, range_right_4]
        self.range_index = 0
        self.bullet = [bullet_1, bullet_2, bullet_3, bullet_4, bullet_5, bullet_6, bullet_7, bullet_8]
        self.bullet_index = 0
        self.explosion = [explosion_1, explosion_2, explosion_3, explosion_4, explosion_5, explosion_6]
        self.explosion_index = 0
        self.lives_image = heart_lives

        #Starting position + initialize images
        self.x_pos = 100
        self.y_pos = 690
        self.bullet_x_pos = 100
        self.bullet_y_pos = 690
        self.image = stand_right
        self.right = True
        self.left = False
        self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))
        screen.blit(self.image, self.rect)
        self.bullet_image = self.bullet[0]
        self.bullet_rect = self.bullet_image.get_rect(center = (self.bullet_x_pos, self.bullet_y_pos))

        #States + variable initializations
        self.jump_state = False
        self.melee_state = False
        self.range_state = False
        self.bullet_state = False
        self.bullet_direction = False
        self.top_platform = False
        self.bottom_platform = False
        self.gravity = 0
        self.health = 100
        self.lives = 3
        self.run_index_count = 0.22
        self.melee_index_count = 0.15
        self.range_index_count = 0.08
        self.bullet_index_count = 0.1
        self.bullet_loop_count = 0
        self.melee_order = 0
        self.range_order = 0

    def health_bar(self):
        #Display health bar + lives
        black_colour = (0, 0, 0)
        green_colour = (0, 255, 0)
        self.lives_image = pygame.transform.scale(self.lives_image, (40, 40))
        pygame.draw.rect(screen, green_colour, pygame.Rect(35, 30, self.health * 2.5, 40))
        pygame.draw.rect(screen, black_colour, pygame.Rect(35, 30, 250, 40), 4)
        if self.lives == 3:
            self.lives_rect_1 = self.lives_image.get_rect(topleft = (305, 30))
            self.lives_rect_2 = self.lives_image.get_rect(topleft = (355, 30))
            self.lives_rect_3 = self.lives_image.get_rect(topleft = (405, 30))
            screen.blit(self.lives_image, self.lives_rect_1)
            screen.blit(self.lives_image, self.lives_rect_2)
            screen.blit(self.lives_image, self.lives_rect_3)
        elif self.lives == 2:
            self.lives_rect_1 = self.lives_image.get_rect(topleft = (305, 30))
            self.lives_rect_2 = self.lives_image.get_rect(topleft = (355, 30))
            screen.blit(self.lives_image, self.lives_rect_1)
            screen.blit(self.lives_image, self.lives_rect_2)
        elif self.lives == 1:
            self.lives_rect = self.lives_image.get_rect(topleft = (305, 30))
            screen.blit(self.lives_image, self.lives_rect)

    def jump(self):
        #Timer not reached 0 + avatars still alive
        if elapsed_time < 300 and self.lives > 0 and enyo_object.lives > 0:
            
            #Initiate jump + sound effect
            keys = pygame.key.get_pressed()
            if P_1_Eris and self.health > 0:
                if keys[ord('w')] and self.y_pos == 690 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 505 and self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 505 and self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 320 and self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
            elif P_2_Eris and self.health > 0:
                if keys[pygame.K_UP] and self.y_pos == 690 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 505 and self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 505 and self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 320 and self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                    
            #Apply gravity
            if self.jump_state:
                self.gravity += 0.5
                self.y_pos += self.gravity
                
            #Platform + ground floor conditions
            if self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and self.y_pos >= 505 and self.y_pos <= 525 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.bottom_platform = True
            elif self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and self.y_pos >= 505 and self.y_pos <= 525 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.bottom_platform = True
            elif self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and self.y_pos >= 320 and self.y_pos <= 330 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.top_platform = True
            if self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and self.y_pos >= 505 and self.bottom_platform:
                self.y_pos = 505
            elif self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and self.y_pos >= 505 and self.bottom_platform:
                self.y_pos = 505
            elif self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and self.y_pos >= 320 and self.top_platform:
                self.y_pos = 320
            elif self.y_pos >= 690:
                self.y_pos = 690
                self.jump_state = False
                self.top_platform = False
                self.bottom_platform = False
            else:
                self.jump_state = True
                self.bottom_platform = False
                self.top_platform = False
            self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))
    
    def animation_movement_state(self):
        if elapsed_time < 300 and self.lives > 0 and enyo_object.lives > 0:
            
            #Initiate melee + range attack
            keys = pygame.key.get_pressed()
            if P_1_Eris:
                if keys[ord('r')]:
                    self.melee_state = True
                if keys[ord('t')] and not self.bullet_state:
                    self.range_state = True
            if P_2_Eris:
                if keys[ord('n')]:
                    self.melee_state = True
                if keys[ord('m')] and not self.bullet_state:
                    self.range_state = True
            if not self.range_state and self.melee_state:
                self.melee_order = 1
            elif not self.melee_state and self.range_state:
                self.range_order = 1
            elif self.range_state and self.melee_state and self.melee_order != 1 and self.range_order != 1:
                self.range_order = 1

            #Respawn if dead + decrease lives
            if self.health <= 0:
                if self.lives != 1:
                    self.respawn_index += 0.015
                    self.x_pos = 100
                    self.y_pos = 690
                    self.image = self.respawn_right[int(self.respawn_index)]
                    if self.image == self.respawn_right[3]:
                        self.health = 100
                        self.respawn_index = 0
                        self.lives -= 1
                        print(self.lives)
                    self.image = pygame.transform.scale(self.image, (80, 100))
                else:
                    self.lives = 0

            #Jumping conditions
            elif self.jump_state:
                
                #Move left, right, or stand still & play sound effect while melee animation runs mid-air
                if self.melee_order == 1:
                    if self.melee_index == 0:
                        self.sword_effect.play()
                    if P_1_Eris:
                        if keys[ord('d')]:
                            if keys[ord('d')] and keys[ord('a')]:
                                self.x_pos += 0
                            elif keys[ord('d')]:
                                self.x_pos += 9
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                            self.right = True
                            self.left = False
                        elif keys[ord('a')]:
                            self.x_pos -= 9
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                            self.right = False
                            self.left = True
                        elif self.right:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                        elif self.left:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                        self.image = pygame.transform.scale(self.image, (100, 110))
                    elif P_2_Eris:
                        if keys[pygame.K_RIGHT]:
                            if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                                self.x_pos += 0
                            elif keys[pygame.K_RIGHT]:
                                self.x_pos += 9
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                            self.right = True
                            self.left = False
                        elif keys[pygame.K_LEFT]:
                            self.x_pos -= 9
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                            self.right = False
                            self.left = True
                        elif self.right:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                        elif self.left:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                        self.image = pygame.transform.scale(self.image, (100, 110))
                        
                #Stand still & play sound effect while long range animation runs mid-air
                elif self.range_order == 1:
                    if self.range_index == 0:
                        self.long_range_effect.play()
                    if self.range_index == 0:
                        self.bullet_state = True
                    if self.right:
                        self.range_index += self.range_index_count
                        if self.range_index >= len(self.range_right):
                            self.range_index = 0
                            self.range_order = 0
                            self.range_state = False
                        self.image = self.range_right[int(self.range_index)]
                    elif self.left:
                        self.range_index += self.range_index_count
                        if self.range_index >= len(self.range_left):
                            self.range_index = 0
                            self.range_order = 0
                            self.range_state = False
                        self.image = self.range_left[int(self.range_index)]
                    if self.image == self.range_left[0] or self.image == self.range_right[0]:
                        self.image = pygame.transform.scale(self.image, (79, 100))
                    elif self.image == self.range_left[1] or self.image == self.range_right[1]:
                        self.image = pygame.transform.scale(self.image, (126, 100))
                    elif self.image == self.range_left[2] or self.image == self.range_right[2]:
                        self.image = pygame.transform.scale(self.image, (126, 100))
                    elif self.image == self.range_left[3] or self.image == self.range_right[3]:
                        self.image = pygame.transform.scale(self.image, (110, 100))

                #Run jumping animation while moving right + left
                elif keys[ord('d')] and P_1_Eris:
                    if keys[ord('d')] and keys[ord('a')]:
                        self.x_pos += 0
                    else:
                        self.x_pos += 9
                    if self.gravity <= -9:
                        self.image = self.jump_right[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_right[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_right[3]
                    else:
                        self.image = self.jump_right[4]
                    self.right = True
                    self.left = False
                elif keys[ord('a')] and P_1_Eris:
                    self.x_pos -= 9
                    if self.gravity <= -9:
                        self.image = self.jump_left[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_left[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_left[3]
                    else:
                        self.image = self.jump_left[4]
                    self.right = False
                    self.left = True
                elif keys[pygame.K_RIGHT] and P_2_Eris:
                    if [pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                        self.x_pos += 0
                    else:
                        self.x_pos += 9
                    if self.gravity <= -9:
                        self.image = self.jump_right[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_right[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_right[3]
                    else:
                        self.image = self.jump_right[4]
                    self.right = True
                    self.left = False
                elif keys[pygame.K_LEFT] and P_2_Eris:
                    self.x_pos -= 9
                    if self.gravity <= -9:
                        self.image = self.jump_left[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_left[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_left[3]
                    else:
                        self.image = self.jump_left[4]
                    self.right = False
                    self.left = True

                #Run jumping animation while standing still
                elif self.right:
                    if self.gravity <= -9:
                        self.image = self.jump_right[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_right[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_right[3]
                    else:
                        self.image = self.jump_right[4]
                elif self.left:
                    if self.gravity <= -9:
                        self.image = self.jump_left[0]
                    elif self.gravity <= -3:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 3:
                        self.image = self.jump_left[2]
                    elif self.gravity <= 9:
                        self.image = self.jump_left[3]
                    else:
                        self.image = self.jump_left[4]
                if not self.melee_state and not self.range_state:
                    self.image = pygame.transform.scale(self.image, (85, 100))

            #Melee animation, movement & sound effect when not jumping
            elif self.melee_order == 1:
                if self.melee_index == 0:
                    self.sword_effect.play()
                if P_1_Eris:
                    if keys[ord('d')]:
                        if keys[ord('d')] and keys[ord('a')]:
                            self.x_pos += 0
                        elif keys[ord('d')]:
                            self.x_pos += 9
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                        self.right = True
                        self.left = False
                    elif keys[ord('a')]:
                        self.x_pos -= 9
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                        self.right = False
                        self.left = True
                    elif self.right:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                    elif self.left:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                    self.image = pygame.transform.scale(self.image, (100, 110))
                elif P_2_Eris:
                    if keys[pygame.K_RIGHT]:
                        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                            self.x_pos += 0
                        elif keys[pygame.K_RIGHT]:
                            self.x_pos += 9
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                        self.right = True
                        self.left = False
                    elif keys[pygame.K_LEFT]:
                        self.x_pos -= 9
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                        self.right = False
                        self.left = True
                    elif self.right:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                    elif self.left:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                    self.image = pygame.transform.scale(self.image, (100, 110))

            #Long range animation & sound effect when not jumping
            elif self.range_order == 1:
                if self.range_index == 0:
                    self.long_range_effect.play()
                if self.range_index == 0:
                    self.bullet_state = True
                if self.right:
                    self.range_index += self.range_index_count
                    if self.range_index >= len(self.range_right):
                        self.range_index = 0
                        self.range_order = 0
                        self.range_state = False
                    self.image = self.range_right[int(self.range_index)]
                elif self.left:
                    self.range_index += self.range_index_count
                    if self.range_index >= len(self.range_left):
                        self.range_index = 0
                        self.range_order = 0
                        self.range_state = False
                    self.image = self.range_left[int(self.range_index)]
                if self.image == self.range_left[0] or self.image == self.range_right[0]:
                    self.image = pygame.transform.scale(self.image, (79, 100))
                elif self.image == self.range_left[1] or self.image == self.range_right[1]:
                    self.image = pygame.transform.scale(self.image, (126, 100))
                elif self.image == self.range_left[2] or self.image == self.range_right[2]:
                    self.image = pygame.transform.scale(self.image, (126, 100))
                elif self.image == self.range_left[3] or self.image == self.range_right[3]:
                    self.image = pygame.transform.scale(self.image, (110, 100))

            #Running left and right animation when not jumping
            elif keys[ord('d')] and P_1_Eris:
                if [ord('d')] and keys[ord('a')]:
                    self.x_pos += 0
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))
                else:
                    self.x_pos += 9
                    self.run_right_index += self.run_index_count
                    if self.run_right_index >= len(self.run_right):
                        self.run_right_index = 0
                        self.run_right.reverse()
                    self.image = self.run_right[int(self.run_right_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = True
                self.left = False
            elif keys[ord('a')] and P_1_Eris:
                self.x_pos -= 9
                self.run_left_index += self.run_index_count
                if self.run_left_index >= len(self.run_left):
                    self.run_left_index = 0
                    self.run_left.reverse()
                self.image = self.run_left[int(self.run_left_index)]
                self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = False
                self.left = True
            elif keys[pygame.K_RIGHT] and P_2_Eris:
                if [pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                    self.x_pos += 0
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))
                else:
                    self.x_pos += 9
                    self.run_right_index += self.run_index_count
                    if self.run_right_index >= len(self.run_right):
                        self.run_right_index = 0
                        self.run_right.reverse()
                    self.image = self.run_right[int(self.run_right_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = True
                self.left = False
            elif keys[pygame.K_LEFT] and P_2_Eris:
                self.x_pos -= 9
                self.run_left_index += self.run_index_count
                if self.run_left_index >= len(self.run_left):
                    self.run_left_index = 0
                    self.run_left.reverse()
                self.image = self.run_left[int(self.run_left_index)]
                self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = False
                self.left = True

            #Standing animation
            else:
                if self.right:
                    self.image = self.stand[1]
                elif self.left:
                    self.image = self.stand[0]
                self.image = pygame.transform.scale(self.image, (75, 100))

            #Bullet animation
            if self.bullet_state:
                if self.bullet_index == 0 and self.bullet_loop_count == 0:
                    if self.right:
                        self.bullet_direction = True
                        self.bullet_x_pos = self.x_pos + 27
                        self.bullet_y_pos = self.y_pos - 77
                    else:
                        self.bullet_direction = False
                        self.bullet_x_pos = self.x_pos - 98
                        self.bullet_y_pos = self.y_pos - 77
                self.bullet_index += self.bullet_index_count
                if self.bullet_index >= len(self.bullet) or self.bullet_x_pos - 15 > 1300 or self.bullet_x_pos + 15 < 0:
                    self.bullet_index = 0
                    self.bullet_loop_count = 0
                    self.bullet_state = False
                self.bullet_image = self.bullet[int(self.bullet_index)]
                if self.bullet_image == self.bullet[0]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (25, 25))
                elif self.bullet_image == self.bullet[1]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (35, 25))
                elif self.bullet_image == self.bullet[2]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (27, 35))
                elif self.bullet_image == self.bullet[3]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (30, 30))
                elif self.bullet_image == self.bullet[4]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (35, 35))
                elif self.bullet_image == self.bullet[5]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (25, 25))
                elif self.bullet_image == self.bullet[6]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (12, 12))
                elif self.bullet_image == self.bullet[7]:
                    self.bullet_image = pygame.transform.scale(self.bullet_image, (7, 7))
                if self.bullet_direction:
                    self.bullet_x_pos += 10
                else:
                    self.bullet_x_pos -= 10

            #Screen boundary conditions
            if self.range_state and self.range_order == 1 and self.x_pos - 103 < 0:
                self.x_pos = 103
            if self.melee_state and self.melee_order == 1 and self.x_pos - 100 < 0:
                self.x_pos = 100
            if self.jump_state and self.x_pos - 85 < 0:
                self.x_pos = 85
            if self.x_pos - 75 < 0:
                self.x_pos = 75
                self.image = self.stand[0]
                self.image = pygame.transform.scale(self.image, (75, 100))
            if self.range_state and self.range_order == 1 and self.x_pos + 29 > 1300:
                self.x_pos = 1271
            if self.x_pos > 1300:
                self.x_pos = 1300
                if not self.jump_state and not self.melee_state:
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))

            #Position avatar based on its movement type
            if self.range_state and self.range_order == 1:
                if self.left:
                    self.rect = self.image.get_rect(bottomright = (self.x_pos - 25, self.y_pos))
                else:
                    self.rect = self.image.get_rect(bottomleft = (self.x_pos - 50, self.y_pos))
            else:
                self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))

        #Display avatar + bullet
        screen.blit(self.image, self.rect)
        if self.bullet_state:
            self.bullet_rect = self.bullet_image.get_rect(center = (self.bullet_x_pos, self.bullet_y_pos))
            screen.blit(self.bullet_image, self.bullet_rect)
                
    def update(self):
        self.health_bar()
        self.jump()
        self.animation_movement_state()

class Enyo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        stand_left = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-stand-left.png').convert_alpha()
        stand_right = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-stand-right.png').convert_alpha()
        run_left_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_1-left.png').convert_alpha()
        run_left_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_2-left.png').convert_alpha()
        run_left_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_3-left.png').convert_alpha()
        run_right_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_1-right.png').convert_alpha()
        run_right_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_2-right.png').convert_alpha()
        run_right_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Stand_+_Run/av_3-run_3-right.png').convert_alpha()
        jump_left_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_2-left.png').convert_alpha()
        jump_left_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_1-left.png').convert_alpha()
        jump_left_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_3-left.png').convert_alpha()
        jump_left_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_4-left.png').convert_alpha()
        jump_right_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_2-right.png').convert_alpha()
        jump_right_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_1-right.png').convert_alpha()
        jump_right_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_3-right.png').convert_alpha()
        jump_right_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Jump/av_3-jump_4-right.png').convert_alpha()
        respawn_right_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_1-right.png').convert_alpha()
        respawn_right_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_2-right.png').convert_alpha()
        respawn_right_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_3-right.png').convert_alpha()
        respawn_left_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_1-left.png').convert_alpha()
        respawn_left_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_2-left.png').convert_alpha()
        respawn_left_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Respawn/av_3-respawn_3-left.png').convert_alpha()
        melee_left_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_1-left.png').convert_alpha()
        melee_left_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_2-left.png').convert_alpha()
        melee_left_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_3-left.png').convert_alpha()
        melee_left_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_4-left.png').convert_alpha()
        melee_left_5 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_5-left.png').convert_alpha()
        melee_right_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_1-right.png').convert_alpha()
        melee_right_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_2-right.png').convert_alpha()
        melee_right_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_3-right.png').convert_alpha()
        melee_right_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_4-right.png').convert_alpha()
        melee_right_5 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Melee/av_3-melee_5-right.png').convert_alpha()
        range_left_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_1_7-left.png').convert_alpha()
        range_left_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_2-left.png').convert_alpha()
        range_left_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_3-left.png').convert_alpha()
        range_left_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_4-left.png').convert_alpha()
        range_left_5 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_5-left.png').convert_alpha()
        range_left_6 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_6-left.png').convert_alpha()
        range_left_7 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_1_7-left.png').convert_alpha()
        range_right_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_1_7-right.png').convert_alpha()
        range_right_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_2-right.png').convert_alpha()
        range_right_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_3-right.png').convert_alpha()
        range_right_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_4-right.png').convert_alpha()
        range_right_5 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_5-right.png').convert_alpha()
        range_right_6 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_6-right.png').convert_alpha()
        range_right_7 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-range_1_7-right.png').convert_alpha()
        bullet_left = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-bullet-left.png').convert_alpha()
        bullet_right = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Long_Range/av_3-bullet-right.png').convert_alpha()
        explosion_1 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_1.png').convert_alpha()
        explosion_2 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_2.png').convert_alpha()
        explosion_3 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_3.png').convert_alpha()
        explosion_4 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_4.png').convert_alpha()
        explosion_5 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_5.png').convert_alpha()
        explosion_6 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_6.png').convert_alpha()
        explosion_7 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_7.png').convert_alpha()
        explosion_8 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_8.png').convert_alpha()
        explosion_9 = pygame.image.load('Sprites/Enyo_God_of_the_Underworld/Explosion_Animation/av_3-explosion_9.png').convert_alpha()
        heart_lives = pygame.image.load('Sprites/Game_Environment/heart_lives.png').convert_alpha()
        self.jump_effect = pygame.mixer.Sound('Sprites/Game_Environment/jump-sound.wav')
        self.melee_effect = pygame.mixer.Sound('Sprites/Game_Environment/melee-sound.wav')
        self.melee_effect.set_volume(3)
        self.long_range_effect = pygame.mixer.Sound('Sprites/Game_Environment/enyo-long_range-sound.wav')
        self.long_range_effect.set_volume(2.7)

        self.stand = [stand_left, stand_right]
        self.run_left = [run_left_1, run_left_2, run_left_3]
        self.run_left_index = 0
        self.run_right = [run_right_1, run_right_2, run_right_3]
        self.run_right_index = 0
        self.jump_left = [jump_left_1, jump_left_2, jump_left_3, jump_left_4]
        self.jump_left_index = 0
        self.jump_right = [jump_right_1, jump_right_2, jump_right_3, jump_right_4]
        self.jump_right_index = 0
        self.respawn_left = [respawn_left_1, respawn_left_2, respawn_left_3, stand_left]
        self.respawn_right = [respawn_right_1, respawn_right_2, respawn_right_3, stand_right, stand_right]
        self.respawn_index = 0
        self.melee_left = [melee_left_1, melee_left_2, melee_left_3, melee_left_4, melee_left_5]
        self.melee_right = [melee_right_1, melee_right_2, melee_right_3, melee_right_4, melee_right_5]
        self.melee_index = 0
        self.range_left = [range_left_1, range_left_2, range_left_3, range_left_4, range_left_5, range_left_6, range_left_7]
        self.range_right = [range_right_1, range_right_2, range_right_3, range_right_4, range_right_5, range_right_6, range_right_7]
        self.range_index = 0
        self.bullet = [bullet_left, bullet_right]
        self.bullet_index = 0
        self.explosion = [explosion_1, explosion_2, explosion_3, explosion_4, explosion_5, explosion_6, explosion_7, explosion_8, explosion_9]
        self.explosion_index = 0
        self.lives_image = heart_lives

        self.x_pos = 1200
        self.y_pos = 690
        self.bullet_x_pos = 1200
        self.bullet_y_pos = 690
        self.image = stand_left
        self.right = False
        self.left = True
        self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))
        screen.blit(self.image, self.rect)
        self.bullet_image = self.bullet[0]
        self.bullet_rect = self.bullet_image.get_rect(center = (self.bullet_x_pos, self.bullet_y_pos))

        self.jump_state = False
        self.melee_state = False
        self.range_state = False
        self.bullet_state = False
        self.bullet_direction = False
        self.top_platform = False
        self.bottom_platform = False
        self.gravity = 0
        self.health = 100
        self.lives = 3
        self.run_index_count = 0.1
        self.melee_index_count = 0.1
        self.range_index_count = 0.08
        self.bullet_loop_count = 0
        self.melee_order = 0
        self.range_order = 0
        self.bullet_gravity = -20

    def health_bar(self):
        black_colour = (0, 0, 0)
        green_colour = (0, 255, 0)
        self.lives_image = pygame.transform.scale(self.lives_image, (40, 40))

        pygame.draw.rect(screen, green_colour, pygame.Rect(1015, 30, self.health * 2.5, 40))
        pygame.draw.rect(screen, black_colour, pygame.Rect(1015, 30, 250, 40), 4)
        if self.lives == 3:
            self.lives_rect_1 = self.lives_image.get_rect(topleft = (855, 30))
            self.lives_rect_2 = self.lives_image.get_rect(topleft = (905, 30))
            self.lives_rect_3 = self.lives_image.get_rect(topleft = (955, 30))
            screen.blit(self.lives_image, self.lives_rect_1)
            screen.blit(self.lives_image, self.lives_rect_2)
            screen.blit(self.lives_image, self.lives_rect_3)
        elif self.lives == 2:
            self.lives_rect_1 = self.lives_image.get_rect(topleft = (855, 30))
            self.lives_rect_2 = self.lives_image.get_rect(topleft = (905, 30))
            screen.blit(self.lives_image, self.lives_rect_1)
            screen.blit(self.lives_image, self.lives_rect_2)
        elif self.lives == 1:
            self.lives_rect = self.lives_image.get_rect(topleft = (855, 30))
            screen.blit(self.lives_image, self.lives_rect)

    def jump(self):
        if elapsed_time < 300 and self.lives > 0 and eris_object.lives > 0:
            keys = pygame.key.get_pressed()
            if P_1_Enyo and self.health > 0:
                if keys[ord('w')] and self.y_pos == 690 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 505 and self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 505 and self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[ord('w')] and self.y_pos == 320 and self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
            elif P_2_Enyo and self.health > 0:
                if keys[pygame.K_UP] and self.y_pos == 690 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 505 and self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 505 and self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                elif keys[pygame.K_UP] and self.y_pos == 320 and self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and not self.jump_state:
                    self.gravity = -15
                    self.jump_state = True
                    self.jump_effect.play()
                    
            if self.jump_state:
                self.gravity += 0.5
                self.y_pos += self.gravity
                
            if self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and self.y_pos >= 505 and self.y_pos <= 525 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.bottom_platform = True
            elif self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and self.y_pos >= 505 and self.y_pos <= 525 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.bottom_platform = True
            elif self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and self.y_pos >= 320 and self.y_pos <= 330 and self.jump_state and self.gravity > 5:
                self.jump_state = False
                self.top_platform = True
            if self.x_pos - 20 >= 250 and self.x_pos - 57 <= 500 and self.y_pos >= 505 and self.bottom_platform:
                self.y_pos = 505
            elif self.x_pos - 20 >= 800 and self.x_pos - 57 <= 1050 and self.y_pos >= 505 and self.bottom_platform:
                self.y_pos = 505
            elif self.x_pos - 20 >= 425 and self.x_pos - 57 <= 875 and self.y_pos >= 320 and self.top_platform:
                self.y_pos = 320
            elif self.y_pos >= 690:
                self.y_pos = 690
                self.jump_state = False
                self.top_platform = False
                self.bottom_platform = False
            else:
                self.jump_state = True
                self.bottom_platform = False
                self.top_platform = False
            self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))
    
    def animation_movement_state(self):
        if elapsed_time < 300 and self.lives > 0 and eris_object.lives > 0:
            keys = pygame.key.get_pressed()
            if P_1_Enyo:
                if keys[ord('r')]:
                    self.melee_state = True
                if keys[ord('t')] and not self.bullet_state:
                    self.range_state = True
            if P_2_Enyo:
                if keys[ord('n')]:
                    self.melee_state = True
                if keys[ord('m')] and not self.bullet_state:
                    self.range_state = True
            if not self.range_state and self.melee_state:
                self.melee_order = 1
            elif not self.melee_state and self.range_state:
                self.range_order = 1
            elif self.range_state and self.melee_state and self.melee_order != 1 and self.range_order != 1:
                self.range_order = 1

            if self.health <= 0:
                if self.lives != 1:
                    self.respawn_index += 0.015
                    self.x_pos = 1200
                    self.y_pos = 690
                    self.image = self.respawn_left[int(self.respawn_index)]
                    if self.image == self.respawn_left[3]:
                        self.health = 100
                        self.respawn_index = 0
                        self.lives -= 1
                    self.image = pygame.transform.scale(self.image, (80, 100))
                else:
                    self.lives = 0

            elif self.jump_state:
                if self.melee_order == 1:
                    if self.melee_index == 0:
                        self.melee_effect.play()
                    if P_1_Enyo:
                        if keys[ord('d')]:
                            if keys[ord('d')] and keys[ord('a')]:
                                self.x_pos += 0
                            elif keys[ord('d')]:
                                self.x_pos += 5
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                            self.right = True
                            self.left = False
                        elif keys[ord('a')]:
                            self.x_pos -= 5
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                            self.right = False
                            self.left = True
                        elif self.right:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                        elif self.left:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                        self.image = pygame.transform.scale(self.image, (85, 100))
                    elif P_2_Enyo:
                        if keys[pygame.K_RIGHT]:
                            if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                                self.x_pos += 0
                            elif keys[pygame.K_RIGHT]:
                                self.x_pos += 5
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                            self.right = True
                            self.left = False
                        elif keys[pygame.K_LEFT]:
                            self.x_pos -= 5
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                            self.right = False
                            self.left = True
                        elif self.right:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_right):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_right[int(self.melee_index)]
                        elif self.left:
                            self.melee_index += self.melee_index_count
                            if self.melee_index >= len(self.melee_left):
                                self.melee_index = 0
                                self.melee_order = 0
                                self.melee_state = False
                            self.image = self.melee_left[int(self.melee_index)]
                        self.image = pygame.transform.scale(self.image, (85, 100))
                        
                elif self.range_order == 1:
                    if self.range_index == 0:
                        self.long_range_effect.play()
                    if self.range_index == 0:
                        self.bullet_state = True
                    if self.right:
                        self.range_index += self.range_index_count
                        if self.range_index >= len(self.range_right):
                            self.range_index = 0
                            self.range_order = 0
                            self.range_state = False
                        self.image = self.range_right[int(self.range_index)]
                    elif self.left:
                        self.range_index += self.range_index_count
                        if self.range_index >= len(self.range_left):
                            self.range_index = 0
                            self.range_order = 0
                            self.range_state = False
                        self.image = self.range_left[int(self.range_index)]
                    if self.image == self.range_left[0] or self.image == self.range_right[0]:
                        self.image = pygame.transform.scale(self.image, (80, 120))
                    elif self.image == self.range_left[1] or self.image == self.range_right[1]:
                        self.image = pygame.transform.scale(self.image, (80, 120))
                    elif self.image == self.range_left[2] or self.image == self.range_right[2]:
                        self.image = pygame.transform.scale(self.image, (80, 130))
                    elif self.image == self.range_left[3] or self.image == self.range_right[3]:
                        self.image = pygame.transform.scale(self.image, (80, 137))
                    elif self.image == self.range_left[4] or self.image == self.range_right[4]:
                        self.image = pygame.transform.scale(self.image, (80, 130))
                    elif self.image == self.range_left[5] or self.image == self.range_right[5]:
                        self.image = pygame.transform.scale(self.image, (80, 130))
                    elif self.image == self.range_left[6] or self.image == self.range_right[6]:
                        self.image = pygame.transform.scale(self.image, (80, 110))
                    elif self.image == self.range_left[7] or self.image == self.range_right[7]:
                        self.image = pygame.transform.scale(self.image, (80, 110))

                elif keys[ord('d')] and P_1_Enyo:
                    if keys[ord('d')] and keys[ord('a')]:
                        self.x_pos += 0
                    else:
                        self.x_pos += 5
                    if self.gravity <= -7:
                        self.image = self.jump_right[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_right[2]
                    else:
                        self.image = self.jump_right[3]
                    self.right = True
                    self.left = False
                elif keys[ord('a')] and P_1_Enyo:
                    self.x_pos -= 5
                    if self.gravity <= -7:
                        self.image = self.jump_left[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_left[2]
                    else:
                        self.image = self.jump_left[3]
                    self.right = False
                    self.left = True
                elif keys[pygame.K_RIGHT] and P_2_Enyo:
                    if [pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                        self.x_pos += 0
                    else:
                        self.x_pos += 5
                    if self.gravity <= -7:
                        self.image = self.jump_right[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_right[2]
                    else:
                        self.image = self.jump_right[3]
                    self.right = True
                    self.left = False
                elif keys[pygame.K_LEFT] and P_2_Enyo:
                    self.x_pos -= 5
                    if self.gravity <= -7:
                        self.image = self.jump_left[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_left[2]
                    else:
                        self.image = self.jump_left[3]
                    self.right = False
                    self.left = True

                elif self.right:
                    if self.gravity <= -7:
                        self.image = self.jump_right[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_right[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_right[2]
                    else:
                        self.image = self.jump_right[3]
                elif self.left:
                    if self.gravity <= -7:
                        self.image = self.jump_left[0]
                    elif self.gravity <= 0:
                        self.image = self.jump_left[1]
                    elif self.gravity <= 8:
                        self.image = self.jump_left[2]
                    else:
                        self.image = self.jump_left[3]
                if not self.melee_state and not self.range_state:
                    self.image = pygame.transform.scale(self.image, (90, 100))

            elif self.melee_order == 1:
                if self.melee_index == 0:
                    self.melee_effect.play()
                if P_1_Enyo:
                    if keys[ord('d')]:
                        if keys[ord('d')] and keys[ord('a')]:
                            self.x_pos += 0
                        elif keys[ord('d')]:
                            self.x_pos += 5
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                        self.right = True
                        self.left = False
                    elif keys[ord('a')]:
                        self.x_pos -= 5
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                        self.right = False
                        self.left = True
                    elif self.right:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                    elif self.left:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))
                elif P_2_Enyo:
                    if keys[pygame.K_RIGHT]:
                        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                            self.x_pos += 0
                        elif keys[pygame.K_RIGHT]:
                            self.x_pos += 5
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                        self.right = True
                        self.left = False
                    elif keys[pygame.K_LEFT]:
                        self.x_pos -= 5
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                        self.right = False
                        self.left = True
                    elif self.right:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_right):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_right[int(self.melee_index)]
                    elif self.left:
                        self.melee_index += self.melee_index_count
                        if self.melee_index >= len(self.melee_left):
                            self.melee_index = 0
                            self.melee_order = 0
                            self.melee_state = False
                        self.image = self.melee_left[int(self.melee_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))

            elif self.range_order == 1:
                if self.range_index == 0:
                    self.long_range_effect.play()
                if self.range_index == 0:
                    self.bullet_state = True
                if self.right:
                    self.range_index += self.range_index_count
                    if self.range_index >= len(self.range_right):
                        self.range_index = 0
                        self.range_order = 0
                        self.range_state = False
                    self.image = self.range_right[int(self.range_index)]
                elif self.left:
                    self.range_index += self.range_index_count
                    if self.range_index >= len(self.range_left):
                        self.range_index = 0
                        self.range_order = 0
                        self.range_state = False
                    self.image = self.range_left[int(self.range_index)]
                if self.image == self.range_left[0] or self.image == self.range_right[0]:
                    self.image = pygame.transform.scale(self.image, (80, 120))
                elif self.image == self.range_left[1] or self.image == self.range_right[1]:
                    self.image = pygame.transform.scale(self.image, (80, 120))
                elif self.image == self.range_left[2] or self.image == self.range_right[2]:
                    self.image = pygame.transform.scale(self.image, (80, 130))
                elif self.image == self.range_left[3] or self.image == self.range_right[3]:
                    self.image = pygame.transform.scale(self.image, (80, 137))
                elif self.image == self.range_left[4] or self.image == self.range_right[4]:
                    self.image = pygame.transform.scale(self.image, (80, 130))
                elif self.image == self.range_left[5] or self.image == self.range_right[5]:
                    self.image = pygame.transform.scale(self.image, (80, 130))
                elif self.image == self.range_left[6] or self.image == self.range_right[6]:
                    self.image = pygame.transform.scale(self.image, (80, 110))
                elif self.image == self.range_left[7] or self.image == self.range_right[7]:
                    self.image = pygame.transform.scale(self.image, (80, 110))
                

            elif keys[ord('d')] and P_1_Enyo:
                if [ord('d')] and keys[ord('a')]:
                    self.x_pos += 0
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))
                else:
                    self.x_pos += 5
                    self.run_right_index += self.run_index_count
                    if self.run_right_index >= len(self.run_right):
                        self.run_right_index = 0
                    self.image = self.run_right[int(self.run_right_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = True
                self.left = False
            elif keys[ord('a')] and P_1_Enyo:
                self.x_pos -= 5
                self.run_left_index += self.run_index_count
                if self.run_left_index >= len(self.run_left):
                    self.run_left_index = 0
                self.image = self.run_left[int(self.run_left_index)]
                self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = False
                self.left = True
            elif keys[pygame.K_RIGHT] and P_2_Enyo:
                if [pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                    self.x_pos += 0
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))
                else:
                    self.x_pos += 5
                    self.run_right_index += self.run_index_count
                    if self.run_right_index >= len(self.run_right):
                        self.run_right_index = 0

                    self.image = self.run_right[int(self.run_right_index)]
                    self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = True
                self.left = False
            elif keys[pygame.K_LEFT] and P_2_Enyo:
                self.x_pos -= 5
                self.run_left_index += self.run_index_count
                if self.run_left_index >= len(self.run_left):
                    self.run_left_index = 0
                self.image = self.run_left[int(self.run_left_index)]
                self.image = pygame.transform.scale(self.image, (85, 100))
                self.right = False
                self.left = True

            else:
                if self.right:
                    self.image = self.stand[1]
                elif self.left:
                    self.image = self.stand[0]
                self.image = pygame.transform.scale(self.image, (75, 100))

            if self.bullet_state: 
                if self.bullet_loop_count == 0:
                    if self.right:
                        self.bullet_direction = True
                        self.bullet_image = self.bullet[1]
                        self.bullet_x_pos = self.x_pos
                        self.bullet_y_pos = self.y_pos - 95
                    else:
                        self.bullet_direction = False
                        self.bullet_image = self.bullet[0]
                        self.bullet_x_pos = self.x_pos - 75
                        self.bullet_y_pos = self.y_pos - 100
                self.bullet_gravity += 0.7
                self.bullet_loop_count += 1
                if self.bullet_x_pos - 15 > 1300 or self.bullet_x_pos + 15 < 0 or self.bullet_y_pos >= 690:
                    self.bullet_loop_count = 0
                    self.bullet_state = False
                    self.bullet_gravity = -20
                if self.bullet_direction:
                    self.bullet_x_pos += 8
                else:
                    self.bullet_x_pos -= 8
                self.bullet_y_pos += self.bullet_gravity
                self.bullet_image = pygame.transform.scale(self.bullet_image, (40, 30))
                

            if self.range_state and self.range_order == 1 and self.x_pos - 105 < 0:
                self.x_pos = 105
            if self.melee_state and self.melee_order == 1 and self.x_pos - 85 < 0:
                self.x_pos = 85
            if self.jump_state and self.x_pos - 90 < 0:
                self.x_pos = 90
            if self.x_pos - 75 < 0:
                self.x_pos = 75
                self.image = self.stand[0]
                self.image = pygame.transform.scale(self.image, (75, 100))
            if self.range_state and self.range_order == 1 and self.x_pos + 30 > 1300:
                self.x_pos = 1270
            if self.x_pos > 1300:
                self.x_pos = 1300
                if not self.jump_state and not self.melee_state:
                    self.image = self.stand[1]
                    self.image = pygame.transform.scale(self.image, (75, 100))

            if self.range_state and self.range_order == 1:
                if self.left:
                    self.rect = self.image.get_rect(bottomright = (self.x_pos - 25, self.y_pos))
                else:
                    self.rect = self.image.get_rect(bottomleft = (self.x_pos - 50, self.y_pos))
            else:
                self.rect = self.image.get_rect(bottomright = (self.x_pos, self.y_pos))

        screen.blit(self.image, self.rect)
        if self.bullet_state:
            self.bullet_rect = self.bullet_image.get_rect(center = (self.bullet_x_pos, self.bullet_y_pos))
            screen.blit(self.bullet_image, self.bullet_rect)
                
    def update(self):
        self.health_bar()
        self.jump()
        self.animation_movement_state()

#Deal damage when bullet/melee attack hits opponent   
def collision(object_1, object_2):
    if object_1.range_order == 1:
        if object_1.bullet_rect.colliderect(object_2.rect) and object_2.health > 0:
            object_2.health -= 0.4
            if object_2.health < 0:
                object_2.health = 0
    if object_1.melee_order == 1:
        if object_1.rect.colliderect(object_2.rect) and object_2.health > 0:
            object_2.health -= 0.15
            if object_2.health < 0:
                object_2.health = 0
    if object_2.range_order == 1:
        if object_2.bullet_rect.colliderect(object_1.rect) and object_1.health > 0:
            object_1.health -= 0.34
            if object_1.health < 0:
                object_1.health = 0
    if object_2.melee_order == 1:
        if object_2.rect.colliderect(object_1.rect) and object_1.health > 0:
            object_1.health -= 0.2
            if object_1.health < 0:
                object_1.health = 0
        
#Basic initializations
pygame.init()
screen = pygame.display.set_mode((1300, 725))
pygame.display.set_caption('The Titanomachy')
clock = pygame.time.Clock()
game_font = pygame.font.Font('Sprites/Game_Environment/game_font.ttf', 100)
transparency_amount = 0
loop_count = 0
sound_loop_count = 0
elapsed_time = 0
main_menu_active = True
instruction_menu_active = False
choose_avatar_active = False
game_active = False
end_game_active = False
P_1_Eris = True
P_2_Eris = False
P_1_Enyo = False
P_2_Enyo = True
fade_to_dark = False

#Create instances + group avatars
avatar_group = pygame.sprite.Group()
eris_object = Eris()
enyo_object = Enyo()
avatar_group.add(eris_object)
avatar_group.add(enyo_object)

#Background + platform + countdown + title images
countdown_1 = pygame.image.load('Sprites/Game_Environment/countdown-1.png')
countdown_2 = pygame.image.load('Sprites/Game_Environment/countdown-2.png')
countdown_3 = pygame.image.load('Sprites/Game_Environment/countdown-3.png')
countdown_4 = pygame.image.load('Sprites/Game_Environment/countdown-4.png')
countdown_5 = pygame.image.load('Sprites/Game_Environment/countdown-5.png')
game_sign_image = pygame.image.load('Sprites/Game_Environment/game_over.png')
main_menu_background = pygame.image.load('Sprites/Game_Environment/main-menu-background.png')
instruction_menu_background = pygame.image.load('Sprites/Game_Environment/instruction-menu-background.png')
choose_avatar_background = pygame.image.load('Sprites/Game_Environment/choose-avatar-background.png')
game_background = pygame.image.load('Sprites/Game_Environment/universe-background.png')
tie_background = pygame.image.load('Sprites/Game_Environment/end-menu-tie_background.png')
eris_win_background = pygame.image.load('Sprites/Game_Environment/end-menu-eris_background.png')
enyo_win_background = pygame.image.load('Sprites/Game_Environment/end-menu-enyo_background.png')
platform_1_image = pygame.image.load('Sprites/Game_Environment/platform_1.png')
platform_2_image = pygame.image.load('Sprites/Game_Environment/platform_1.png')
platform_1_image = pygame.transform.scale(platform_1_image, (250, 15))
platform_2_image = pygame.transform.scale(platform_2_image, (450, 20))
platform_rect_1 = platform_1_image.get_rect(bottomleft = (250, 520))
platform_rect_2 = platform_1_image.get_rect(bottomleft = (800, 520))
platform_rect_3 = platform_2_image.get_rect(bottomleft = (425, 340))

#Background music + game over sound effect
background_music = pygame.mixer.Sound('Sprites/Game_Environment/background-music.mp3')
background_music.set_volume(0.5)
background_music.play(loops = -1)
game_over_effect = pygame.mixer.Sound('Sprites/Game_Environment/game-over-sound.wav')
game_over_effect.set_volume(4)

#Game loop
while True:
    
    #Check for exiting window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Check if player clicks on section of screen that moves them to next menu
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if main_menu_active and mouse_pos[0] >= 490 and mouse_pos[0] <= 810 and mouse_pos[1] >= 385 and mouse_pos[1] <= 480:
                main_menu_active = False
                instruction_menu_active = True
            elif instruction_menu_active and mouse_pos[0] >= 205 and mouse_pos[0] <= 1095 and mouse_pos[1] >= 542 and mouse_pos[1] <= 597:
                instruction_menu_active = False
                choose_avatar_active = True
            elif choose_avatar_active and mouse_pos[0] >= 25 and mouse_pos[0] <= 520 and mouse_pos[1] >= 280 and mouse_pos[1] <= 435:
                choose_avatar_active = False
                game_active = True
                P_1_Eris = True
                P_2_Eris = False
                P_1_Enyo = False
                P_2_Enyo = True
            elif choose_avatar_active and mouse_pos[0] >= 677 and mouse_pos[0] <= 1277 and mouse_pos[1] >= 285 and mouse_pos[1] <= 440:
                choose_avatar_active = False
                game_active = True
                P_1_Eris = False
                P_2_Eris = True
                P_1_Enyo = True
                P_2_Enyo = False
            elif end_game_active and mouse_pos[0] >= 288 and mouse_pos[0] <= 1013 and mouse_pos[1] >= 415 and mouse_pos[1] <= 502:
                end_game_active = False
                choose_avatar_active = True
                loop_count = 0
                avatar_group = pygame.sprite.Group()
                eris_object = Eris()
                enyo_object = Enyo()
                avatar_group.add(eris_object)
                avatar_group.add(enyo_object)
                fade_to_dark = False
                sound_loop_count = 0
                loop_count = 0
                transparency_amount = 0
                elapsed_time = 0

    #Display menus 
    if main_menu_active:
        pygame.mouse.set_visible(True)
        screen.blit(main_menu_background, (0, 0))
    elif instruction_menu_active:
        screen.blit(instruction_menu_background, (0, 0))
    elif choose_avatar_active:
        screen.blit(choose_avatar_background, (0, 0))

    elif game_active:
        pygame.mouse.set_visible(False)
        #When game is running
        if loop_count == 0 or loop_count >= 500:

            #Timer
            if loop_count == 0 or loop_count == 500:
                start_time = time.time()
            end_time = time.time()
            elapsed_time = end_time - start_time
            timer = 300 - elapsed_time
            if timer > 0:
                timer_minutes = timer // 60
                timer_seconds = str(timer / 60)[1:]
                timer_seconds = int(format(float(timer_seconds) / 1.666666667 * 100, '0,.0f'))
                timer_minutes = int(format(timer_minutes, '12,.0f'))
                if timer_seconds == 60:
                    timer_minutes += 1
                if timer_seconds > 0 and timer_seconds < 10:
                    timer_message = game_font.render(f'{timer_minutes}:0{timer_seconds}', False, (0, 0, 0))
                elif timer_seconds == 60 or timer_seconds == 0:
                    timer_message = game_font.render(f'{timer_minutes}:00', False, (0, 0, 0))
                else:
                    timer_message = game_font.render(f'{timer_minutes}:{timer_seconds}', False, (0, 0, 0))
            else:
                timer_message = game_font.render('0:00', False, (0, 0, 0))
            timer_message_rect = timer_message.get_rect(midtop = (645, 20))

            #Display everything to screen + update instances
            screen.blit(game_background, (0, 0))
            screen.blit(platform_1_image, platform_rect_1)
            screen.blit(platform_1_image, platform_rect_2)
            screen.blit(platform_2_image, platform_rect_3)
            screen.blit(timer_message, timer_message_rect)
            avatar_group.update()
            collision(eris_object, enyo_object)

            #Game over sound effect + text  
            if elapsed_time >= 300 or eris_object.lives == 0 or enyo_object.lives == 0:
                if sound_loop_count == 0:
                    game_over_effect.play()
                game_sign_image = pygame.transform.scale(game_sign_image, (500, 175))
                game_sign_rect = game_sign_image.get_rect(midtop = (645, 120))
                screen.blit(game_sign_image, game_sign_rect)
                sound_loop_count += 1
                
        else:
            #Countdown
            if loop_count <= 100:
                countdown_image = countdown_5
                countdown_image_rect = countdown_image.get_rect(midtop = (645, 120))
            elif loop_count <= 200:
                countdown_image = countdown_4
                countdown_image_rect = countdown_image.get_rect(midtop = (645, 225))
            elif loop_count <= 300:
                countdown_image = countdown_3
                countdown_image_rect = countdown_image.get_rect(midtop = (645, 350))
            elif loop_count <= 400:
                countdown_image = countdown_2
                countdown_image_rect = countdown_image.get_rect(midtop = (645, 460))
            else:
                countdown_image = countdown_1
                countdown_image_rect = countdown_image.get_rect(midtop = (645, 570))
            countdown_image = pygame.transform.scale(countdown_image, (85, 95))
            screen.blit(countdown_image, countdown_image_rect)
        loop_count += 1
        
    elif end_game_active:
        pygame.mouse.set_visible(True)
        #Displays winner or tie
        if enyo_object.lives == 0 and eris_object.lives > 0:
            screen.blit(eris_win_background, (0, 0))
        elif eris_object.lives == 0 and enyo_object.lives > 0:
            screen.blit(enyo_win_background, (0, 0))
        elif eris_object.lives > enyo_object.lives:
            screen.blit(eris_win_background, (0, 0))
        elif enyo_object.lives > eris_object.lives:
            screen.blit(enyo_win_background, (0, 0))
        elif enyo_object.lives == eris_object.lives:
            screen.blit(tie_background, (0, 0))

    #Fades game screen to end menu
    if transparency_amount >= 0:
        if elapsed_time >= 305 or eris_object.lives == 0 or enyo_object.lives == 0:
            if not fade_to_dark:
                transparency_amount += 1
            else:
                transparency_amount -= 1
            if transparency_amount >= 0 and transparency_amount <= 255:
                pygame.gfxdraw.box(screen, (0, 0, 1300, 725), (0, 0, 0, transparency_amount))
            if transparency_amount == 255:
                fade_to_dark = True
                game_active = False
                end_game_active = True
                
    pygame.display.update()
    clock.tick(100)
