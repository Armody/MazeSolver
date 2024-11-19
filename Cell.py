from Graphics import *


class Cell():
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color="gray"
        else:
            color="red"
        self_mid_x = self.__x1 + (self.__x2 - self.__x1) / 2
        self_mid_y = self.__y1 + (self.__y2 - self.__y1) / 2
        to_cell_mid_x = to_cell.__x1 + (to_cell.__x2 - to_cell.__x1) / 2
        to_cell_mid_y = to_cell.__y1 + (to_cell.__y2 - to_cell.__y1) / 2
        path = Line(Point(self_mid_x, self_mid_y), Point(to_cell_mid_x, to_cell_mid_y))
        self.__win.draw_line(path, color)
        