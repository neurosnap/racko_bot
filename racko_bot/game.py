import random


class Dealer(object):
	""" https://en.wikipedia.org/wiki/Rack-O """

	def __init__(self, num_cards, num_players):
		if num_players < 2 or num_players > 4:
			raise ValueError("Rack-o requires 2-4 players")
		self.num_players = num_players

		if num_cards not in [40, 50, 60]:
			raise ValueError("The number of cards must be 40, 50, or 60")
		self.num_cards = num_cards
		self.discard_deck = []

	def shuffle_deck(self):
		return random.sample(range(1, 60), self.num_cards-1)

	def draw_card(self):
		if self.deck:
			self.discard_deck.append(self.deck.pop())

	def top_card(self):
		return self.discard_deck[-1]

	def deal(self):
		self.deck = self.shuffle_deck()
		dealt = []
		for player in range(0, self.num_players):
			dealt.append(self.deck[-10:])
			del self.deck[-10:]
		self.draw_card()
		return dealt