from random import *
import pygame

class Area:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.area = []
		self.lines_cleared = 0
		self.score = 0


		array_builder = []
		for row in range(int(self.height/20)):
			for column in range(int(self.width/20)):
				array_builder.append(0)
			self.area.append(array_builder)
			array_builder = []

	def matrix(self):
		return self.area

	def draw(self, shape, matrix, screen):
		self.check_state(shape, matrix)
		solid_color = (50,50,50)
		solid = pygame.image.load("outside.png").convert()
		solid.fill(solid_color,(1,1,18,18))
		for row, row_items in enumerate(matrix):
			for column, item in enumerate(row_items):
				x, y = column, row
				if item == 1:
					screen.blit(solid,(x*20, y*20))
					
	def draw_next_shape(self,shape,screen):
		for index, item in enumerate(shape.x):
			screen.blit(shape.block, ((shape.x[index])*20, shape.y[index]*20))

	# Checks whether the shape needs to become part of the matrix
	# also checks if any lines need to be cleared.
	def check_state(self, shape, matrix):
		if shape.state == 1:
			for ind, i in enumerate(shape.x):
				if matrix[shape.y[ind]][shape.x[ind]] == 0:
					matrix[shape.y[ind]][shape.x[ind]] = 1
		
		old_lines_cleared = self.lines_cleared
		count = 0
		update_score = 0
		for row, row_items in enumerate(matrix):
			if sum(row_items) == 10:
				matrix.pop(row)
				matrix.reverse()
				matrix.append([0]*10)
				matrix.reverse()
				self.lines_cleared += 1
				count += 1
				update_score = 1
		
		if update_score == 1:
			self.score += (self.lines_cleared - old_lines_cleared) * count * 100

	def print_game_info(self, screen):
		myfont = pygame.font.SysFont("monospace", 16)
		font_color = (255,255,0)
		# render text
		label_1 = myfont.render("Lines", 1, font_color)
		label_1_rect = label_1.get_rect()
		label_1_rect.center = (250, self.height/8*7 - 20)

		label_2 = myfont.render("Cleared:", 1, font_color)
		label_2_rect = label_2.get_rect()
		label_2_rect.center = (250, self.height/8*7)

		lines = myfont.render("%i" % self.lines_cleared, 1, font_color)
		lines_rect = lines.get_rect()
		lines_rect.center = (250, self.height/8*7 + 20)

		score_1 = myfont.render("Your", 1, font_color)
		score_1_rect = score_1.get_rect()
		score_1_rect.center = (250, self.height/2 - 20)

		score_2 = myfont.render("Score:", 1, font_color)
		score_2_rect = score_2.get_rect()
		score_2_rect.center = (250, self.height/2)

		score = myfont.render("%i" % self.score, 1, font_color)
		score_rect = score.get_rect()
		score_rect.center = (250, self.height/2 + 20)

		screen.blit(label_1, label_1_rect)
		screen.blit(label_2, label_2_rect)
		screen.blit(lines, lines_rect)

		screen.blit(score_1, score_1_rect)
		screen.blit(score_2, score_2_rect)
		screen.blit(score, score_rect)





