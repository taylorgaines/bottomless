"""
CY300 Project Initial Skeleton, AY19-1

Name: CDT William Gaines
x-Number:  x03651
File Name:  project.py
"""


import sys

import pygame, random
from pygame.locals import *

# Constant color definitions
		   #R    G    B
ORANGE =   (255, 128, 0)
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVY =     (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)  
LIME =     (0, 255, 0)
CYAN =     (0, 255, 255)
MAGENTA =  (255, 0, 255)
SILVER =   (192, 192, 192)
GRAY =     (128, 128, 128)
MAROON =   (128, 0, 0)
OLIVE =    (128, 128, 0)
TEAL =     (0, 128, 128)

COLOR_LIST = [ORANGE, BLUE, GREEN, PURPLE, RED, YELLOW, NAVY, WHITE, LIME, CYAN, MAGENTA, SILVER, GRAY, MAROON, OLIVE, TEAL]
RANDOM1 = random.choice(COLOR_LIST)
RANDOM2 = random.choice(COLOR_LIST)
if RANDOM1 == RANDOM2:
	RANDOM2.random.choice(COLOR_LIST)


def init_main_window(dimensions, caption):
	"""
	Initialize the main window.
	"""
	pygame.init()
	pygame.display.set_caption(caption)
	return pygame.display.set_mode(dimensions)

###############################################################################
	   
def load_circle_image():
	"""
	Load and return list of circle animation images.
	"""
	file_name = ['Ball.png']
	img = pygame.image.load(file_name)
	return img

###############################################################################

def move_circle(circle, event, dist, disp_surf):
	"""
	Update disp_surf with new location of circle based on keyboard event and
	distance moved.
	"""
	if event.key == K_RIGHT:
		circle.centerx = min(circle.centerx+dist, disp_surf.get_width())
	elif event.key == K_LEFT:
		circle.centerx = max(circle.centerx-dist, 0)
		
###############################################################################\       

def terminate():
	"""
	Closes the pygame window and exits the program.
	"""
	pygame.quit()
	sys.exit()

###############################################################################

def play_game():
	DISPLAYSURF = init_main_window((500, 500), 'Bottomless')

	# Adds Background Music
	pygame.mixer.music.load("loop.wav")
	pygame.mixer.music.play(-1)

	# optional key holding
	pygame.key.set_repeat(20,20)

	FPS = 30
	fps_clock = pygame.time.Clock()

	# Create Circle
	circle_image = pygame.image.load("Ball.png")			#(Creative Commons, Ball PNG Free Download)
	circle = circle_image.get_rect()
	circle.centerx = 250
	circle.centery = 100
	circleSpeed = 5

	#Create Bar
	obstacle = pygame.Surface((500, 20))
	obstacle.fill((RANDOM2))
	
	bar1 = obstacle.get_rect()
	bar1.centerx = 250

	bar2 = obstacle.get_rect()
	bar2.centerx = 250

	bar3 = obstacle.get_rect()
	bar3.centerx = 250

	bar4 = obstacle.get_rect()
	bar4.centerx = 250

	bar5 = obstacle.get_rect()
	bar5.centerx = 250

	bottomBar = obstacle.get_rect()
	bottomBar.centerx = 250

	# Create Opening
	opening = pygame.Surface((100, 20))
	opening.fill((RANDOM1))
	
	space1 = opening.get_rect()
	space1.centerx = 250
	space1.centery = 300
	space1Speed = -5

	space2 = opening.get_rect()
	space2.centerx = random.randint(50,450)
	space2.centery = 400
	space2Speed = -5

	space3 = opening.get_rect()
	space3.centerx = random.randint(50,450)
	space3.centery = 500
	space3Speed = -5

	space4 = opening.get_rect()
	space4.centerx = random.randint(50,450)
	space4.centery = 600
	space4Speed = -5

	space5 = opening.get_rect()
	space5.centerx = random.randint(50,450)
	space5.centery = 700
	space5Speed = -5

	# Initialize the score and set the font for displaying it.
	menu = True
	while menu == True:
		DISPLAYSURF.fill(RANDOM1)
		headerFont = pygame.font.SysFont('Times New Roman', 75)
		header = headerFont.render('Bottomless!', 1, (RANDOM2))
		lineFont = pygame.font.SysFont('Times New Roman', 25)
		line1Text = lineFont.render('Welcome. Control your ball with the right.', 1, (RANDOM2))
		line2Font = pygame.font.SysFont('Times New Roman', 25)
		line2Text = lineFont.render("and left arrow keys. Press 'Enter' to begin.", 1, (RANDOM2))
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_RETURN or event.key == K_KP_ENTER:
					startTime = pygame.time.get_ticks()
					print(startTime)
					menu = False
				elif event.key == K_ESCAPE:
					terminate()
		DISPLAYSURF.blit(header,(70, 80))
		DISPLAYSURF.blit(line1Text,(50, 250))
		DISPLAYSURF.blit(line2Text,(50, 300))
		pygame.display.flip()

	# Game Loop
	game = True
	while game == True:
		DISPLAYSURF.fill(RANDOM2)
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					terminate()
				else:
					move_circle(circle, event, 11, DISPLAYSURF)

		# draw a clean background before drawing images
		DISPLAYSURF.fill(RANDOM1)
		

		# Circle Movement
		if circle.top == 0:
			game = False
		if circle.bottom > space1.top and circle.bottom < space1.top + 25:
			if circle.centerx > space1.centerx+25 or circle.centerx < space1.centerx-25:
				circle.bottom = circle.bottom + space1Speed
				circle.bottom = space1.top
			else:
				circle.centery = circle.centery + circleSpeed
		elif circle.bottom > space2.top and circle.bottom < space2.top + 25:
			if circle.centerx > space2.centerx+25 or circle.centerx < space2.centerx-25:
				circle.bottom = circle.bottom + space2Speed
				circle.bottom = space2.top
			else:
				circle.centery = circle.centery + circleSpeed
		
		elif circle.bottom > space3.top and circle.bottom < space3.top + 25:
			if circle.centerx > space3.centerx+25 or circle.centerx < space3.centerx-25:
				circle.bottom = circle.bottom + space3Speed
				circle.bottom = space3.top
			else:
				circle.centery = circle.centery + circleSpeed

		elif circle.bottom > space4.top and circle.bottom < space4.top + 25:
			if circle.centerx > space4.centerx+25 or circle.centerx < space4.centerx-25:
				circle.bottom = circle.bottom + space4Speed
				circle.bottom = space4.top
			else:
				circle.centery = circle.centery + circleSpeed

		elif circle.bottom > space5.top and circle.bottom < space5.top + 25:
			if circle.centerx > space5.centerx+25 or circle.centerx < space5.centerx-25:
				circle.bottom = circle.bottom + space5Speed
				circle.bottom = space5.top
			else:
				circle.centery = circle.centery + circleSpeed
		elif circle.bottom >= 500:
			circle.bottom = 500
		else:
			circle.centery = circle.centery + circleSpeed

		# display space
		space1.centery = space1.centery + space1Speed
		if space1.centery == 0:
			space1.centery = 500
			space1.centerx = random.randint(50,450)
		bar1.centery = space1.centery

		space2.centery = space2.centery + space2Speed
		if space2.centery == 0:
			space2.centery = 500
			space2.centerx = random.randint(50,450)
		bar2.centery = space2.centery

		space3.centery = space3.centery + space3Speed
		if space3.centery == 0:
			space3.centery = 500
			space3.centerx = random.randint(50,450)
		bar3.centery = space3.centery

		space4.centery = space4.centery + space4Speed
		if space4.centery == 0:
			space4.centery = 500
			space4.centerx = random.randint(50,450)
		bar4.centery = space4.centery

		space5.centery = space5.centery + space5Speed
		if space5.centery == 0:
			space5.centery = 500
			space5.centerx = random.randint(50,450)
		bar5.centery = space5.centery

		currentTime = pygame.time.get_ticks()
		rawScore = currentTime - startTime
		score = str(rawScore // 1000)
		scoreFont = pygame.font.SysFont('Times New Roman', 200)
		scoreText = scoreFont.render(score, 1, (BLACK))

		#Display Shapes
		DISPLAYSURF.blit(obstacle, bar1)      
		DISPLAYSURF.blit(obstacle, bar2)      
		DISPLAYSURF.blit(obstacle, bar3)      
		DISPLAYSURF.blit(obstacle, bar4)      
		DISPLAYSURF.blit(obstacle, bar5)
		DISPLAYSURF.blit(opening, space1)
		DISPLAYSURF.blit(opening, space2)
		DISPLAYSURF.blit(opening, space3)
		DISPLAYSURF.blit(opening, space4)
		DISPLAYSURF.blit(opening, space5)
		DISPLAYSURF.blit(scoreText,(225, 200))
		DISPLAYSURF.blit(circle_image, circle)
		pygame.display.update()


		fps_clock.tick(FPS)

	gameOver = True
	while gameOver == True:
		DISPLAYSURF.fill(RANDOM1)
		headerFont = pygame.font.SysFont('Times New Roman', 70)
		header = headerFont.render('Final Score: ' + score, 1, (RANDOM2))
		lineFont = pygame.font.SysFont('Times New Roman', 25)
		line1Text = lineFont.render("Game Over.", 1, (RANDOM2))
		line2Font = pygame.font.SysFont('Times New Roman', 25)
		line2Text = lineFont.render("Press 'Enter' to quit.", 1, (RANDOM2))
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_RETURN or event.key == K_KP_ENTER:
					startTime = pygame.time.get_ticks()
					print(startTime)
					gameOver = False
				elif event.key == K_ESCAPE:
					terminate()
		DISPLAYSURF.blit(header,(30, 80))
		DISPLAYSURF.blit(line1Text,(185, 250))
		DISPLAYSURF.blit(line2Text,(150, 300))
		pygame.display.flip()
###############################################################

if __name__ == '__main__':
  play_game()