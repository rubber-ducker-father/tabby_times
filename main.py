import pygame
import setup
import tiles

def main():
    state = setup.GameState()
    clock = pygame.time.Clock()
    while state.event_state.running:
        state.screen.fill("purple")
        state.event_state.poll_events()
        tiles.render_tiles()
        pygame.display.flip()
        state.delta_time = clock.tick() / 1000

if __name__=="__main__":
    main()