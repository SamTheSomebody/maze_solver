from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y,
                 win = None, seed = None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            self._seed = random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows): 
                cell = self._create_cell(i, j)
                col_cells.append(cell)
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows): 
                self._draw_cell(i, j)

    def _create_cell(self, x, y):
        x1 = self._x1 + x * self._cell_size_x
        y1 = self._y1 + y * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell = Cell(x1, x2, y1, y2, self._win)
        return cell

    def _draw_cell(self, x, y):
        self._cells[x][y].draw()
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw();
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True
        while True:
            unvisted_neighbours = []
            if i > 0 and not self._cells[i - 1][j].visited:
                unvisted_neighbours.append((i - 1, j))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                unvisted_neighbours.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                unvisted_neighbours.append((i, j - 1))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                unvisted_neighbours.append((i, j + 1))
            
            if len(unvisted_neighbours) == 0:
                self._draw_cell(i , j)
                return

            r = random.randrange(len(unvisted_neighbours))
            x, y = unvisted_neighbours[r]
            next = self._cells[x][y]
            if x > i:
                cell.has_right_wall = False
                next.has_left_wall = False
            elif x < i:
                cell.has_left_wall = False
                next.has_right_wall = False
            elif y > j:
                cell.has_bottom_wall = False
                next.has_top_wall = False
            elif y < j:
                cell.has_top_wall = False
                next.has_bottom_wall = False
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def _solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        cell = self._cells[i][j]
        cell.visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        directions = []
        if i < self._num_cols - 1 and not cell.has_right_wall:
            directions.append((i + 1, j))
        if j < self._num_rows - 1 and not cell.has_bottom_wall:
            directions.append((i, j + 1))
        if i > 0 and not cell.has_left_wall:
            directions.append((i - 1, j))
        if j > 0 and not cell.has_top_wall:
            directions.append((i, j - 1))

        for direction in directions:
            x, y = direction
            next = self._cells[x][y]
            if (next.visited):
                continue
            cell.draw_move(next)
            if self._solve_r(x, y):
                return True
            cell.draw_move(next, True)

        return False
