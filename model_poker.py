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
                return [True,l]
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
        return [True, barva, self.cards]

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
        return [m == 3, tris]

    def pair(self):
        pomozni = []
        for e in self.cards:
            pomozni.append(e[0])
        m = 0
        for el in pomozni:
            if pomozni.count(el) > m:
                m = pomozni.count(e)
                par = e
        return [m == 2, par]
    
    def ful(self):
        if self.tris()[0]:
            pomozni = []
            for e in self.cards:
                if e[0] == self.tris()[1]:
                    pomozni.append(e)
            sez1 = [x for x in self.cards if x not in pomozni]
            return [Hand(sez1).pair()[0], self.tris()[1], Hand(sez1).pair()[1]]
        else:
            return [False, self.cards]

        
    