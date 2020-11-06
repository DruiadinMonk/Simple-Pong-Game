# Pong Game



# MODULES
import pygame
import random
from ball import Ball 		# From ball file, import item 'Ball'.
from paddle import Paddle 	# From paddle file, import item 'Paddle'.


# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 800, 400
window = pygame.display.set_mode((WIN_X, WIN_Y)) 	# Window
pygame.display.set_caption("Pong")
font = pygame.font.Font('freesansbold.ttf', 32) 	# Text for scores.
clock = pygame.time.Clock()
run = True 		
FPS = 60
score_1 = 0	
score_2 = 0



# COLORS
WHITE  = (255, 255, 255)
BLACK  = (  0,   0,   0)
L_GRAY = (175, 175, 175)



# INITIALIZE OBJECTS
rx = random.randint(0, 1) 	# Randomize ball 'x'.
ry = random.randint(0, 1)	# Randomize ball 'y'.

if (rx == 0):
	rx = -1
else: 	# r1 == 1...
	rx = 1

if (ry == 0):
	ry = -1
else: 	# r1 == 1...
	ry = 1

ball = Ball(window, WHITE, 400, 200, 10, 2 * rx, 2 * ry)
p1   = Paddle(window, WHITE,  25, 175,  25, 225, 5)
p2   = Paddle(window, WHITE, 775, 175, 775, 225, 5)



# MAIN LOOP
while run:

	# # INITIALIZE
	clock.tick(FPS) 		# Timer
	window.fill(0) 			# BACKGROUND: BLACK	
	keys = pygame.key.get_pressed() 	# PLAYER MOVEMENT


	# EACH EVENT
	for event in pygame.event.get():

		# IF WINDOW EXIT
		if event.type == pygame.QUIT:
			run = False


	# BOUNDARIES: Top / Bottom
	pygame.draw.rect(window, L_GRAY, (0,     0, WIN_X, 10))
	pygame.draw.rect(window, L_GRAY, (0, WIN_Y - 10, WIN_X, 10))


	# MIDDLE DIVIDER
	for i in range(7):
		pygame.draw.rect(window, (25, 25, 25), (395,  30 + (i * 50), 10, 40))


	# PADDLE 1
	if keys[pygame.K_w] and p1.y1 > 12:
		p1.y1 -= 3
		p1.y2 -= 3
	if keys[pygame.K_s] and p1.y1 < 338:
		p1.y1 += 3
		p1.y2 += 3

	# PADDLE 2
	if keys[pygame.K_UP] and p2.y1 > 12:
		p2.y1 -= 3
		p2.y2 -= 3
	if keys[pygame.K_DOWN] and p2.y1 < 338:
		p2.y1 += 3
		p2.y2 += 3


	# COLLISION: Walls
	if ball.y <= 20 or ball.y >= 380:
		ball.vel_y *= -1 	# Change 'Y' velocity. (Bounce off.)

	# COLLISION: Paddles
	if ball.x <= p1.x1+15 and ball.y >= p1.y1 and ball.y <= p1.y1+50: 	# Player 1
		ball.vel_x *= -1

	if ball.x >= p2.x1-10 and ball.y >= p2.y1 and ball.y <= p2.y1+50: 	# Player 2
		ball.vel_x *= -1


	# DRAW OBJECTS
	ball.drawBall()
	ball.moveBall()
	p1.drawPaddle()
	p2.drawPaddle()


	# SCORE: If ball either passes left or right side...
	if ball.x <= 0 - ball.radius or ball.x >= 800 + ball.radius:

		# Check Left or Right side for score update.
		if ball.x < 400: 	# Left
			score_1 += 1
		else: 				# Right
			score_2 += 1

		# RESET BALL
		ball.x = 400		# Reset ball.x
		ball.y = 200 		# Reset ball.y
		ball.vel_x *= -1 	# Give serve to other player.

		# Randomize either up or down.
		r = random.randint(0, 1)
		if (r == 0):
			r = -1
		else: 	# r1 == 1...
			r = 1

		ball.vel_y *= r 	# Give serve to other player, moving either up or down.


	# DRAW SCORES
	font = pygame.font.SysFont(None, 108)
	s1 = font.render(str(score_1), True, WHITE)
	s2 = font.render(str(score_2), True, WHITE)
	window.blit(s1, (275, 25))
	window.blit(s2, (475, 25))


	# UPDATE WINDOW
	pygame.display.update()


# END LOOP



# IF MAIN LOOP == FALSE, QUIT.
pygame.quit()
