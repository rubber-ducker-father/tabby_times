import pygame
from src import setup

def main():
    state = setup.init()
    clock = pygame.time.Clock()
    while state.event_state.running:
        state.screen.fill("purple")
        state.event_state.poll_events()
        pygame.display.flip()
        state.delta_time = clock.tick() / 1000

if __name__=="__main__":
    main()