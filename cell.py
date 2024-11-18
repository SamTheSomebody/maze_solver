from point import Point
from line import Line
from window import Window

class Cell:
    def __init__(self, x1, x2, y1, y2, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.win = win
        self.visited = False
        self.update_coords(x1, x2, y1, y2)

    def update_coords(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        self._left_wall = Line(top_left, bottom_left)
        self._right_wall = Line(top_right, bottom_right)
        self._top_wall = Line(top_left, top_right)
        self._bottom_wall = Line(bottom_left, bottom_right)

    def draw(self, line_color = "black", background_color = "#d9d9d9"):
        if self.win is None:
            return
        color = line_color
        if not self.has_left_wall:
            color = background_color
        self.win.draw_line(self._left_wall, color)

        if self.has_right_wall:
            color = line_color
        else:
            color = background_color
        self.win.draw_line(self._right_wall, color)
        
        if self.has_top_wall:
            color = line_color
        else:
            color = background_color
        self.win.draw_line(self._top_wall, color)

        if self.has_bottom_wall:
            color = line_color
        else:
            color = background_color
        self.win.draw_line(self._bottom_wall, color)

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "grey"
        x1, y1 = self.get_center()
        x2, y2 = to_cell.get_center()
        start = Point(x1, y1)
        end = Point(x2, y2)
        line = Line(start, end)
        self.win.draw_line(line, color)

    def get_center(self):
        x = (self._x1 + self._x2) / 2
        y = (self._y1 + self._y2) / 2
        return (x, y)
