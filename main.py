from Window import *

def main():
    win = Window(800, 600)
    point1 = Point(600, 0)
    point2 = Point(10, 300)
    line = Line(point1, point2)
    win.draw_line(line, "black")
    win.wait_for_close()

main()