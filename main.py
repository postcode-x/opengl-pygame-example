import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


x_vertices = [0, 0, 0, 70, 0, 0, 58, 14, 0, 105, 62, 0, 115, 14, 0, 102, 0, 0, 170, 0, 0, 154, 15, 0, 139, 95, 0, 232,
              190, 0, 159, 190, 0, 174, 173, 0, 128, 127, 0, 120, 173, 0, 141, 190, 0, 59, 190, 0, 83, 173, 0, 97,
              97, 0, 0, 0, 0]
x_depth = 16
J = []

# THESE ARE THE LINES THAT JOIN BOTH FACES
for i in range(0, round(len(x_vertices)/3)):

    J.append(x_vertices[3*i])
    J.append(x_vertices[3*i + 1])
    J.append(x_vertices[3*i + 2])

    J.append(x_vertices[3*i])
    J.append(x_vertices[3*i + 1])
    J.append(x_depth)


# MAIN WIREFRAME LOGIC
def x_wireframe():

    glLineWidth(2.0)
    glEnableClientState(GL_VERTEX_ARRAY)

    # FIRST FACE
    glVertexPointer(3, GL_FLOAT, 0, x_vertices)
    glDrawArrays(GL_LINE_STRIP, 0, 19)

    # TRANSLATE TO ACCOMMODATE SECOND FACE
    glTranslatef(0, 0, -x_depth)

    # SECOND FACE
    glVertexPointer(3, GL_FLOAT, 0, x_vertices)
    glDrawArrays(GL_LINE_STRIP, 0, 19)

    # JOINS
    glVertexPointer(3, GL_FLOAT, 0, J)
    glDrawArrays(GL_LINES, 0, 36)

    glDisableClientState(GL_VERTEX_ARRAY)


def main():

    pygame.init()
    display = (800, 600)
    window = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(100, (display[0]/display[1]), 0, 400.0)
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    angle = 0
    n = 2.8333333333   # -> 17/6

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glPushMatrix()

        glRotatef((74-angle*0.5)*-n, 0, 0, 1)  # 4) Rotate the object around z axis
        glRotatef((74-angle*0.5)*-6*n, 0, 1, 0)  # 3) Rotate the object around y axis
        glRotatef((74-angle*0.5)*2*n, 1, 0, 0)  # 2) Rotate the object around x axis
        glTranslatef(-232 / 2, -190 / 2, x_depth / 2)  # 1) Center object

        x_wireframe()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(15)

        angle = angle + 0.4


main()
