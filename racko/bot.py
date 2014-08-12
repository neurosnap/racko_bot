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

    def my_turn(self, game):
        print("my turn!")
        print("Check Racko: %s" % self.check_racko())
        low, high = self.get_hand_avg()
        print("Low Card Avg: %s" % low)
        print("High Card Avg: %s" % high)
        if low < 30:
            if game.top_card() < 30:
                pass
            else:
                draw = game.draw_card()
                if draw < 30:
                    self.take_card(game, draw)

        game.top_card()
        game.draw_card()

    def take_card(self, game, card):
        found_card = game.deck.index(card)


    def check_racko(self):
        points = 0
        for index, card in enumerate(self.hand):
            next_i = index + 1
            if (next_i < len(self.hand)
                and card < self.hand[next_i]):
                    points += 1
                    continue
        return points

    def get_variance_avg(self):
        pass

    def get_hand_avg(self):
        low = reduce(lambda x, y: x + y, self.hand[0:4]) / 5
        high = reduce(lambda x, y: x + y, self.hand[5:9]) / 5
        return low, high