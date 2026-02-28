import pygame
from . import events

WIDTH = 640
HEIGHT = 320 

class GameState:
    screen: pygame.Surface
    delta_time: float
    event_state: events.EventState = events.EventState()

def init() -> GameState:
    pygame.init()
    state = GameState()
    state.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    state.delta_time = 1

    return state