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

    ship = Ship(ai_settings, screen)  # ����һ�ҷɴ�
    alien = Alien(ai_settings, screen)  # ����������
    bullets = Group()  # ����һ�����ڴ洢�ӵ��ı���
    aliens = Group()  # �����������飨�յı��飩

    gf.create_fleet(ai_settings, screen, ship, aliens)  # ����������Ⱥ

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
