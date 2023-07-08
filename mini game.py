import os
import pygame

pygame.init()

screen_width = 640 
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("TEAM_FIVE")

# FPS
clock = pygame.time.Clock()


#사용자 게임 초기화
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경
background = pygame.image.load(os.path.join(image_path, "background.png"))
