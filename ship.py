#coding=gbk
import pygame

class Ship():
    def __init__(self, ai_settings, screen):  # 1
        self.screen = screen
        self.ai_settings = ai_settings  # 2

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()   # rect 是 image的dimension
        self.screen_rect = screen.get_rect() # screen_rect 是屏幕的dimension
        ''' 如果这里是self.rect.centerx，那么飞船就在最左边。如果是self.screen_rect.centerx
        那么飞船就在中间'''
        self.center = float(self.screen_rect.centerx)  
        self.y = float(self.screen_rect.bottom - self.rect.bottom)

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor  # 4
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center  # 5
        self.rect.top = self.y
