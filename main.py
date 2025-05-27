from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(200,500)
    point_2 = Point(400,70) 
    point_3 = Point(80,100) 
    line1 = Line(point_1,point_2)
    win.draw_line(line1,"red")
    line2 = Line(point_3,point_2)
    win.draw_line(line2,"black")
    win.wait_for_close()

main()