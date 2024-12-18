from Graphics import *
from Maze import *

def main():
    size_x = 800
    size_y = 600
    num_cols = 20
    num_rows = 16
    margin = 50
    cell_size_x = (size_x - margin * 2) / num_cols
    cell_size_y = (size_y - margin * 2) / num_rows
    win = Window(size_x, size_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()

main()