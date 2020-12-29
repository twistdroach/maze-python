# -*- coding: utf-8 -*-

from .context import maze

import unittest


class TestCell(unittest.TestCase):
    def setUp(self):
        self.cell1 = maze.Cell(0, 0)
        self.cell2 = maze.Cell(0, 1)

    def test_new_cell_has_no_links_or_neighbors(self):
        self.assertEqual(0, len(self.cell1.links()))
        self.assertEqual(0, len(self.cell1.neighbors()))

    def test_links_returns_linked_cells(self):
        self.cell1.link(self.cell2)
        self.assertEqual(1, len(self.cell1.links()))
        self.assertTrue(self.cell2 in self.cell1.links())

    def test_link_is_bidirectional(self):
        self.cell1.link(self.cell2)
        self.assertEqual(1, len(self.cell1.links()))
        self.assertEqual(1, len(self.cell2.links()))
        self.assertTrue(self.cell2 in self.cell1.links())
        self.assertTrue(self.cell1 in self.cell2.links())

    def test_unlink_is_bidirectional(self):
        self.cell1.link(self.cell2)
        self.cell2.unlink(self.cell1)
        self.assertEqual(0, len(self.cell1.links()))
        self.assertEqual(0, len(self.cell2.links()))
        self.assertTrue(self.cell2 not in self.cell1.links())
        self.assertTrue(self.cell1 not in self.cell2.links())

    def test_is_linked(self):
        self.assertFalse(self.cell1.is_linked(self.cell2))
        self.cell1.link(self.cell2)
        self.assertTrue(self.cell1.is_linked(self.cell2))


class TestGrid(unittest.TestCase):

    def test_grid_initializes_cells(self):
        grid1 = maze.Grid(1, 1)
        self.assertEqual(1, len(grid1.cells))
        self.assertTrue(type(grid1.cells[0][0]) is maze.Cell)

    def test_grid_initializes_calculates_cell_neighbors(self):
        grid1 = maze.Grid(2, 1)
        self.assertEqual(1, len(grid1.cells[0][0].neighbors()))
        self.assertEqual(1, len(grid1.cells[0][1].neighbors()))
        self.assertTrue(grid1.cells[0][0] in grid1.cells[0][1].neighbors())

    def test_grid_size(self):
        grid = maze.Grid(2, 3)
        self.assertEqual(6, grid.size())

    def test_each_cell(self):
        grid = maze.Grid(3, 2)
        cells = grid.each_cell()
        self.assertEqual(grid.cells[0][0], cells[0])
        self.assertEqual(grid.cells[0][1], cells[1])
        self.assertEqual(grid.cells[0][2], cells[2])
        self.assertEqual(grid.cells[1][0], cells[3])
        self.assertEqual(grid.cells[1][1], cells[4])
        self.assertEqual(grid.cells[1][2], cells[5])

    def test_each_row(self):
        grid = maze.Grid(2, 3)
        rows = grid.each_row()
        self.assertEqual(grid.cells[0][0], rows[0][0])
        self.assertEqual(grid.cells[1][0], rows[1][0])
        self.assertEqual(grid.cells[2][0], rows[2][0])

if __name__ == '__main__':
    unittest.main()
