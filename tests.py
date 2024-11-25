import unittest
from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_calls(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_wide_create_calls(self):
        num_cols = 100
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_tall_create_calls(self):
        num_cols = 1
        num_rows = 100
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_entrance_and_exit_cleared(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols-1][num_rows-1].has_bottom_wall, False)

    def test_maze_reset_cell_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(m1._cells[0][0].visited, False)
        self.assertEqual(m1._cells[num_cols // 2][num_rows // 2].visited, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].visited, False)

if __name__ == "__main__":
    unittest.main()
