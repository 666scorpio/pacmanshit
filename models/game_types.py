from dataclasses import dataclass
from enum import Enum
from time import monotonic

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
    VICTORY = "victory"

class GhostStatus(Enum):
    NORMAL = "normal"
    EDIBLE = "edible"

class PlayerPower(Enum):
    NORMAL = "normal"
    SUPERPOWER = "superpower"

class GhostName(Enum):
    BLINKY = 1
    PINKY = 2
    INKY = 3
    CLYDE = 4

class Ghost:
    def __init__(self, name: GhostName, coordinates: Position):
        self.name = name
        self.coordinates: Position = coordinates
        self.start_coordinates = coordinates
        self.path = []
        self.path_index = 1
        self.last_ghost_move = monotonic()
        self.player_previous_coordinates = None
        self.status = GhostStatus.NORMAL

class Player:
    def __init__(self, coordinates: Position) -> None:
        self.coordinates: Position = coordinates
        self.start_coordinates = Position(coordinates.x, coordinates.y)
        self.direction = Direction.UP
        self.status = PlayerPower.NORMAL
        self.last_move = None
    
    def move_player(self, direction: Direction):
        x, y = direction.value
        self.coordinates.x += x
        self.coordinates.y += y

class GameState:
    def __init__(self, lives, timer) -> None:
        self.score: int = 0
        self.lives: int = lives
        self.level: int = 1
        self.timer: int = timer
        self.status: Status = Status.PLAYING