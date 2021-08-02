import pygame
import random

class Character(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, scale, speed ) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image_path = image_path
        self.x = x
        self.y = y
        self.speed = speed
        self.character_image = pygame.image.load(image_path)
        self.character_image = pygame.transform.scale(self.character_image, 
                                        (
                                            int(self.character_image.get_width() * scale) , 
                                            int(self.character_image.get_height() * scale)
                                        )
                                    )
        self.character_rect = self.character_image.get_rect()
        self.character_rect.center = (x,y)

    def move_x(self, moving_left, moving_right):
        dx = 0
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed

        self.character_rect.x += dx
        if self.character_rect.x >= 400:
            self.character_rect = 400           
        elif self.character_rect.x <= 0:
            self.character_rect.x = 0

         

    def move_y(self, moving_up, moving_down):
        dy = 0

        if moving_up:
            dy = -self.speed
        else: 
            dy = self.speed
        self.character_rect.y += dy


    def draw(self, screen):
        screen.blit(self.character_image, self.character_rect)

    def fire(self, screen):
        screen.blit(self.character_image, self.character_rect)
        dy = -self.speed
        self.character_rect.y += dy

    def spawn(self):
        enemy_img = pygame.image.load("image/enemy.png")
        enemy_rect = enemy_img.get_rect()
        enemy_rect.center = (random.randint(0,736), random.randint(5,15))
        self.character_image = enemy_img
        self.character_rect = enemy_rect
        self.draw()

    def move_enemy(self): 
        bullet_hit = False 
        while True:
            self.move_x(True, False)
            enemy_xchange = 0.3
            enemy_ychange = 5
            if self.character_rect.x <= 0:
                self.character_rect.x += enemy_xchange
                self.character_rect.y += enemy_ychange
                self.move_x(False, True)
            elif self.character_rect.x >= 480:
                self.character_rect.x -= enemy_xchange
                self.character_rect.y += enemy_ychange
                self.move_x(True, False)


