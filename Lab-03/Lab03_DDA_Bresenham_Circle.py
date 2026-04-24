from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


# -------- Draw Text on Screen --------
def drawText(x, y, text):
    glRasterPos2f(x, y)   # set position for text
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))  # draw character


# -------- DDA Line Drawing --------
def DDA(x1, y1, x2, y2):
    points = []  # store points

    dx = x2 - x1   # difference in x
    dy = y2 - y1   # difference in y

    steps = int(max(abs(dx), abs(dy)))   # total steps

    x_inc = dx / steps   # x increment
    y_inc = dy / steps   # y increment

    x, y = x1, y1   # starting point

    for i in range(steps):
        points.append((round(x), round(y)))   # add point
        x += x_inc   # move x
        y += y_inc   # move y

    return points


# -------- Bresenham Line --------
def BresenhamLine(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)   # change in x
    dy = abs(y1 - y0)   # change in y

    sx = 1 if x0 < x1 else -1   # x direction
    sy = 1 if y0 < y1 else -1   # y direction

    err = dx - dy   # decision parameter

    while True:
        points.append((x0, y0))   # plot point

        if x0 == x1 and y0 == y1:
            break   # stop when reached end

        e2 = 2 * err   # calculate error

        if e2 > -dy:
            err -= dy
            x0 += sx   # move in x direction

        if e2 < dx:
            err += dx
            y0 += sy   # move in y direction

    return points


# -------- Bresenham Circle --------
def drawCircle(cx, cy, r):
    points = []

    x = 0
    y = r
    d = 3 - 2 * r   # initial decision parameter

    while x <= y:
        # 8-way symmetry points
        pts = [
            (cx+x, cy+y), (cx-x, cy+y),
            (cx+x, cy-y), (cx-x, cy-y),
            (cx+y, cy+x), (cx-y, cy+x),
            (cx+y, cy-x), (cx-y, cy-x)
        ]
        points.extend(pts)

        if d < 0:
            d += 4*x + 6
        else:
            d += 4*(x-y) + 10
            y -= 1

        x += 1

    return points


# -------- Display Function --------
def show():
    glClear(GL_COLOR_BUFFER_BIT)   # clear screen

    # -------- DDA Line --------
    start = time.time()   # start time
    dda_points = DDA(100,100,300,300)   # get points
    dda_time = (time.time() - start) * 1000000   # convert to microsecond

    glPointSize(3.0)   # thickness
    glBegin(GL_POINTS)

    glColor3f(1,0,0)   # red color
    for x,y in dda_points:
        glVertex2i(x,y)   # draw pixel

    glEnd()

    # -------- Delay --------
    time.sleep(3)   # wait 3 seconds

    # -------- Bresenham Line --------
    start = time.time()
    bres_points = BresenhamLine(300,100,100,300)
    bres_time = (time.time() - start) * 1000000

    glBegin(GL_POINTS)

    glColor3f(0,0,1)   # blue color
    for x,y in bres_points:
        glVertex2i(x,y)

    glEnd()

    # -------- Circle --------
    glPointSize(2.0)   # thinner
    glBegin(GL_POINTS)

    glColor3f(0,0,0)   # black
    circle = drawCircle(250,250,10)   # exact center
    for x,y in circle:
        glVertex2i(x,y)

    glEnd()

    # -------- Show Time --------
    glColor3f(0,0,0)

    drawText(50,560, f"DDA Time: {round(dda_time,2)} us")
    drawText(50,530, f"Bresenham Time: {round(bres_time,2)} us")

    glutSwapBuffers()   # update screen


# -------- Main Function --------
glutInit()   # initialize GLUT
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)   # display mode
glutInitWindowSize(600,600)   # window size
glutCreateWindow(b"Kamrul_43")   # window title

glClearColor(1,1,1,1)   # background white
gluOrtho2D(0,600,0,600)   # coordinate system

glutDisplayFunc(show)   # set display function
glutMainLoop()   # run program