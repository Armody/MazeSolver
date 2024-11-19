from Graphics import *
from Cell import *

def main():
    win = Window(800, 600)
    c1 = Cell(Point(10,10), Point(100, 100), win)
    c2 = Cell(Point(10, 100), Point(100, 200), win)
    c1.has_bottom_wall = False
    c1.draw()
    c2.has_top_wall = False
    c2.has_right_wall = False
    c2.draw()
    c1.draw_move(c2)
    win.wait_for_close()

main()