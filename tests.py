import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_different_sizes(self):
        # Test with different number of rows and columns
        num_cols = 5
        num_rows = 8
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m2._Maze__cells), num_cols)
        self.assertEqual(len(m2._Maze__cells[0]), num_rows)

        num_cols = 15
        num_rows = 20
        m3 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m3._Maze__cells), num_cols)
        self.assertEqual(len(m3._Maze__cells[0]), num_rows)

    def test_maze_zero_size(self):
        # Test with zero rows and columns
        num_cols = 0
        num_rows = 0
        m4 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(len(m4._Maze__cells), num_cols)
        if num_cols > 0:
            self.assertEqual(len(m4._Maze__cells[0]), num_rows)
        else:
            self.assertEqual(len(m4._Maze__cells), 0)

    def test_maze_one_cell(self):
        # Test with one cell
        num_cols = 1
        num_rows = 1
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m5._Maze__cells), num_cols)
        self.assertEqual(len(m5._Maze__cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()