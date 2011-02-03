#!/usr/bin/env python2.3

class world(object):
	def __init__(self, w_m):
		self.length = 100	#Block length of level world
		self.height = 50	#Percentage of walkable screen
		self.template = w_m
		self.bg_image = None	#BG image, will be pulled from world_map
		self.floor_image = None	#Floor image, ****
		self.extra_images = None#Images of customizable stuff defined
		

class world_map(object):
	def __init__(self, directory):
		self.file_locations = directory
