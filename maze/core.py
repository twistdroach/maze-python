# -*- coding: utf-8 -*-
from enum import Enum, auto, unique
import random
# from PIL import Image, ImageDraw, ImageColor

@unique
class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Distances:
    def __init__(self, root):
        self.root = root
        self.cells = {root: 0}

    def __getitem__(self, item):
        return self.cells.get(item, None)

    def __setitem__(self, key, value):
        self.cells[key] = value

    def __contains__(self, elem):
        return self.cells.__contains__(elem)

    def path_to(self, goal_cell):
        current_cell = goal_cell
        breadcrumbs = Distances(self.root)
        breadcrumbs[current_cell] = self[current_cell]

        while current_cell is not self.root:
            for neighbor in current_cell.links():
                if self[neighbor] < self[current_cell]:
                    breadcrumbs[neighbor] = self[neighbor]
                    current_cell = neighbor

        return breadcrumbs

    def max(self):
        """Returns the cell with the max path length"""
        return max(self.cells, key=self.cells.get)


class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.cell_links = {}
        self.cell_neighbors = {}

    def link(self, cell, bidirectional=True):
        self.cell_links[cell] = True
        if bidirectional:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidirectional=True):
        self.cell_links.pop(cell, None)
        if bidirectional:
            cell.unlink(self, False)
        return self

    def links(self):
        return self.cell_links.keys()

    def is_linked(self, cell):
        return cell in self.cell_links.keys()

    def neighbors(self):
        # TODO is it necessary to filter the None values?  I assume so
        return [i for i in self.cell_neighbors.values() if i]

    def get_neighbor(self, direction):
        return self.cell_neighbors.get(direction, None)

    def distances(self):
        distances = Distances(self)
        frontier = [self]
        while frontier:
            new_frontier = []
            for cell in frontier:
                for linked_cell in cell.links():
                    if linked_cell in distances:
                        continue
                    distances[linked_cell] = distances[cell] + 1
                    new_frontier.append(linked_cell)

            frontier = new_frontier

        return distances


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(row, column) for column in range(width)] for row in range(height)]
        self.configure_neighbors()

    def size(self):
        return self.width * self.height

    def random_cell(self):
        random.choice(random.choice(self.cells))

    def each_row(self):
        return self.cells

    def each_cell(self):
        return [row for columns in self.cells for row in columns]

    # def to_img(self, cell_size=10):
    #     img_width = 1 + cell_size * self.width
    #     img_height = 1 + cell_size * self.height
    #
    #     background = ImageColor.getrgb("white")
    #     wall = ImageColor.getrgb("black")
    #
    #     img = Image.new("RGB", (img_width, img_height), background)
    #     imgdraw = ImageDraw.Draw(img)
    #
    #     for cell in self.each_cell():
    #         x1 = cell.column * cell_size
    #         y1 = cell.row * cell_size
    #         x2 = (cell.column + 1) * cell_size
    #         y2 = (cell.row + 1) * cell_size
    #
    #         if not cell.get_neighbor(Direction.NORTH):
    #             imgdraw.line([(x1, y1), (x2, y1)], wall)
    #         if not cell.get_neighbor(Direction.WEST):
    #             imgdraw.line([(x1, y1), (x1, y2)], wall)
    #
    #         if not cell.is_linked(cell.get_neighbor(Direction.EAST)):
    #             imgdraw.line([(x2, y1), (x2, y2)], wall)
    #         if not cell.is_linked(cell.get_neighbor(Direction.SOUTH)):
    #             imgdraw.line([(x1, y2), (x2, y2)], wall)
    #
    #     return img

    def configure_neighbors(self):
        for column in range(self.width):
            for row in range(self.height):
                cell = self.cells[row][column]
                if column == 0:
                    cell.cell_neighbors[Direction.WEST] = None
                else:
                    cell.cell_neighbors[Direction.WEST] = self.cells[row][column - 1]

                if column == self.width - 1:
                    cell.cell_neighbors[Direction.EAST] = None
                else:
                    cell.cell_neighbors[Direction.EAST] = self.cells[row][column + 1]

                if row == 0:
                    cell.cell_neighbors[Direction.NORTH] = None
                else:
                    cell.cell_neighbors[Direction.NORTH] = self.cells[row - 1][column]

                if row == self.height - 1:
                    cell.cell_neighbors[Direction.SOUTH] = None
                else:
                    cell.cell_neighbors[Direction.SOUTH] = self.cells[row + 1][column]

    def contents_of(self, cell):
        return " "

    def __str__(self):
        output = "+" + "---+" * self.width + "\n"
        for row in self.each_row():
            top = "|"
            bottom = "+"
            for cell in row:
                body = '{:^3}'.format(self.contents_of(cell))

                east_boundary = "|"
                if cell.is_linked(cell.get_neighbor(Direction.EAST)):
                    east_boundary = " "
                top += "{}{}".format(body, east_boundary)

                south_boundary = "---"
                if cell.is_linked(cell.get_neighbor(Direction.SOUTH)):
                    south_boundary = "   "

                corner = "+"
                bottom += "{}{}".format(south_boundary, corner)
            output += top + "\n"
            output += bottom + "\n"
        return output


class DistanceGrid(Grid):
    distances = None

    def contents_of(self, cell):
        # if self.distances and self.distances[cell]:
        if self.distances and cell in self.distances:
            return self.distances[cell]
        else:
            return super().contents_of(cell)
