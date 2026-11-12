from .models.game_session import GameSession
from .models.game_types import Player
from .models.game_types import Position
from .models.game_types import Ghost
from .models.game_types import GameState
from .models.game_types import GhostName

class GameInitializer():
    def __init__(self, game_configs):
        self.game_configs = game_configs
        self.width = 0
        self.height = 0

    def init_game(self, level):
        self.width = self.game_configs.levels[level].width
        self.height = self.game_configs.levels[level].height
        self.maze = self.game_configs.levels[level].maze
        player = self.create_player()
        ghosts = self.create_ghosts()
        pacgums = self.create_pacgums(player)
        game_state = GameState(self.game_configs.lives,
                                self.game_configs.timer)
        return GameSession(self.maze, player, ghosts, pacgums, game_state)

    def create_player(self):
        x = self.width // 2
        y = self.height // 2
        positions = [
            (x, y), (x + 1, y), (x - 1, y),
            (x, y - 1), (x, y + 1) 
        ]
        for px, py in positions:
            if ((0 <= px < self.width and 0 <= py < self.height)
                and self.maze[py][px] != 15):
                return Player(Position(px, py))

    def create_ghosts(self):
        w = self.width
        h = self.height
        positions = [
            (1, 0), (1, h-1), (w-1, 1), (w-2, h-1)
        ]
        ghosts = []
        for i, pos in enumerate(positions, 1):
            ghosts.append(Ghost(GhostName(i), Position(pos[0], pos[1])))
        return ghosts

    def create_pacgums(self, player):
        pacgums_positions = []
        superpacgums_positions = [
            (0, 0),
            (0, self.height - 1),
            (self.width - 1, 0),
            (self.width - 1, self.height - 1)
        ]
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 15:
                    continue
                if (x, y) == (player.coordinates.x, player.coordinates.y):
                    continue
                if (x, y) not in superpacgums_positions:
                    pacgums_positions.append(Position(x, y))
        pacgums_grid = [[0 for _ in range(self.width)]
                        for _ in range(self.height)]
        for position in pacgums_positions:
            pacgums_grid[position.y][position.x] = 1
        for position in superpacgums_positions:
            pacgums_grid[position.y][position.x] = 2
        return pacgums_grid