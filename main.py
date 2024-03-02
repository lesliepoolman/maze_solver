from graphics import *
import random

def main():
    win = Window(800, 600)
    for i in range(500):
        cell = Cell(random.choice([True, False]), random.choice([True, False]), random.choice([True, False]), random.choice([True, False]))
        cell.set_window(win)
        cell.draw(Point(i*2, i*3), Point(i*4, i*6))
    win.wait_for_close()

main()