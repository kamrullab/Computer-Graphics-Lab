from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def show():
    glClear(GL_COLOR_BUFFER_BIT)   # Clear window

    # Bottom-left: small green square
    glColor3f(0.0, 1.0, 0.0)       # Green color
    glBegin(GL_QUADS)
    glVertex2f(50, 50)
    glVertex2f(150, 50)
    glVertex2f(150, 150)
    glVertex2f(50, 150)
    glEnd()

    # Top-right: large purple triangle
    glColor3f(1.0, 0.0, 1.0)       # Purple color
    glBegin(GL_TRIANGLES)
    glVertex2f(400, 400)
    glVertex2f(550, 400)
    glVertex2f(475, 550)
    glEnd()

    # Top-left: rectangle using two triangles (different colors)
    glBegin(GL_TRIANGLES)

    # First triangle (Yellow)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(50, 400)
    glVertex2f(250, 400)
    glVertex2f(250, 550)

    # Second triangle (Blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50, 400)
    glVertex2f(50, 550)
    glVertex2f(250, 550)

    glEnd()

    # Bottom-right: small orange pentagon
    glColor3f(1.0, 0.5, 0.0)       # Orange color
    glBegin(GL_POLYGON)
    glVertex2f(400, 50)
    glVertex2f(500, 50)
    glVertex2f(550, 100)
    glVertex2f(500, 150)
    glVertex2f(400, 100)
    glEnd()

    glutSwapBuffers()              # Refresh window


# Main setup
glutInit()                                    # Initialize GLUT
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(600, 600)                  # Window size
glutCreateWindow(b"Kamrul_43")                # Window title

glClearColor(1.0, 1.0, 1.0, 1.0)              # White background
gluOrtho2D(0, 600, 0, 600)                   # 2D coordinate system

glutDisplayFunc(show)                         # Display function
glutMainLoop()                               # Start program