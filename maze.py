from cell import *
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()
        self.__break_entrance_and_exit()

    def __create_cells(self):
        for col in range(self.__num_cols):
            cell_col = []
            for row in range(self.__num_rows):
                cell_col.append(Cell(self.__win))
            self._cells.append(cell_col)
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self.__draw_cell(col, row)

    def __draw_cell(self, col, row):
        tlx = self.__x1+(self.__cell_size_x * col)
        tly = self.__y1+(self.__cell_size_y * row)
        top_left = Point(tlx, tly)
        btm_right = Point(tlx+self.__cell_size_x, tly+self.__cell_size_y)
        self._cells[col][row].draw(top_left, btm_right)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(0, 0)
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
