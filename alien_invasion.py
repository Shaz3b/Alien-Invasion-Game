#!/usr/bin/python3
import sys
import pygame

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("Alien Invension")

  bg_color = (230, 230, 230)

  while True:
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        sys.exit()

    screen.fill(bg_color)
    pygame.display.flip()

run_game()
