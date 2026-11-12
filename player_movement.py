from .models.game_types import Direction
from .models.game_types import Position
from time import monotonic

WALL_BIT: dict[Direction, int] = {
    Direction.UP: 1,      # north
    Direction.RIGHT: 2,   # east
    Direction.DOWN: 4,    # south
    Direction.LEFT: 8,    # west
}

class PlayerMovement():
    def __init__(self, game_session):
        self.game_session = game_session
        self.player = game_session.player
        self.player.last_move = monotonic()
        self.player_move_interval = 0.02

    def ready_move_again(self):
        current_time = monotonic()
        if current_time - self.player.last_move >=\
            self.player_move_interval:
            self.player.last_move = current_time
            return True
        return False

    def can_move(self, direction: Direction):
        dx, dy = direction.value
        move_position = Position(
            self.player.coordinates.x + dx,
            self.player.coordinates.y + dy
        )
        if (0 <= move_position.x < len(self.game_session.maze[0])) and\
            (0 <= move_position.y < len(self.game_session.maze)) and\
            self.game_session.maze[move_position.y][move_position.x] != 15 and\
            not self.game_session.maze[self.player.coordinates.y][self.player.coordinates.x]\
                & WALL_BIT[direction]:
            return True
        return False

    def move_player(self, direction: Direction):
        if self.can_move(direction):
            dx, dy = direction.value
            self.player.direction = direction
            self.player.coordinates = Position(
                self.player.coordinates.x + dx,
                self.player.coordinates.y + dy
            )
            return True
        return False