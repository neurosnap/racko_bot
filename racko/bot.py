from __future__ import print_function


class Player(object):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "<Player %s>" % self.name

    def hand(self, cards):
        self.hand = cards

    def my_turn(self, dealer):
        print(self.hand)
        low, high = self.get_hand_avg()
        #print("Low Card Avg: %s" % low)
        #print("High Card Avg: %s" % high)

        take_discard = False
        top_discard = dealer.top_discard()
        take_discard = self.find_place(self.hand, top_discard)

        if take_discard:
            self.exchange_discard(dealer, take_discard, top_discard)
        else:
            take_drawn_card = False
            drawn_card = dealer.draw_card()
            take_drawn_card = self.find_place(self.hand, drawn_card)

            if take_drawn_card:
                self.exchange_card(dealer, take_drawn_card, drawn_card)
            else:
                dealer.discard(dealer.deck, drawn_card)

        print(self.hand)
        print("--------\n")
        if self.call_racko():
            print("RACKO!")
        else:
            dealer.next_turn()

    def find_place(self, arr, new_card):

        if arr[0] > 15 and new_card < 15:
            return arr[0]

        if arr[9] < 45 and new_card > 45:
            return arr[9]

        if is_asc_order(arr[0:5]) and new_card > arr[4] and new_card <= 30:
            return arr[5]

        if new_card >= 30 and not is_asc_order(arr[5:10]):
            for index, card in enumerate(arr[5:10]):
                """if index != 0 and index != 4:
                    prev_card = arr[index - 1]
                    next_card = arr[index + 1]
                    delta_card = abs(next_card - prev_card)
                    if delta_card <= 10:
                        print("delta!")
                        return next_card"""
                if new_card < card:
                    if index in [0,1,2,3]:
                        print("new card %s < card" % new_card)
                        return card
                elif card < 30 and new_card > arr[index - 1]:
                    print("card < 30")
                    return card

        if new_card <= 30 and not is_asc_order(arr[0:5]):
            for index, card in enumerate(arr[0:5]):
                """if index != 0 and index != 4:
                    prev_card = arr[index - 1]
                    next_card = arr[index + 1]
                    delta_card = abs(next_card - prev_card)
                    if delta_card <= 10:
                        print("delta!")
                        return next_card"""
                if new_card < card:
                    if index in [1,2,3,4]:
                        if abs(new_card - arr[index - 1]) <= 5 and new_card > arr[index - 1]:
                            print("new card %s < card" % new_card)
                            return card
                    else:
                        return card
                elif index in [1,2,3,4] and card <= 5 and arr[0] > 5:
                    print("Index 1-4 and card <= 5")
                    return card

        return False

    def exchange_discard(self, dealer, old_card, new_card):
        if old_card in self.hand:
            dealer.give_discard(new_card)
            replace_index = self.hand.index(old_card)
            self.hand[replace_index] = new_card
            dealer.discard_deck.append(old_card)
            print("Exchanged %s card from discard deck for %s" % (old_card, new_card))
        else:
            raise Exception("Old card %s not found in hand" % old_card)

    def exchange_card(self, dealer, old_card, new_card):
        if old_card in self.hand:
            dealer.give_card(new_card)
            replace_index = self.hand.index(old_card)
            self.hand[replace_index] = new_card
            dealer.discard_deck.append(old_card)
            print("Exchanged %s card from deck for %s" % (old_card, new_card))
        else:
            raise Exception("Old card %s not found in hand" % old_card)

    def call_racko(self):
        return self.hand == sorted(self.hand)

    def get_hand_avg(self):
        low = reduce(lambda x, y: x + y, self.hand[0:5]) / 5
        high = reduce(lambda x, y: x + y, self.hand[5:10]) / 5
        return low, high

def is_asc_order(arr):
    return arr == sorted(arr)