from cell import Cell
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None, 
        seed = None
    ):
        if seed:
            random.seed(seed)
        
        self.__x1 = x1 
        self.__y1 = y1 
        self.__num_rows = num_rows 
        self.__num_cols = num_cols 
        self.__cell_size_x = cell_size_x 
        self.__cell_size_y = cell_size_y 
        self.__win = win 
        self.__cells = []
        
        self.__SLEEP_TIME = 0.005      # FOR DEBUG ONLY
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__SLEEP_TIME = 0.05      # FOR DEBUG ONLY
        self.__break_walls_r(0, 0)

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        
        if self.__win is None:
            return
            
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y

        if self.__win is None:
            return
        
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(self.__SLEEP_TIME)      # __SLEEP_TIME FOR DEBUG ONLY

    def __break_entrance_and_exit(self):  
        if self.__num_cols == 0 or self.__num_rows == 0:
            return  # Nothing to break        
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    # FOR DEBUG ONLY
    def __fill_cell(self, i, j, color: str):
        if 0 <= i < self.__num_cols and 0 <= j < self.__num_rows:
            self.__cells[i][j].fill(color)
            self.__animate()

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_index_list = []
            print(f"Location: [{i}][{j}]")             # FOR DEBUG ONLY
            self.__fill_cell(i, j, "blue")             # FOR DEBUG ONLY

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
                print("Going LEFT")                    # FOR DEBUG ONLY
                self.__fill_cell(i, j, "lightblue")    # FOR DEBUG ONLY
            # right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
                print("Going RIGHT")                    # FOR DEBUG ONLY
                self.__fill_cell(i, j, "lightblue")    # FOR DEBUG ONLY                
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                print("Going UP")                      # FOR DEBUG ONLY
                self.__fill_cell(i, j, "lightblue")    # FOR DEBUG ONLY  
            # down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                print("Going DOWN")                    # FOR DEBUG ONLY
                self.__fill_cell(i, j, "lightblue")    # FOR DEBUG ONLY  

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                print("BREAK OUT!!")                   # FOR DEBUG ONLY
                self.__fill_cell(i, j, "red")          # FOR DEBUG ONLY  
                self.__draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
                self.__fill_cell(i, j, "green")                    # FOR DEBUG ONLY                  
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
                self.__fill_cell(i, j, "green")                    # FOR DEBUG ONLY                            
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
                self.__fill_cell(i, j, "green")                    # FOR DEBUG ONLY                            
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False
                self.__fill_cell(i, j, "green")                    # FOR DEBUG ONLY                            

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])
