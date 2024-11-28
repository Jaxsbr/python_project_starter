from dataclasses import dataclass

from enums import GameState


@dataclass
class StateManager:
    current_state: GameState

    def change(self, new_state: GameState):
        self.current_state = new_state
