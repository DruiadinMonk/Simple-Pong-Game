# Paddle class for the game Pong.

# MODULES
import pygame


# CLASS
class Paddle:

	# INITALIZE
	def __init__(self, window, color, x1, y1, x2, y2, width):
		self.window = window
		self.color  = color
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.width = width

	# DRAW PADDLES
	def drawPaddle(self):
		pygame.draw.line(self.window, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)
