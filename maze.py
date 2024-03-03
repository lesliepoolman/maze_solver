from cell import *
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win,):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        for col in range(self.__num_cols):
            cell_col = []
            for row in range(self.__num_rows):
                cell_col.append(Cell(self.__win))
            self.__cells.append(cell_col)
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, col, row):
        tlx = self.__x1+(self.__cell_size_x * col)
        tly = self.__y1+(self.__cell_size_y * row)
        top_left = Point(tlx, tly)
        btm_right = Point(tlx+self.__cell_size_x, tly+self.__cell_size_y)
        self.__cells[col][row].draw(top_left, btm_right)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)