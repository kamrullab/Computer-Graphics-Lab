from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 600, 600

boundary_color = [0.0, 0.0, 0.0]
fill_color = [1.0, 0.0, 0.0]


# -------- Color Compare --------
def isSameColor(c1, c2):
    return all(abs(c1[i] - c2[i]) < 0.05 for i in range(3))


# -------- Get Pixel --------
def getPixel(x, y):
    glFlush()
    data = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    return list(data[0][0])


# -------- Set Pixel --------
def setPixel(x, y, color):
    glColor3f(*color)
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


# -------- Boundary Fill --------
def boundaryFill(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        current = getPixel(x, y)

        if not isSameColor(current, boundary_color) and not isSameColor(current, fill_color):

            setPixel(x, y, fill_color)

            # 4 direction
            stack.append((x+1, y))
            stack.append((x-1, y))
            stack.append((x, y+1))
            stack.append((x, y-1))


# -------- Draw Shape --------
def drawShape():
    glColor3f(0,0,0)
    glLineWidth(5.0)   # 🔥 thicker boundary

    glBegin(GL_LINE_LOOP)
    glVertex2i(200,200)
    glVertex2i(400,200)
    glVertex2i(400,400)
    glVertex2i(200,400)
    glEnd()


# -------- Mouse --------
def mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        y = height - y

        # 🔥 STRICT AREA CHECK
        if 200 < x < 400 and 200 < y < 400:
            boundaryFill(x, y)
            glFlush()


# -------- Display --------
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    drawShape()
    glFlush()


# -------- Main --------
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(width, height)
glutCreateWindow(b"Kamrul_43")

glClearColor(1,1,1,1)
gluOrtho2D(0, width, 0, height)

glutDisplayFunc(display)
glutMouseFunc(mouse)

glutMainLoop()