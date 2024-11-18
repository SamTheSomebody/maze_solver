from point import Point
from line import Line
from window import Window

class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.win = win
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

    def draw(self):
        line_color = "black"
        if self.has_left_wall:
            self.win.draw_line(self._left_wall, line_color)
        if self.has_right_wall:
            self.win.draw_line(self._right_wall, line_color)
        if self.has_top_wall:
            self.win.draw_line(self._top_wall, line_color)
        if self.has_bottom_wall:
            self.win.draw_line(self._bottom_wall, line_color)
