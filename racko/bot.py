from __future__ import print_function


class Player(object):

	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		if self.name == other.name:
			return True
		else:
			return False

	def __str__(self):
		return "<Player %s>" % self.name

	def hand(self, cards):
		self.hand = cards

	def my_turn(self, top_card):
		print("my turn!")