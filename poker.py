#To je večerni projekt, kjer bom z knjižnico random raziskal igro Poker Texas Holdem. 
#Dogovorimo se, da so karte oblike (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1)
import random
from model_poker import Packet, Hand


#def par(sez):
#    pomozni = []
#    for e in sez:
#        pomozni.append(e[0])
#    m = 0
#    for e in pomozni:
#        if pomozni.count(e) > m:
#            m = pomozni.count(e)
#            par = e
#    return [m == 2, par]
#
#def ful(sez):
#    if tris(sez)[0]:
#        pomozni = []
#        for e in sez:
#            if e[0] == tris(sez)[1]:
#                pomozni.append(e)
#        sez1 = [x for x in sez if x not in pomozni]
#        return [par(sez1)[0], tris(sez)[1], par(sez1)[1]]
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

packet = Packet()
cards = packet.random_hand(7)
hand = Hand(cards)

print(hand.flush())