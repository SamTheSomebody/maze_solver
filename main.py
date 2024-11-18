from tkinter import Tk, BOTH, Canvas
from line import Line
from window import Window
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    x1 = 100
    x2 = 200
    x3 = 400
    x4 = 600
    y1 = 50
    y2 = 200
    y3 = 300
    y4 = 600
    cell_a = Cell(x1, x2, y1, y2, win)
    cell_b = Cell(x2, x3, y2, y3, win)
    cell_c = Cell(x3, x4, y3, y4, win)
    cell_d = Cell(x2, x4, y1, y4, win)
    cell_a.has_left_wall = False
    cell_b.has_top_wall = False
    cell_c.has_left_wall = False
    cell_c.has_right_wall = False
    cell_a.draw()
    cell_b.draw()
    cell_c.draw()
    cell_d.draw()
    win.wait_for_close()

main()
