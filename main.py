from graphics import *
from cell import *

def main():
    win = Window(800, 600)
    cell1 = Cell(win, r_wall=False)
    cell1.draw(Point(10, 10), Point(100, 100))
    cell2 = Cell(win, l_wall=False, b_wall=False)
    cell2.draw(Point(100, 10), Point(200, 100))
    cell1.draw_move(cell2)

    cell3 = Cell(win, r_wall=False, t_wall=False)
    cell3.draw(Point(100, 100), Point(200, 200))
    cell2.draw_move(cell3)

    cell4 = Cell(win, l_wall=False, t_wall=False)
    cell4.draw(Point(200, 100), Point(300, 200))
    cell3.draw_move(cell4)

    cell5 = Cell(win, b_wall=False, r_wall=False)
    cell5.draw(Point(200, 10), Point(300, 100))
    cell4.draw_move(cell5, undo=True)

    cell6 = Cell(win, r_wall=False)
    cell6.draw(Point(200, 300), Point(300, 400))
    cell7 = Cell(win, l_wall=False)
    cell7.draw(Point(300, 300), Point(400, 400))
    cell6.draw_move(cell7, undo=True)

    win.wait_for_close()

main()