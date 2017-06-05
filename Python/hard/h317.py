# 02/06/2017
import itertools
from collections import Counter 

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def rank(self):
        return "234567890JQKA".index(self.value)

class Hand(object):
    def __init__(self, cards):
        assert len(cards) == 5

        self.cards = cards
        self.name = None
        self.tier = None
        self.get_type()
        self.sort_cards()

    def get_suits(self):
        return [card.suit for card in self.cards]
    
    def get_values(self):
        return [card.value for card in self.cards]
        
    def get_type(self):
        if len(set(self.get_suits())) == 1 and self.have_consecs():
            self.name = "Straight Flush"
            self.tier = 9
        elif max(Counter(self.get_values()).values()) == 4:
            self.name = "Four of a Kind"
            self.tier = 8
        elif set(Counter(self.get_values()).values()) == {3, 2}:
            self.name = "Full House"
            self.tier = 7
        elif len(set(self.get_suits())) == 1:
            self.name = "Flush"
            self.tier = 6
        elif self.have_consecs():
            self.name = "Straight"
            self.tier = 5
        elif set(Counter(self.get_values()).values()) == {3, 1}:
            self.name = "Three of a Kind"
            self.tier = 4
        elif list(Counter(self.get_values()).values()).count(2) == 2:
            self.name = "Two Pairs"
            self.tier = 3
        elif len(set(self.get_values())) == 4:
            self.name = "Pair"
            self.tier = 2
        else:
            self.name = "Highest Card"
            self.tier = 1

    def sort_cards(self):
        if self.name in ["Straight Flush", "Straight"]:
            self.cards.sort(key=Card.rank, reverse=True)
            if 'A' in self.get_values() and '2' in self.get_values():
                self.cards = self.cards[1:] + [self.cards[0]]

        elif self.name in ["Four of a Kind", "Full House", "Three of a Kind", "Pair"]:
            x_of_this = Counter(self.get_values()).most_common(1)[0][0]
            tmp = [card for card in self.cards if card.value == x_of_this]
            self.cards = tmp + sorted([card for card in self.cards if card.value != x_of_this],
                                      key=Card.rank, reverse=True)

        elif self.name in ["Flush", "Highest Card"]:
            self.cards.sort(key=Card.rank, reverse=True)

        elif self.name == "Two Pairs":
            pairs = [v for v, _ in Counter(self.get_values()).most_common(2)]
            tmp = sorted([card for card in self.cards if card.value in pairs], key=Card.rank, reverse=True)
            self.cards = tmp + [card for card in self.cards if card.value not in pairs]

    def have_consecs(self):
        value_list = "A234567890JQKA"
        possibles = []
        for i in range(1+len(value_list)-5):
            possibles.append(value_list[i:i+5])

        sorted_values = sorted(self.get_values(), key=lambda x: "234567890JQKA".index(x))
        if 'A' in self.get_values() and '2' in self.get_values():
            sorted_values = [sorted_values[-1]] + sorted_values[:-1]
        return ''.join(sorted_values) in possibles

    def __eq__(self, other):
        if self.tier == other.tier:
            for card_s, card_o in zip(self.cards, other.cards):
                if card_s.rank() != card_o.rank():
                    return False
            return True
        return False

    def __lt__(self, other):
        if self.tier < other.tier:
            return True
        elif self.tier == other.tier:
            for card_s, card_o in zip(self.cards, other.cards):
                if card_s.rank() < card_o.rank():
                    return True
                elif card_s.rank() > card_o.rank():
                    return False
        return False

def get_available_cards(flop, hands):
    deck = [Card(v, s) for v in "234567890JQKA" for s in "CSDH"
            if not any(c.suit == s and c.value == v for c in flop + hands)]
    return deck

def parse_cards(string):
    hand = [Card(v, s) for v, s in zip(string[::2], string[1::2])]
    return hand

def get_best_hand(cards):
    best_hand = None
    for hand in itertools.combinations(cards, 5):
        this_hand = Hand(list(hand))
        if best_hand is None or this_hand > best_hand:
            best_hand = this_hand
    return best_hand

if __name__ == "__main__":
    #flop = parse_cards(input("Flop cards: "))
    #player_cards = []
    #for i in range(4):
    #    player_cards.append(parse_cards(input("Player {} cards: ".format(i+1))))

    flop = parse_cards("3D5C9C")
    player_cards = []
    player_cards.append(parse_cards("3C7H"))
    player_cards.append(parse_cards("AS0S"))
    player_cards.append(parse_cards("9S2D"))
    player_cards.append(parse_cards("KCJC"))

    remaining = get_available_cards(flop, [item for sublist in player_cards for item in sublist])
    player_wins = {'1': 0, '2': 0, '3': 0, '4': 0}
    totals = 0

    for turn in remaining:
        for river in set(remaining) - set([turn]):
            player_hands = {}
            for i in range(4):
                table_cards = flop + [turn] + [river]
                player_hands[str(i)] = get_best_hand(player_cards[i] + table_cards)

            winner = max(player_hands, key=player_hands.get)
            if any([player_hands[x] == player_hands[winner] for x in player_hands if x != winner]):
                 totals += 1
            else:
                winner = str(int(winner) + 1)
                player_wins[winner] += 1
                totals += 1
    
    for i in "1234":
        print("{}: {:.1f}%".format(i, player_wins[i]/totals * 100))