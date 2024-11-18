from point import Point

class Line:
    def __init__(self, point_start, point_end):
        self.__point_start = point_start
        self.__point_end = point_end

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.__point_start.x, self.__point_start.y,
            self.__point_end.x, self.__point_end.y,
            fill = fill_color, width = 2)

