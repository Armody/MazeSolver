from Graphics import *

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall)
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall)

    def draw_move(self, to_cell, undo=False):
        color="red"
        if undo:
            color="gray"
            
        self_mid_x = self._x1 + abs(self._x2 - self._x1) / 2
        self_mid_y = self._y1 + abs(self._y2 - self._y1) / 2

        to_cell_mid_x = to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2
        to_cell_mid_y = to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2

        path = Line(Point(self_mid_x, self_mid_y), Point(to_cell_mid_x, to_cell_mid_y))
        self._win.draw_line(path, color)
        