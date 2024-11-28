from enums import GameState
from state_manager import StateManager
from state import State
import pygame

class Menu(State):
    def __init__(self, bounds: pygame.Rect, state_manager: StateManager):
        self._bounds = bounds
        self._state_manager = state_manager
        pygame.font.init()
        self._font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self._hover_color = "red"
        self._text_color = "white"
        self._button_width = 150
        self._button_height = 75
        self._play_button = pygame.Rect(
            bounds.width / 2 - self._button_width / 2,
            bounds.height / 2 - self._button_height / 2,
            self._button_width,
            self._button_height)


    def update(self, dt):
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]
        self._play_button_hover_color = self._text_color

        if self._play_button.collidepoint(mouse_pos):
            self._play_button_hover_color = self._hover_color
            if mouse_clicked:
                self._state_manager.change(GameState.GAME)


    def draw(self, screen):
        screen.fill("purple")
        pygame.Surface.fill(screen, "blue", self._play_button)
        pygame.draw.rect(screen, self._play_button_hover_color, self._play_button, 2)
        text_surface = self._font.render("Play", True, self._play_button_hover_color)
        text_rect = text_surface.get_rect(center=(
            self._play_button.x + self._button_width / 2,
            self._play_button.y + self._button_height / 2))
        screen.blit(text_surface, text_rect)
