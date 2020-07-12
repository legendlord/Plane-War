import random

import pygame

#屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#刷新频率
FRAME_PRE_SEC = 120
#创建敌机的定时器
CREATE_ENEMY_EVENT = pygame.USEREVENT

#
ENEMY_SPEED_MAX = 5
ENEMY_SPEED_MIN = 1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    # 020-派生游戏精灵子类
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上向下移动
        self.rect.y += self.speed
        
        
class BackGround(GameSprite):
    """背景精灵"""
    def __init__(self, is_alt=False):
        super().__init__("D:/File/Python/Plane Wars/image/background.png")
        #如果是交替图像则设置于屏幕上方
        if is_alt:
            self.rect.y = -self.rect.height
            
    def update(self):
        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕，如果移出，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        
class Enemy(GameSprite):
    '''033-敌机精灵'''
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("D:/File/Python/Plane Wars/image/enemy.png")
        #035-2.指定初始随机速度，指定初始随机位置
        self.speed = random.randint(ENEMY_SPEED_MIN, ENEMY_SPEED_MAX)
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0
    def __del__(self):
        #print("敌机挂了%s" % self.rect)
        pass
    
    def update(self):
        #1.调用父类方法，保持垂直方向飞行
        super().update()
        
        #2.判断是否飞出屏幕，如果是，需要从精灵族删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("敌机飞出屏幕，需要从精灵组删除")
            self.kill()
            
class Hero(GameSprite):
    '''英雄精灵'''
    
    #初始位置
    #每隔0.5秒发射一枚子弹
    #键盘左右键使影响左右移动
    def __init__(self):
        #1.调用父类方法，设置image和speed
        super().__init__("D:/File/Python/Plane Wars/image/hero.png",speed = 0)
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.rect.centerx = SCREEN_RECT.centerx
    def update(self):
        pass
    