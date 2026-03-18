import pygame
from pygame.draw import *

# --- Функции отрисовки отдельных частей ---

def draw_body(surf, x, y, w, h, color):
    ellipse(surf, color, (x - w // 2, y - h // 2, w, h))

def draw_head(surf, x, y, size, color):
    circle(surf, color, (x, y), size // 2)

def draw_ear(surf, x, y, w, h, color):
    ellipse(surf, color, (x - w // 2, y - h // 2, w, h))

def draw_eye(surf, x, y, size):
    '''Рисует глаз: белок и зрачок'''
    circle(surf, (255, 255, 255), (x, y), size // 2)
    circle(surf, (0, 0, 0), (x, y), size // 4)

def draw_nose(surf, x, y, size):
    '''Рисует розовый носик'''
    circle(surf, (255, 182, 193), (x, y), size // 2)

def draw_paw(surf, x, y, w, h, color):
    '''Рисует лапку (овал)'''
    ellipse(surf, color, (x - w // 2, y - h // 2, w, h))

# --- Основная функция сборки зайца ---

def draw_hare(surf, x, y, w, h, color):
    '''Собирает зайца из деталей по относительным координатам'''
    
    # 1. Тело
    bw, bh = w // 2, h // 2
    draw_body(surf, x, y + bh // 2, bw, bh, color)
    
    # 2. Голова
    h_size = h // 4
    h_y = y - h_size // 2
    draw_head(surf, x, h_y, h_size, color)
    
    # 3. Уши
    e_h = h // 3
    e_y = y - h // 2 + e_h // 2
    for e_x in (x - h_size // 4, x + h_size // 4):
        draw_ear(surf, e_x, e_y, w // 8, e_h, color)
        
    # 4. Глаза
    eye_size = h_size // 5
    eye_y = h_y - h_size // 8
    for eye_x in (x - h_size // 4, x + h_size // 4):
        draw_eye(surf, eye_x, eye_y, eye_size)
        
    # 5. Нос
    draw_nose(surf, x, h_y + h_size // 8, h_size // 10)
    
    # 6. Лапки (нижние)
    p_h = h // 12
    p_y = y + h // 2 - p_h // 2
    for p_x in (x - bw // 3, x + bw // 3):
        draw_paw(surf, p_x, p_y, bw // 2, p_h, color)

# --- Исполняемая часть ---

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((135, 206, 235)) # Небесный фон

# Рисуем серого зайца в центре
draw_hare(screen, 200, 200, 180, 320, (200, 200, 200))

pygame.display.update()
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

pygame.quit()