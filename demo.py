import maze

def header(type):
    print("{} {} {}".format("=" * 5, type, "=" * 5))


header("binary tree")
grid = maze.Grid(15, 15, maze.binary_tree)
# grid_img = grid.to_img()
# grid_img.show("binary tree")
print(grid)

header("sidewinder")
grid = maze.Grid(15, 15, maze.sidewinder)
# grid_img = grid.to_img()
# grid_img.show("sidewinder")
print(grid)

header("aldous broder")
grid = maze.Grid(15, 15, maze.aldous_broder)
# grid_img = grid.to_img()
# grid_img.show("aldous broder")
print(grid)

header("wilsons")
grid = maze.Grid(15, 15, maze.wilsons)
# grid_img = grid.to_img()
# grid_img.show("wilsons")
print(grid)

header("hunt and kill")
grid = maze.Grid(15, 15, maze.hunt_and_kill)
# grid_img = grid.to_img()
# grid_img.show("wilsons")
print(grid)

header("recursive backtracker")
grid = maze.Grid(15, 15, maze.recursive_backtracker)
# grid_img = grid.to_img()
# grid_img.show("wilsons")
print(grid)

header("recursive backtracker - masked")
mask = maze.Mask.from_string('''X........X
....XX....
...XXXX...
....XX....
X........X
X........X
....XX....
...XXXX...
....XX....
X........X''')
grid = maze.MaskedGrid(mask, maze.recursive_backtracker)
# grid_img = grid.to_img()
# grid_img.show("recursive backtracker - masked")
print(grid)

header("recursive backtracker - masked test_mask.png")
mask = maze.Mask.from_image("test_mask.png")
if not mask:
    print("Failed to load mask")
    exit(2)
grid = maze.MaskedGrid(mask, maze.recursive_backtracker)
grid_img = grid.to_img()
grid_img.show("recursive backtracker - masked test_mask.png")
print(grid)

exit(1)

header("wilson - distance")
grid = maze.DistanceGrid(50, 50, None)
print("creating maze with sidewinder algo")
# maze.sidewinder(grid)
# maze.aldous_broder(grid)
# maze.wilsons(grid)
# maze.hunt_and_kill(grid)
maze.recursive_backtracker(grid)
#start from the middle
start_cell = grid.cells[int(grid.height / 2)][int(grid.width / 2)]
print("calculating distances")
grid.distances = start_cell.distances()
print("generating image")
grid_img = grid.to_img()
grid_img.show("sidewinder - distance")
print(grid)

new_start = grid.distances.max()
new_distances = new_start.distances()
goal = new_distances.max()
grid.distances = new_distances

# grid2 = maze.DistanceGrid(15, 15)
# grid2.distances = grid.distances.path_to(grid.cells[grid.height - 1][grid.width - 1])
# print(grid2)
header("wilson - longest path")
grid.distances = grid.distances.path_to(grid.cells[grid.height - 1][0])
# grid.distances = grid.distances.path_to(grid.cells[grid.height - 1][grid.width - 1])
print(grid)
