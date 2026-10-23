from mazegenerator import MazeGenerator

class Level:
    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        mazegenerator = MazeGenerator(
                                        size=(width, height),
                                        perfect=False,
                                        entry_cell=(0, 0),
                                        exit_cell=(-1, -1),
                                        seed=seed
                                        )
        self.maze = mazegenerator.maze

class Config:
    def __init__(
        self,
        highscore_filename,
        level_array,
        points_per_pacgum,
        points_per_super_pacgum,
        points_per_ghost,
        seed,
        level_max_time,
    ):
        self.highscore_filename = highscore_filename
        self.level_array = level_array
        self.points_per_pacgum = points_per_pacgum
        self.points_per_super_pacgum = points_per_super_pacgum
        self.points_per_ghost = points_per_ghost
        self.seed = seed
        self.level_max_time = level_max_time
        self.levels = []
        for level in self.level_array:
            self.levels.append(Level(level["width"], level["height"], self.seed))