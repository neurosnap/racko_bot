import random


class Racko(object):
	""" https://en.wikipedia.org/wiki/Rack-O """

	def __init__(self, num_cards, num_players):
		if num_players < 2 or num_players > 4:
			raise ValueError("Rack-o requires 2-4 players")
		self.num_players = num_players

		if num_cards not in [40, 50, 60]:
			raise ValueError("The number of cards must be 40, 50, or 60")
		self.num_cards = num_cards

	def shuffle_deck(self):
		return random.sample(range(1, 60), self.num_cards)

	def draw_card(self):
		if self.deck:
			return self.deck.pop()

	def deal(self):
		self.deck = self.shuffle_deck()
		deal = [self.deal() for player in num_players]
		self.draw_card()