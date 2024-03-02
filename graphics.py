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
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas, colour):
        canvas.create_line(
            self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=colour, width=2
        )
        canvas.pack(fill=BOTH, expand=1)