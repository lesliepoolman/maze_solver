from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root_widget = Tk()
        self.__root_widget.title('Funtastic Maze')
        self.__canvas = Canvas(self.__root_widget, bg="grey", height=height, width=width)
        self.__window_running = False
        self.__canvas.pack()
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
