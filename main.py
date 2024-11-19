from Graphics import *

def main():
    win = Window(800, 600)
    cell = Cell(Point(10,10), Point(100, 100), win)
    cell.draw()
    win.wait_for_close()

main()