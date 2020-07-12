import sys
sys.path.append("D:\File\Python\Plane Wars")

import pygame

from plane_sprites import *

class PlaneGame(object):
    """飞机大战主程序"""
    def __init__(self):
        print("游戏初始化中...")
        pygame.init()
        pygame.display.set_caption('雷电X')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #创建精灵
        self.__create_sprites()
        #创建时钟
        self.clock = pygame.time.Clock()
        
        #创建敌机定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        
    def __create_sprites(self):
        #创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
        
        #034-创建敌机精灵组
        self.EnemyGroup = pygame.sprite.Group()
        #039-创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        
    def start_game(self):
        print("游戏开始...")
        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PRE_SEC)
            
            #2.事件监听
            self.__event_handler()
            
            #3.碰撞检查
            self.__check_collide()
            
            #4.更新/绘制精灵组
            self.__update_sprites()
            
            #5.更新显示
            pygame.display.update()
            
            #关闭窗口
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("退出游戏。。。")
                    pygame.quit()
                    #直接退出系统
                    exit()
                    
    def __event_handler(self):
        for event in pygame.event.get():
            #判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #034-1.创建精灵
                enemy = Enemy()
                #034-2.将敌机精灵添加到敌机精灵组
                self.EnemyGroup.add(enemy)
                print("敌机出场...")
                
    def __check_collide(self):
        pass
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        
        self.EnemyGroup.update()
        self.EnemyGroup.draw(self.screen)
        
        self.EnemyGroup.update()
        self.EnemyGroup.draw(self.screen)
        
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        #pygame.display.update()
        
    
    @staticmethod#静态方法
    def __game_over():
        print("游戏结束")
        pygame.QUIT()
        exit()

if __name__ == '__main__':
    #创建游戏
    game = PlaneGame()
    #开始游戏
    game.start_game()