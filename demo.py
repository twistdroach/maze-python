import maze

def header(type):
    print("{} {} {}".format("=" * 5, type, "=" * 5))

header("binary tree")
grid = maze.Grid(10, 10)
maze.binary_tree(grid)
# grid_img = grid.to_img()
# grid_img.show("binary tree")
print(grid)

header("sidewinder")
# grid = maze.Grid(20, 30)
grid = maze.Grid(15, 15)
maze.sidewinder(grid)
# grid_img = grid.to_img()
# grid_img.show("sidewinder")
print(grid)

header("sidewinder - distance")
grid = maze.DistanceGrid(15, 15)
maze.sidewinder(grid)
start_cell = grid.cells[0][0]
grid.distances = start_cell.distances()
print(grid)

new_start = grid.distances.max()
new_distances = new_start.distances()
goal = new_distances.max()
grid.distances = new_distances

# grid2 = maze.DistanceGrid(15, 15)
# grid2.distances = grid.distances.path_to(grid.cells[grid.height - 1][grid.width - 1])
# print(grid2)
header("sidewinder - longest path")
grid.distances = grid.distances.path_to(grid.cells[grid.height - 1][0])
# grid.distances = grid.distances.path_to(grid.cells[grid.height - 1][grid.width - 1])
print(grid)
