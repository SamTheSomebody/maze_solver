from tkinter import Tk, BOTH, Canvas
from line import Line
from window import Window
from point import Point
from cell import Cell
from maze import Maze
def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 12, 10, 30, 30, win)
    win.wait_for_close()

main()
