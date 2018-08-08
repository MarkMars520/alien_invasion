# coding=gbk
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)  # 创建一艘飞船
    alien = Alien(ai_settings, screen)  # 创建外星人
    bullets = Group()  # 创建一个用于存储子弹的编组
    aliens = Group()  # 创建外星人组（空的编组）

    gf.create_fleet(ai_settings, screen, ship, aliens)  # 创建外星人群

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
