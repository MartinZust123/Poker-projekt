#To je večerni projekt, kjer bom z knjižnico random raziskal igro Poker Texas Holdem. 
#Dogovorimo se, da so karte oblike (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1)
import random
from model_poker import Packet, Hand

#Preverimo, v kakšnem deležu primerov dobimo full-house. 

packet = Packet()
cards = packet.random_hand(7)
hand = Hand(cards)
print(hand.its_value())
    


        



