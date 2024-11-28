from state_manager import StateManager
from states.menu import Menu
from states.game import Game
from enums import GameState
import pygame

class Main:
    def __init__(self) -> None:
        pygame.init()
        self._bounds = pygame.Rect(0, 0, 1280, 640)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._bounds.width, self._bounds.height))
        self._state_manager = StateManager(GameState.MENU)
        self._state_objects = {
            GameState.MENU: Menu(self._bounds, self._state_manager),
            GameState.GAME: Game(self._bounds, self._state_manager)
        }


    def _update(self):
        dt = self._clock.tick(60) / 1000
        self._state_objects[self._state_manager.current_state].update(dt)


    def _draw(self):
        self._state_objects[self._state_manager.current_state].draw(self._screen)
        pygame.display.flip()


    def _update_game_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True


    def run_game_loop(self):
        while True:
            running = self._update_game_state()
            if not running:
                break

            self._update()
            self._draw()


if __name__ == "__main__":
    main = Main()
    main.run_game_loop()
