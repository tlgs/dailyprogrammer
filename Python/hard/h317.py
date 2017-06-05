# 02/06/2017
import itertools
from collections import Counter 

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

class Hand(object):
    def __init__(self, cards):
        self.cards = cards
        self.name = None
        self.relevant_cards = None
        self.next_high_cards = None
        self.tier = None
        self.assign()
        
    def get_suits(self):
        return [card.suit for card in self.cards]
    
    def get_values(self):
        return [card.value for card in self.cards]

    def is_straight_flush(self):
        #print(self.cards)
        if len(set(self.get_suits())) == 1 and have_consecs(self.get_values(), 5):
            self.name = "Straight Flush"
            self.relevant_cards = self.cards
            self.tier = 1
            return True
    
    def is_four_of_a_kind(self):
        if max(Counter(self.get_values()).values()) == 4:
            self.name = "Four of a Kind"
            relevant_value = Counter(self.get_values()).most_common(1)[0][0]
            self.relevant_cards = [card for card in self.cards if card.value == relevant_value]
            self.next_high_cards = [card for card in self.cards if card.value != relevant_value]
            self.tier = 2
            return True

    def is_full_house(self):
        if set(Counter(self.get_values()).values()) == {3, 2}:
            self.name = "Full House"
            relevant_value = Counter(self.get_values()).most_common(1)[0][0]
            self.relevant_cards = [card for card in self.cards if card.value == relevant_value]
            self.next_high_cards = [card for card in self.cards if card.value != relevant_value]
            self.tier = 3
            return True

    def is_flush(self):
        if len(set(self.get_suits())) == 1:
            self.name = "Flush"
            self.relevant_cards = [max(self.cards, key=sort_func)]
            self.next_high_cards = sorted(self.cards, key=sort_func, reverse=True)
            self.tier = 4
            return True

    def is_straight(self):
        if have_consecs(self.get_values(), 5):
            self.name = "Straight"
            self.relevant_cards = [max(self.cards, key=sort_func)]
            self.tier = 5
            return True
    
    def is_three_of_a_kind(self):
        if set(Counter(self.get_values()).values()) == {3, 1}:
            self.name = "Three of a Kind"
            relevant_value = Counter(self.get_values()).most_common(1)[0][0]
            self.relevant_cards = [card for card in self.cards if card.value == relevant_value]
            self.next_high_cards = sorted([card for card in self.cards if card.value != relevant_value], 
                                          key=sort_func, reverse=True)
            self.tier = 6
            return True
    
    def is_two_pairs(self):
        if list(Counter(self.get_values()).values()).count(2) == 2:
            self.name = "Two Pairs"
            pairs = sorted([v for v, _ in Counter(self.get_values()).most_common(2)], 
                                 key=lambda x: "234567890JQKA".index(x), reverse=True)
            self.relevant_cards = [card for card in self.cards if card.value == pairs[0]]
            self.next_high_cards = [card for card in self.cards if card.value == pairs[1]] + \
                                   [card for card in self.cards if card.value == (set(self.get_values()) - set(pairs)).pop()]
            self.tier = 7
            return True
    
    def is_pair(self):
        if len(set(self.get_values())) == 4:
            self.name = "Pair"
            relevant_value = Counter(self.get_values()).most_common(1)[0][0]
            self.relevant_cards = [card for card in self.cards if card.value == relevant_value]
            self.next_high_cards = sorted([card for card in self.cards if card.value != relevant_value], 
                                          key=sort_func, reverse=True)
            self.tier = 8
            return True

    def assign(self):
        if self.is_straight_flush():
            return 
        elif self.is_four_of_a_kind():
            return
        elif self.is_full_house():
            return
        elif self.is_flush():
            return
        elif self.is_straight():
            return
        elif self.is_three_of_a_kind():
            return
        elif self.is_two_pairs():
            return
        elif self.is_pair():
            return
        else:
            self.name = "Highest Card"
            self.relevant_cards = [max(self.cards, key=sort_func)]
            self.next_high_cards = sorted(self.cards, key=sort_func, reverse=True)[1::]
            self.tier = 9


def sort_func(x):
    return "234567890JQKA".index(x.value)

def have_consecs(values, n):
    value_list = "A234567890JQKA"
    possibles = []
    for i in range(1+len(value_list)-n):
        possibles.append(value_list[i:i+n])
    return values in possibles

def get_available_cards(flop, hands):
    deck = [Card(v, s) for v in "234567890JQKA" for s in "CSDH"
            if not any(c.suit == s and c.value == v for c in flop + hands)]
    return deck

def parse_cards(string):
    hand = [Card(v, s) for v, s in zip(string[::2], string[1::2])]
    return hand

def compare_hands(a, b):
    if a.tier < b.tier:
        return a
    elif b.tier < a.tier:
        return b
    elif b.tier == a.tier:
        if sort_func(b.relevant_cards[0]) > sort_func(a.relevant_cards[0]):
            return b
        elif sort_func(b.relevant_cards[0]) < sort_func(a.relevant_cards[0]):
            return a
        elif sort_func(b.relevant_cards[0]) == sort_func(a.relevant_cards[0]):
            tie = True
            for card_b, card_a in zip(b.next_high_cards, a.next_high_cards):
                if sort_func(card_b) > sort_func(card_a):
                    return b
                elif sort_func(card_b) < sort_func(card_a):
                    return a
            if tie:
                return None

def get_best_hand(cards):
    best_hand = None
    for hand in itertools.combinations(cards, 5):
        this_hand = Hand(hand)
        if best_hand is None:
            best_hand = this_hand
        result = compare_hands(best_hand, this_hand)
        best_hand = best_hand if result is None else result

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
                player_hands[str(i)] = get_best_hand(player_cards[i] + flop + [turn] + [river])

            results = {k: v.tier for k, v in player_hands.items()}
            winner_tier = min(results.values())

            if Counter(results.values())[winner_tier] > 1:
                tied_players = [k for k, v in results.items() if v == winner_tier]
                winner = tied_players[0]
                for p in tied_players:
                    winner = p if player_hands[p] == compare_hands(player_hands[p], player_hands[winner]) else winner
                for p in set(tied_players) - set(winner):
                    if compare_hands(player_hands[p], player_hands[winner]) is None:
                        winner = None
                        break
                if winner is None:
                    totals += 1
                    continue
                else:
                    winner = str(int(winner) + 1)
            else:
                winner = str(int(sorted(results, key=results.get)[0]) + 1)
            player_wins[winner] += 1
            totals += 1
    
    for i in "1234":
        print("{}: {:.1f}%".format(i, player_wins[i]/totals * 100))