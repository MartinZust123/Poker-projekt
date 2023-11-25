#model for project poker
import numpy as np 
from numpy import random
from icecream import ic

class Packet:
    """Instances in this class are packets of 52 standard cards."""
    
    karte = []
    for n in range(13):
        for m in range(4):
            karte.append((n+1,m+1))

    karte1 = [i for i in range(52)]

    def __init__(self, rand=True):
        self.cards = Packet.karte

    def __repr__(self):
        return f"Packet(cards)"

    def __str__(self):
        return "Instance of class Packet"

    def random_hand(self, size):
        indeksi = random.choice(Packet.karte1, size=size,replace=False)
        hand = []
        for i in indeksi:
            hand.append(Packet.karte[i])
        return hand

class Hand:
    """Instances of this class are hands of either 2 till 7 cards."""
    def __init__(self, cards, player=None):
        self.cards = cards
        self.player = player

    def __repr__(self):
        return f"Hand({self.cards})"

    def __str__(self):
        return f"Player has a hand {self.cards}."

    def straight(self):
        if len(self.cards) < 5:
            return [False,[]]
        l = []
        for e in self.cards:
            l.append(e[0])
        for e in l:
            if l.count(e) != 1:
                l.remove(e)
        l.sort()
        if l[0] == 1:
            l.append(14)
        for n in range(len(l) - 4):
            if l[n] +4 == l[n+1] + 3 == l[n+2] + 2 == l[n+3] +1 == l[n+4]:
                return [True,l[n+4]]
        return [False,l]

    def flush(self):
        seznam = []
        for e in self.cards:
            seznam.append(e[1])
        m = 0
        barva = 0
        for e in seznam:
            if seznam.count(e) > m:
                m = seznam.count(e)
                barva = e
        if m < 5:
            return [False, barva]
        else:
            sez = []
            for e in self.cards:
                if e[1] == barva:
                    sez.append(e[0]) 
            return [True, barva, max(sez)]

    def straight_flush(self):
        m = 0
        barva = 0
        pomozni = []
        for e in self.cards:
            pomozni.append(e[1])
        for b in pomozni:
            if pomozni.count(b) > m:
                m = pomozni.count(b)
                barva = b
        if m < 5:
            return [False, barva, []]
        indeksi = []
        for e in self.cards:
            if e[1] != barva:
                indeksi.append(e)
        sez = []
        for e in self.cards:
            sez.append(e)
        for e in indeksi:
            sez.remove(e)
        if Hand(sez).straight()[0]:
            return [True, barva, self.cards]
        else:
            return [False, barva, self.cards]

    def poker(self):
        pomozni = []
        for e in self.cards:
            pomozni.append(e[0])
        m = 0
        for e in pomozni:
            if pomozni.count(e) > m:
                m = pomozni.count(e)
                poker = e
        return [m == 4, poker]

    def tris(self):
        pomozni = []
        for e in self.cards:
            pomozni.append(e[0])
        m = 0
        for e in pomozni:
            if pomozni.count(e) > m:
                m = pomozni.count(e)
                tris = e
        if tris == 1:
            tris == 14
        return [m == 3, tris]

    def pair(self):
        pomozni = []
        for e in self.cards:
            pomozni.append(e[0])
        m = 0
        for el in pomozni:
            if pomozni.count(el) > m:
                m = pomozni.count(el)
                par = e
        if par == 1:
            par = 14
        return [m == 2, par]

    def two_pairs(self):
        pomozni = []
        for e in self.cards:
            pomozni.append(e[0])
        l = []
        for e in pomozni:
            if pomozni.count(e) == 2:
                l.append(e)
        s = set(l)
        if len(set(l)) < 2:
            return [False, 1, 2]
        l1 = list(s)
        if 1 in l1:
            l1.remove(1)
            l1.append(14)
        l1.sort()
        return [True, l1[-1],l1[-2]]
    
    def ful(self):
        if self.tris()[0]:
            pomozni = []
            for e in self.cards:
                if e[0] == self.tris()[1]:
                    pomozni.append(e)
            sez1 = [x for x in self.cards if x not in pomozni]
            if Hand(sez1).two_pairs()[0]:
                return [True, self.tris()[1], Hand(sez1).two_pairs()[1], self.cards]
            return [Hand(sez1).pair()[0], self.tris()[1], Hand(sez1).pair()[1]]
        else:
            return [False, self.cards]

    def high_card(self):
        sez = []
        for e in self.cards:
            sez.append(e[0])
        if 1 in sez:
            return 14
        return max(sez)

    def its_value(self):
        if self.straight_flush()[0]:
            return ('staight_flush', self.straight_flush(), 200)
        elif self.poker()[0]:
            return ('poker', self.poker(), 120 + self.poker()[1])
        elif self.ful()[0]:
            return ('ful', self.ful(), 105 + self.ful()[1])
        elif self.flush()[0]:
            return ('flush', self.flush(), 90 + self.flush()[2])
        elif self.straight()[0]:
            return ('straight', self.straight(), 75 + self.straight()[1])
        elif self.tris()[0]:
            return ('tris', self.tris(), 60 + self.tris()[1])
        elif self.two_pairs()[0]:
            return ('two_pairs', self.two_pairs(), 28 + self.two_pairs()[1] + self.two_pairs()[2])
        elif self.pair()[0]:
            return ('pair', self.pair(), 14 + self.pair()[1])
        else:
            return ('high_card', self.high_card(), 0 + self.high_card())

#Let's define another function for finding the winner of a hand. 
def winner(list_of_hands):
    w = 0
    list_of_winners = []
    for e in list_of_hands:
        if e.its_value()[2] > w:
            w = e.its_value()[2]
    for e in list_of_hands:
        if e.its_value()[2] == w:
            list_of_winners.append(e)
    return list_of_winners

        
    