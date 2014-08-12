from __future__ import print_function
import random


class Dealer(object):
    """ https://en.wikipedia.org/wiki/Rack-O """

    def __init__(self, num_cards, players):
        if len(players) < 2 or len(players) > 4:
            raise ValueError("Rack-o requires 2-4 players")
        self.players = players

        if num_cards not in [40, 50, 60]:
            raise ValueError("The number of cards must be 40, 50, or 60")
        self.num_cards = num_cards
        self.round = 0
        self.discard_deck = []

    def shuffle_deck(self):
        return random.sample(range(1, 60), self.num_cards-1)

    def draw_card(self):
        if len(self.deck) > 0:
            card = self.deck[-1]
            print("Card drawn: %s" % card)
            return card
        else:
            raise Exception("No more cards in deck!")

    def give_discard(self, card):
        if card == self.discard_deck[-1]:
            del self.discard_deck[-1]
        else:
            raise Exception("Card %s not at top of discard deck" % card)

    def give_card(self, card):
        if card == self.deck[-1]:
            del self.deck[-1]
        else:
            raise Exception("Card %s not at top of deck" % card)

    def discard(self, deck, card):
        if len(deck) > 0:
            discard = deck.pop(deck.index(card))
            print("Card discarded: %s" % discard)
            self.discard_deck.append(discard)
            #self.next_turn()
            return discard
        else:
            raise Exception("No more cards in deck")

    def top_discard(self):
        return self.discard_deck[-1]

    def deal(self):
        print("Stating game!\nShuffling deck!")
        self.deck = self.shuffle_deck()
        for player in self.players:
            player.hand(self.deck[-10:])
            print("%s got their cards!" % player)
            print(player.hand)
            del self.deck[-10:]
        self.discard(self.deck, self.draw_card())
        self.next_turn()

    def next_turn(self):
        if hasattr(self, "current_player"):
            player_index = self.players.index(self.current_player)
            if player_index + 1 == len(self.players):
                self.current_player = self.players[0]
                self.round += 1
                print("Round: %s" % self.round)
            else:
                self.current_player = self.players[player_index + 1]
        else:
            self.current_player = self.players[0]

        print("It is %s turn" % self.current_player)
        self.current_player.my_turn(self)