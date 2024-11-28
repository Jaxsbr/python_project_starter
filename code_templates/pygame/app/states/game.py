import math
import random
from state_manager import StateManager
from state import State
from particle_engine import ParticleEngine
import pygame


class Game(State):
    def __init__(self, bounds: pygame.Rect, state_manager: StateManager):
        self._bounds = bounds
        self._state_manager = state_manager
        self._particle_engine = ParticleEngine()
        self._particle_emit_interval = 0.2
        self._partcle_elapsed_emit_time = 0.2
        self._particle_emit_pos = pygame.Vector2(bounds.width / 2, bounds.height / 2)
        self._particle_ttl = 2
        self._particle_colors = [
            pygame.Color(255, 255, 0, 255),   # yellow
            pygame.Color(255, 0, 0, 255),     # red
            pygame.Color(128, 0, 128, 255),   # purple
            pygame.Color(0, 0, 255, 255),     # blue
            pygame.Color(0, 255, 0, 255),   # green
            pygame.Color(173, 216, 230, 255),   # light blue
            pygame.Color(255, 192, 203, 255),   # pink
            pygame.Color(255, 165, 0, 255),   # orange
        ]


    def update(self, dt):
        self._particle_engine.update(dt)

        self._partcle_elapsed_emit_time += 1 * dt
        if self._partcle_elapsed_emit_time >= self._particle_emit_interval:
            self._partcle_elapsed_emit_time = 0
            particle_count = random.randint(25, 100)
            for i in range(particle_count):
                angle = random.choice(range(0, 361, 6))
                radians = math.radians(angle)
                self._particle_engine.emit(
                    self._particle_emit_pos,
                    self._particle_ttl,
                    pygame.Vector2(math.cos(radians), math.sin(radians)),
                    random.choice([250, 500, 750]),
                    random.choice([3, 7, 9, 12, 25]),
                    random.choice(self._particle_colors),
                    True
                )


    def draw(self, screen):
        screen.fill("cornflowerblue")
        self._particle_engine.draw(screen)
