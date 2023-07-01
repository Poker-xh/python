import sys

import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings =Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship=Ship(ai_settings,screen)
    bg_color = (230,230,230)
    bullets = Group()
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        #每次循环都会重绘屏幕
         #绘制屏幕可见
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
 
        gf.update_screen(ai_settings,screen,ship,bullets)


run_game()