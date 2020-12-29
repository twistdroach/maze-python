import random
from maze import Direction

def binary_tree(grid):
    for cell in grid.each_cell():
        neighbors = []
        if cell.get_neighbor(Direction.NORTH):
            neighbors.append(cell.get_neighbor(Direction.NORTH))
        if cell.get_neighbor(Direction.EAST):
            neighbors.append(cell.get_neighbor(Direction.EAST))

        if neighbors:
            cell.link(random.choice(neighbors))

def sidewinder(grid):
    for row in grid.each_row():
        run = []
        for cell in row:
            run.append(cell)

            at_east_boundary = (cell.get_neighbor(Direction.EAST) is None)
            at_northern_boundary = (cell.get_neighbor(Direction.NORTH) is None)

            should_close_out = at_east_boundary or (not at_northern_boundary and random.choice([True, False]))

            if should_close_out:
                member = random.choice(run)
                if member.get_neighbor(Direction.NORTH):
                    member.link(member.get_neighbor(Direction.NORTH))
                run.clear()
            else:
                cell.link(cell.get_neighbor(Direction.EAST))


