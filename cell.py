from graphics import Line, Point

class Cell:
    def __init__(self, win=None, l_wall=True, r_wall=True, t_wall=True, b_wall=True):
        self.has_left_wall = l_wall
        self.has_right_wall = r_wall
        self.has_top_wall = t_wall
        self.has_bottom_wall = b_wall
        self.__win = win
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None

    def set_top_left(self, point):
        self.__x1 = point.x
        self.__y1 = point.y

    def set_btm_right(self, point):
        self.__x2 = point.x
        self.__y2 = point.y

    def draw(self, top_left, btm_right):
        if self.__win is None:
            return
        self.set_btm_right(btm_right)
        self.set_top_left(top_left)
        if self.has_left_wall:
            line = Line(top_left, Point(self.__x1, self.__y2))
            self.__win.draw_line(line, "pink")
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), btm_right)
            self.__win.draw_line(line, "pink")
        if self.has_top_wall:
            line = Line(top_left, Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "pink")            
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), btm_right)
            self.__win.draw_line(line, "pink")
    
    def draw_move(self, to_cell, undo=False, colour="green"):
        if self.__win is None:
            return
        if undo:
            colour = "orange"

        s_mid_y = (self.__y1 + self.__y2) / 2
        s_mid_x = (self.__x1 + self.__x2) / 2

        to_mid_y = (to_cell.__y1 + to_cell.__y2) / 2
        to_mid_x = (to_cell.__x1 + to_cell.__x2) / 2

        if self.__x1 > to_cell.__x1:
            from_center_to_left_edge = Line(Point(self.__x1, s_mid_y), Point(s_mid_x, s_mid_y))
            from_left_edge_to_center = Line(Point(to_mid_x, to_mid_y), Point(to_cell.__x2, to_mid_y))
            self.__win.draw_line(from_center_to_left_edge, colour)
            self.__win.draw_line(from_left_edge_to_center, colour)
        elif self.__x1 < to_cell.__x1:
            from_center_to_right_edge = Line(Point(s_mid_x, s_mid_y), Point(self.__x2, s_mid_y))
            from_right_edge_to_center = Line(Point(to_cell.__x1, to_mid_y), Point(to_mid_x, to_mid_y))
            self.__win.draw_line(from_center_to_right_edge, colour)
            self.__win.draw_line(from_right_edge_to_center, colour)
        elif self.__y1 > to_cell.__y1:
            from_center_to_top_edge = Line(Point(s_mid_x, s_mid_y), Point(s_mid_x, self.__y1))
            from_top_edge_to_center = Line(Point(to_mid_x, to_cell.__y2), Point(to_mid_x, to_mid_y))
            self.__win.draw_line(from_center_to_top_edge, colour)
            self.__win.draw_line(from_top_edge_to_center, colour)
        elif self.__y1 < to_cell.__y1:
            from_center_to_bottom_edge = Line(Point(s_mid_x, s_mid_y), Point(s_mid_x, self.__y2))
            from_bottom_edge_to_center = Line(Point(to_mid_x, to_mid_y), Point(to_mid_x, to_cell.__y1))
            self.__win.draw_line(from_center_to_bottom_edge, colour)
            self.__win.draw_line(from_bottom_edge_to_center, colour)