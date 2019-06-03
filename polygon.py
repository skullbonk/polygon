import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Cube:
    vertices = [
        # bottom
        (-1, -1, 1),  # 0 - back left
        (1, -1, 1),  # 1 - back right
        (1, -1, -1),  # 2 - front left
        (1, -1, -1),  # 3 - front right
        # top
        (-1, 1, 1),  # 4 - back left
        (1, 1, 1),  # 5 - back right
        (-1, 1, -1),  # 6 - front left
        (1, 1, -1)  # 7 - front right
    ]

    edges = (
        # bottom
        (0, 1),
        (1, 3),
        (3, 2),
        (2, 0),
        # top
        (4, 5),
        (5, 7),
        (7, 6),
        (6, 4),
        # struts
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7)
    )

    def __init__(self):
        self.vertices = Cube.vertices
        self.edges = Cube.edges

    def draw(self):
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0, 1, 0)


def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    glTranslatef(0, 0, -8)

    polygon = Cube()
    clock = pygame.time.Clock()
    # CHANGE THIS TO DRAW DIFFERENT STUFF
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(2, 1, 1, 3)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        polygon.draw()
        pygame.display.flip()


main()
