from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__canvas = Canvas()
        self.__window_running = False
        self.__canvas.pack()
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
        self.__root_widget.title('Funtastic Maze')

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()
    
    def close(self):
        self.__window_running = False
