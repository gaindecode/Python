import turtle
import os

import signal
import sys 

my_turtle = turtle.Turtle()
size = 200
while 1:
	my_turtle.forward(size)
	my_turtle.left(144)
	my_turtle.forward(size)
	my_turtle.left(144)
	my_turtle.forward(size)
	my_turtle.left(144)
	my_turtle.forward(size)
	my_turtle.left(144)
	my_turtle.forward(size)
	my_turtle.left(144) 

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

raw_input()




signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
signal.pause()
