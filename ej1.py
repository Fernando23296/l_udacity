
'''
import webbrowser
import time
time.sleep(5)
webbrowser.open("https://www.youtube.com/watch?v=fFu-s8wzlIw")
'''
import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor("white")
	x=0
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	while (x<4):
		brad.forward(100)
		brad.right(90)
		x=x+1

def draw_circ_squ():
	window = turtle.Screen()
	window.bgcolor("white")
	x=0
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	y=0
	while(y<30):
		angle=90
		while (x<4):
			brad.forward(100)
			brad.right(angle)
			x=x+1
		angle=angle+3
		y=y+1

def draw_circle():
	angie=turtle.Turtle()
	angie.shape("turtle")
	angie.circle(100)
	window.exitonclick()

def draw_triangle():
	beto=turtle.Turtle()
	beto.shape("turtle")
	x=0
	while (x<3):
		beto.forward(100)
		beto.right(120)
		x=x+1
	window.exitonclick()

draw_circ_squ()