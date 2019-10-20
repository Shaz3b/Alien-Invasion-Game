#!/usr/bin/env python3
import sys
import pygame
from settings import Settings

def run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
  pygame.display.set_caption("Alien Invastion")


  while True:
    for i in pygame.event.get():
      if i.type == pygame.QUIT:
        sys.exit()

    screen.fill(ai_settings.bg_color)
    pygame.display.flip()

run_game()
