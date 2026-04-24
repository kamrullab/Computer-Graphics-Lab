from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np  

# DDA Algorithm
def DDA(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1    

    if dx == 0:
        for y in range(y1, y2 + 1):
            points.append((x1, y))
        return points

    m = dy / dx
    y = y1

    if abs(dx) >= abs(dy):
        for x in range(x1, x2 + 1):
            points.append((round(x), round(y)))
            y += m
    else:
        x = x1
        step = 1 / m
        for y in np.arange(y1, y2 + 1, 1):
            points.append((round(x), round(y)))
            x += step
    return points


# Bresenham Algorithm (adjusted for all directions)
def Bresenham(x0, y0, x1, y1):
    points = []

    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy

    while True:
        points.append((x0, y0))

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x0 += sx

        if e2 < dx:
            err += dx
            y0 += sy

    return points


def show():
    glClear(GL_COLOR_BUFFER_BIT)          # Clear window

    glColor3f(0.0, 0.0, 0.0)              # Set drawing color (black)
    glBegin(GL_POINTS)                    # Start drawing points

    # Line 1 using DDA
    points1 = DDA(100,100,300,300)
    for x,y in points1:
        glVertex2i(x,y)

    # Line 2 using Bresenham (intersecting line)
    points2 = Bresenham(300,100,100,300)
    for x,y in points2:
        glVertex2i(x,y)

    glEnd()                               # End drawing
    glutSwapBuffers()                     # Refresh window


# Main setup
glutInit()                                # Initialize GLUT
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)  # Set display mode
glutInitWindowSize(500, 500)              # Set window size
glutCreateWindow(b"Kamrul_43")            # Set window title (Name_Roll)

glClearColor(1.0, 1.0, 1.0, 1.0)          # Set background color (white)
gluOrtho2D(0, 500, 0, 500)                # Define 2D coordinate system

glutDisplayFunc(show)                     # Register display function
glutMainLoop()                            # Start main loop