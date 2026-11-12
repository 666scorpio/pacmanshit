from .models.game_types import Ghost
from .models.game_types import Position
from .models.game_types import GhostStatus
from .models.game_types import Status
from .models.game_types import PlayerPower
from .models.game_types import GhostStatus
from .ghosts_movement import GhostsMovement
from .player_movement import PlayerMovement
from copy import copy

class GameEngine():
    def __init__(self, game_session):
        self.game_session = game_session
        self.player = game_session.player
        self.ghosts_movement = GhostsMovement(game_session)
        self.player_movement = PlayerMovement(game_session)
        self.edible_timer = 0.0

    def lose_life(self):
        if self.game_session.game_state.lives == 0:
            return -1
        self.game_session.game_state.lives -= 1
        if self.game_session.game_state.lives == 0:
            self.game_session.game_state.status = Status.GAMEOVER
        return 1

    def add_score(self, score):
        self.game_session.game_state.score += score

    def check_if_pacgum(self, position: Position):
        pacgum = self.game_session.pacgums[position.y][position.x]
        if pacgum == 1:
            self.add_score(self.game_session.points_per["pacgum"])
        elif pacgum == 2:
            self.add_score(self.game_session.points_per["superpacgum"])
            for ghost in self.game_session.ghosts:
                ghost.status = GhostStatus.EDIBLE
            self.edible_timer = 10.0
        self.game_session.pacgums[position.y][position.x] = 0

    def handle_ghost_collision(self, ghost):
        if ghost.status == GhostStatus.EDIBLE:
            self.add_score(self.game_session.points_per["ghost"])
            ghost.status = GhostStatus.NORMAL
            self.ghosts_movement.reset_ghost(ghost)
        else:
            self.lose_life()
            self.player.coordinates = copy(self.player.start_coordinates)
            for g in self.game_session.ghosts:
                self.ghosts_movement.reset_ghost(g)

    def check_collisions(self):
        for ghost in self.game_session.ghosts:
            if ghost.coordinates == self.player.coordinates:
                self.handle_ghost_collision(ghost)
                return

    def update(self, player_next_direction):
        if self.game_session.game_state.status != Status.PLAYING:
            return
        if self.player_movement.ready_move_again():
            if not self.player_movement.move_player(player_next_direction):
                self.player_movement.move_player(self.player.direction)
            self.check_if_pacgum(self.player.coordinates)
        for ghost in self.game_session.ghosts:
            if self.ghosts_movement.can_ghost_move(ghost):
                self.ghosts_movement.move_ghost(ghost)
        self.check_collisions()