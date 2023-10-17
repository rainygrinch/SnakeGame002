import pygame
import sys
import random

pygame.init()

# Set Game Window

window_width = 640
window_height = 480
windows = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set Colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set Snake

snake_speed = 15
snake_block_size = 20
snake_x = window_width // 2
snake_y = window_height // 2
