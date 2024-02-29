from graphics import *
from random import seed
from random import randint

def main():
    seed()
    win = Window(800, 600)
    for i in range(500):
        line = Line(Point(randint(0, i*20), randint(0, i*20)), Point(randint(0, i*20), randint(0, i*200)))
        win.draw_line(line, "orange")
    win.wait_for_close()

main()