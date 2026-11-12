from .models.game_types import Ghost
from .models.game_types import Position
from .models.game_types import GhostStatus
from .models.game_types import Status
from .models.game_types import PlayerPower
from .models.game_types import GhostName
from time import monotonic
from math import dist
from copy import copy

class GhostsMovement():
    def __init__(self, game_session):
        self.game_session = game_session
        self.player = game_session.player
        self.player_previous_coordinates = copy(self.player.coordinates)
        self.ghost_move_interval = 0.3

    def can_ghost_move(self, ghost):
        current_time = monotonic()
        if current_time - ghost.last_ghost_move >= self.ghost_move_interval:
            ghost.last_ghost_move = current_time
            return True
        return False
    
    def get_shortest_path(self, start, goal):
        pass

    def get_ghost_path(self, ghost):
        #blinky is the red ghost
        if ghost.name == GhostName.BLINKY:
            target = self.player.coordinates
        #pinky is the pink one lol
        elif ghost.name == GhostName.PINKY:
            player_direction_x, player_direction_y = self.player.direction.value
            target = Position(
                self.player.coordinates.x + (player_direction_x * 4),
                self.player.coordinates.y + (player_direction_y * 4)
            )
        #inky is the light blue ghost
        elif ghost.name == GhostName.INKY:
            player_direction_x, player_direction_y = self.player.direction.value
            pivot = Position(
                self.player.coordinates.x + (2 * player_direction_x),
                self.player.coordinates.y + (2 * player_direction_y)
                )
            blinky = self.game_session.ghosts[0]
            target = Position(
                pivot.x + (pivot.x - blinky.coordinates.x),
                pivot.y + (pivot.y - blinky.coordinates.y)
            )
        #clyde is the orange one
        elif ghost.name == GhostName.CLYDE:
            distance = dist(
                (ghost.coordinates.x, ghost.coordinates.y),
                (self.player.coordinates.x, self.player.coordinates.y)
                )
            if distance >= 8:
                target = Position(
                    self.player.coordinates.x,
                    self.player.coordinates.y)
            else:
                target = Position(
                    ghost.start_coordinates.x,
                    ghost.start_coordinates.y)
        return self.get_shortest_path(ghost.coordinates, target)

    def reset_ghost(self, ghost):
        ghost.coordinates = copy(ghost.start_coordinates)
        ghost.path = self.get_ghost_path(ghost)
        ghost.path_index = 1

    def move_ghost(self, ghost):       
        if ghost.player_previous_coordinates != self.player.coordinates:
            ghost.player_previous_coordinates = Position(
                self.player.coordinates.x,
                self.player.coordinates.y)
            ghost.path = self.get_ghost_path(ghost)
            ghost.path_index = 1
        if ghost.path_index >= len(ghost.path):
            ghost.path = self.get_ghost_path(ghost)
            ghost.path_index = 1
        if len(ghost.path) < 2:
            return
        ghost.coordinates = Position(
            ghost.path[ghost.path_index].x,
            ghost.path[ghost.path_index].y)
        ghost.path_index += 1