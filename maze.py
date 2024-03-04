from cell import *
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed
        if self.__seed:
            random.seed(self.__seed)
        self.__create_cells()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
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
        time.sleep(0.01)

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(0, 0)
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, col, row):
        current = self._cells[col][row]
        current.visited = True
        while True:
            poss_dirs = self.__neighbours(col, row)
            if len(poss_dirs) == 0:
                self.__draw_cell(col, row)
                return
            rand_dir = poss_dirs[random.randrange(len(poss_dirs))]
            cell_to_connect = self._cells[rand_dir[0]][rand_dir[1]]
            if rand_dir[0] < col:
                current.has_left_wall = False
                self.__draw_cell(col, row)
                cell_to_connect.has_right_wall = False
                self.__draw_cell(rand_dir[0], rand_dir[1])
            elif rand_dir[0] > col:
                current.has_right_wall = False
                self.__draw_cell(col, row)
                cell_to_connect.has_left_wall = False
                self.__draw_cell(rand_dir[0], rand_dir[1])
            elif rand_dir[1] < row:
                current.has_top_wall = False
                self.__draw_cell(col, row)
                cell_to_connect.has_bottom_wall = False
                self.__draw_cell(rand_dir[0], rand_dir[1])
            elif rand_dir[1] > row:
                current.has_bottom_wall = False
                self.__draw_cell(col, row)
                cell_to_connect.has_top_wall = False
                self.__draw_cell(rand_dir[0], rand_dir[1])
            self.__break_walls_r(rand_dir[0], rand_dir[1])
    
    def __reset_cells_visited(self):
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self._cells[col][row].visited = False

    def solve(self):
        return self.__solve_r(0, 0)
    
    def __solve_r(self, col, row):
        self.__animate()
        current = self._cells[col][row]
        current.visited = True
        if col == (self.__num_cols - 1) and row == (self.__num_rows - 1):
            return True
        for neighbour in self.__neighbours(col, row):
            neighbour_cell = self._cells[neighbour[0]][neighbour[1]]
            if neighbour[0] < col and current.has_left_wall is False and neighbour_cell.has_right_wall is False:
                current.draw_move(neighbour_cell)
                if self.__solve_r(neighbour[0], neighbour[1]):
                    return True
                else:
                    current.draw_move(neighbour_cell, undo=True)
            elif neighbour[0] > col and current.has_right_wall is False and neighbour_cell.has_left_wall is False:
                current.draw_move(neighbour_cell)
                if self.__solve_r(neighbour[0], neighbour[1]):
                    return True
                else:
                    current.draw_move(neighbour_cell, undo=True)
            elif neighbour[1] < row and current.has_top_wall is False and neighbour_cell.has_bottom_wall is False:
                current.draw_move(neighbour_cell)
                if self.__solve_r(neighbour[0], neighbour[1]):
                    return True
                else:
                    current.draw_move(neighbour_cell, undo=True)
            elif neighbour[1] > row and current.has_bottom_wall is False and neighbour_cell.has_top_wall is False:
                current.draw_move(neighbour_cell)
                if self.__solve_r(neighbour[0], neighbour[1]):
                    return True
                else:
                    current.draw_move(neighbour_cell, undo=True)
        return False

    def __neighbours(self, col, row):
        to_visit = []
        if col-1 in range(self.__num_cols):
            to_visit.append([col-1, row])
        if col+1 in range(self.__num_cols):
            to_visit.append([col+1, row])
        if row-1 in range(self.__num_rows):
            to_visit.append([col, row-1])
        if row+1 in range(self.__num_rows):
            to_visit.append([col, row+1])
        poss_dirs = []
        for idxs in to_visit:
            if self._cells[idxs[0]][idxs[1]].visited is False:
                poss_dirs.append(idxs)
        return poss_dirs


