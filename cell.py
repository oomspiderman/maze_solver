from graphics import Line, Point

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
   
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win is None:
            return

        line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.__win.draw_line(line)
        else: 
            self.__win.draw_line(line,"white")
        
        line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.__win.draw_line(line)
        else: 
            self.__win.draw_line(line,"white")

        line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.__win.draw_line(line)
        else: 
            self.__win.draw_line(line,"white")
        
        line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.__win.draw_line(line)    
        else: 
            self.__win.draw_line(line,"white")
    
    def draw_move(self, to_cell, undo=False):
        mx1 = (self.__x1 + self.__x2) / 2
        my1 = (self.__y1 + self.__y2) / 2
        mx2 = (to_cell.__x1 + to_cell.__x2) / 2
        my2 = (to_cell.__y1 + to_cell.__y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        if self.__win is None:
            return
        
        self.__win.draw_line(Line(Point(mx1, my1), Point(mx2, my2)), fill_color)
