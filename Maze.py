from Cell import *
import time
import random

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None
                 ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i > 0: #not left column
                if not self._cells[i-1][j].visited:
                    possible_directions.append("left")
            if i < self._num_cols - 1: #not right column
                if not self._cells[i+1][j].visited:
                    possible_directions.append("right")
            if j > 0: #not top row
                if not self._cells[i][j-1].visited:
                    possible_directions.append("top")
            if j < self._num_rows - 1: #not bottom row
                if not self._cells[i][j+1].visited:
                    possible_directions.append("bottom")
            
            if len(possible_directions) == 0:
                return
            else:
                direction = random.choice(possible_directions)
            
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1, j)
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1, j)
            if direction == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i, j-1)
            if direction == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i, j+1)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
