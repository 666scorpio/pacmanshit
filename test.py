from game_config import Level

level = Level(15, 25, 42)

print("Width:", level.width)
print("Height:", level.height)
print("Number of rows:", len(level.maze))
print("Number of columns:", len(level.maze[0]))
print("First row:", level.maze[0])
x = 3
y = 0

cell = level.maze[y][x]

print("Cell value:", cell)
print("North wall:", bool(cell & 1))
print("East wall:", bool(cell & 2))
print("South wall:", bool(cell & 4))
print("West wall:", bool(cell & 8))

x = 3
y = 0

cell = level.maze[y][x]

if not cell & 2:
    print("Can move East")
else:
    print("Wall on East")

if not cell & 8:
    print("Can move West")
else:
    print("Wall on West")