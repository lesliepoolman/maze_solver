from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title('Funtastic Maze')
        self.__canvas = Canvas(self.__root_widget, bg="grey", height=height, width=width)
        self.__window_running = False
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
        print("Maze Vanished!")
    
    def close(self):
        self.__window_running = False

    def draw_line(self, line, colour):
        line.draw(self.__canvas, colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, point_x, point_y):
        self.__point_x = point_x
        self.__point_y = point_y

    def draw(self, canvas, colour):
        canvas.create_line(
            self.__point_x.x, self.__point_y.x, self.__point_x.y, self.__point_y.y, fill=colour, width=2
        )
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, l_wall=True, r_wall=True, t_wall=True, b_wall=True):
        self.has_left_wall = l_wall
        self.has_right_wall = r_wall
        self.has_top_wall = t_wall
        self.has_bottom_wall = b_wall
        self.__win = None
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None

    def set_window(self, window):
        self.__win = window

    def set_top_left(self, point):
        self.__x1 = point.x
        self.__y2 = point.y

    def set_btm_right(self, point):
        self.__x2 = point.x
        self.__y1 = point.y

    def draw(self, t_left, btm_right):
        self.set_btm_right(btm_right)
        self.set_top_left(t_left)
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line, "pink")
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "pink")
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line, "pink")            
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line, "pink")
