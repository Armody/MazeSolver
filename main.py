from Graphics import *
from Maze import *

def main():
    win = Window(800, 600)
    maze = Maze(10, 10, 4, 5, 50, 60, win)

    win.wait_for_close()

main()