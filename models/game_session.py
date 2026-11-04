from enum import Enum

class SessionState(Enum):
    PAUSED = 0
    OVER = 1
    PLAYING = 2

class GameSession():
    def __init__(self, maze, player, ghosts, pacgums, game_state):
        self.maze = maze
        self.player = player
        self.ghosts = ghosts
        self.pacgums = pacgums
        self.game_state = game_state
        self.session_state = SessionState(2)