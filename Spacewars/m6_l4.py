import pygame
#
# win_x = 1024 # Размер по ширине
# win_y = 720 # Размер по высоте
#
# # Установим название нашего приложение
#
# pygame.display.set_caption("Наша Игра")
# pygame.display.set_mode((win_x, win_y))
#
# run = True
# while run:
#     # Перебираем все эвенты которые мы проводим
#     for event in pygame.event.get():
#         # Если тип эвента равен QUIT True на False из-за чего окно подает
#         if event.type == pygame.QUIT:
#             print("Выход!")
# #             run = False
# #
# #         #Обрабатывать событие  на нажатие клавиш
# #
# #         if event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_SPACE:
# #                 print("Вы нажали на пробел!")
# #
# #         if event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_w:
# #                 print("Вы нажали на W")
# #
# #         if event.type == pygame.KEYDOWN:
# #             if event.key == pygame.K_a:
# #                 print("Вы нажали на а")
# #
# #             if event.key == pygame.K_s:
# #                 print("Вы нажали на с")
# #
# #             if event.key == pygame.K_d:
# #                 print("Вы нажали на д")
# #
#
# win_x = 1024
# win_y = 720
#
# pygame.display.set_caption("Игра!")
# WINDOW = pygame.display.set_mode((win_x, win_y))
#
# background_images = pygame.image.load("bg_photo.jpg")
# shippng = pygame.image.load("ship.png")
# shi = pygame.image.load("ship-enemy.png")
# background_object = pygame.transform.scale(background_images, (win_x, win_y))
# bacc = pygame.transform.scale(shippng,(150, 150))
# ship = pygame.transform.scale(shi, (150, 150))
#
# run = True
# while run:
#     pygame.display.update()
#     WINDOW.blit(background_object, (0, 0))
#     WINDOW.blit(shippng, (330, 350))
#     WINDOW.blit(shi, (400, 30))
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             run =

import sys
from PyQt6.QWidgets, import QMessageBox, QPushButton, QMainWindow, QTextEdit, QFileDialog, QApplication