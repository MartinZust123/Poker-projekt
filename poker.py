#To je večerni projekt, kjer bom z knjižnico random raziskal igro Poker Texas Holdem. 
#Dogovorimo se, da so karte oblike (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1)
import random
from model_poker import Packet, Hand


def par(sez):
    pomozni = []
    for e in sez:
        pomozni.append(e[0])
    m = 0
    for e in pomozni:
        if pomozni.count(e) > m:
            m = pomozni.count(e)
            par = e
    return [m == 2, par]


#
#def dva_para(sez):
#    pomozni = []
#    for e in sez:
#        pomozni.append(e[0])
#    l = []
#    for e in pomozni:
#        if pomozni.count(e) == 2:
#            l.append(e)
#    s = set(l)
#    if len(set(l)) < 2:
#        return False
#    l1 = list(s)
#    l1.sort()
#    return [True, l1[-1],l1[-2]]

#Preverimo, v kakšnem deležu primerov dobimo flush

n = 0
for i in range(10000):
    packet = Packet()
    cards = packet.random_hand(7)
    hand = Hand(cards)
    if hand.ful()[0]:
        n += 1

print(n/100)
        



