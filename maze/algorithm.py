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


def aldous_broder(grid):
    cell = grid.random_cell()
    unvisited = grid.size() - 1

    while unvisited > 0:
        neighbor = random.choice(cell.neighbors())

        if not neighbor.links():
            cell.link(neighbor)
            unvisited -= 1

        cell = neighbor


def wilsons(grid):
    unvisited = grid.each_cell()
    first = random.choice(unvisited)
    unvisited.remove(first)

    while unvisited:
        cell = random.choice(unvisited)
        path = [cell]

        while cell in unvisited:
            cell = random.choice(cell.neighbors())
            if cell in path:
                position = path.index(cell)
                path = path[0:position + 1]
            else:
                path.append(cell)

        for index in range(0, len(path) - 1):
            path[index].link(path[index+1])
            unvisited.remove(path[index])


def hunt_and_kill(grid):
    current = grid.random_cell()

    while current:
        unvisited_neighbors = [c for c in current.neighbors() if not c.links()]
        if unvisited_neighbors:
            neighbor = random.choice(unvisited_neighbors)
            current.link(neighbor)
            current = neighbor
        else:
            current = None

            for cell in grid.each_cell():
                visited_neighbors = [c for c in cell.neighbors() if c.links()]
                if not cell.links() and visited_neighbors:
                    current = cell

                    neighbor = random.choice(visited_neighbors)
                    current.link(neighbor)

                    break


def recursive_backtracker(grid, start_at=None):
    if not start_at:
        start_at = grid.random_cell()

    stack = [start_at]
    while stack:
        current = stack[-1]
        neighbors = [cell for cell in current.neighbors() if not cell.links()]

        if not neighbors:
            stack.pop()
        else:
            neighbor = random.choice(neighbors)
            current.link(neighbor)
            stack.append(neighbor)
