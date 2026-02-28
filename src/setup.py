import pygame
from . import events

WIDTH = 640
HEIGHT = 320 

class GameState:
    screen: pygame.Surface
    delta_time: float
    event_state: events.EventState = events.EventState()

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.delta_time = 1
