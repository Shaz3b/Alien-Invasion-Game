import sys
import pygame

def check_events():
  for i in pygame.event.get():
    if i.type == pygame.QUIT:
      sys.exit()
