from graphics import Window
from maze import *

def main():
    win = Window(800, 600)
    Maze(5, 5, 10, 10, 50, 50, win)
    win.wait_for_close()

main()