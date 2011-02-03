#!/usr/bin/env python2.3

import OpenGL
import sys
OpenGL.ERROR_ON_COPY = True
from OpenGL.GL import *
from OpenGL.GLUT import *


win_width = 200
win_height = 200

def draw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	## DRAW HERE

	glutSwapBuffers()

def reshape(width, height):
	w = width
	## do nothing for now

def init():
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_NORMALIZE)

def idle():
	glutPostRedisplay()

def visible(vis):
	if vis == GLUT_VISIBLE:
		glutIdleFunc(idle)
	else:
		glutIdleFunc(None)

def key(k,x,y):
	if k == GLUT_KEY_LEFT:
		a = 1
		##Moveleft
	if k == GLUT_KEY_RIGHT:
		a = 2
		##Moveright
	## ETC...



if __name__ == '__main__':
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

	glutInitWindowPosition(0,0)
	glutInitWindowSize(win_width, win_height)
	glutCreateWindow("The Game")
	init()

	glutDisplayFunc(draw)
	glutSpecialFunc(key)
	glutReshapeFunc(reshape)
	glutVisibilityFunc(visible)

	glutMainLoop()
	print "TEST"


