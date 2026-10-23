from dataclasses import dataclass
from enum import Enum

@dataclass
class Position:
    x: int
    y: int

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Status(Enum):
    PLAYING = "playing"
    PAUSED = "paused"
    GAMEOVER = "gameover"

class GhostStatus(Enum):
    NORMAL = "normal"
    EDIBLE = "edible"

class PlayerPower(Enum):
    NORMAL = "normal"
    SUPERPOWER = "superpower"

class Ghost:
    def __init__(self, coordinates: Position):
        self.coordinates: Position = coordinates
        self.status = GhostStatus.NORMAL

class Player:
    def __init__(self, name: str, coordinates: Position) -> None:
        self.name: str = name
        self.coordinates: Position = coordinates
        self.status = PlayerPower.NORMAL
    
    def move_player(self, direction: Direction):
        x, y = direction.value
        self.coordinates.x += x
        self.coordinates.y += y
q   
class GameState:
    def __init__(self, lives, timer):
        self.score: int = 0
        self.lives: int = lives
        self.level: int = 1
        self.timer: int = timer
        self.status: Status = Status.PLAYING
    
    def add_score(self, score):
        self.score += score
    
    def lose_life(self):
        if self.lives == 0:
            return 0
        self.lives -= 1
        if self.lives == 0:
            self.status = Status.GAMEOVER
        return 1