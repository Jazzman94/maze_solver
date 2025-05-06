from ui import Window, Point, Line

class Cell:
    def __init__(self, win: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
    
    def center(self) -> Point:
        if self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None:
            raise ValueError("Cell coordinates are not set.")
        x_center = self._x1 + (self._x2 - self._x1) // 2
        y_center = self._y2 + (self._y1 - self._y2) // 2
        return Point(x_center, y_center)
    
    def draw_move(self, to_cell: 'Cell', undo=False):
        color = "red"
        if undo:
            color = "gray"
        
        cell_center = self.center()
        other_center = to_cell.center()

        line = Line(cell_center, other_center)
        self._win.draw_line(line, color)


        