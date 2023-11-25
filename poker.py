#To je večerni projekt, kjer bom z knjižnico random raziskal igro Poker Texas Holdem. 
#Dogovorimo se, da so karte oblike (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1)
import random
from model_poker import Packet, Hand

#Preverimo, v kakšnem deležu primerov dobimo full-house. 

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

list_of_players = ["Matej Matos", "Martin Žust", "Gal Vid Verlič", "Urh Ušeničnik", "Jakob Železen", "Peter Brodnik", "Gabriel Klančar"]

packet = Packet()

slovar = {"Martin Žust": 0, "Matej Matos": 0, "Gabriel Klančar": 0, "Urh Ušeničnik": 0, "Jakob Železen": 0, "Gal Vid Verlič": 0, "Peter Brodnik": 0}
for i in range(10000):
    list_of_hands = []
    for clovek in list_of_players:
        list_of_hands.append(Hand(packet.random_hand(7), clovek))
    
    zmagovalci = winner(list_of_hands)
    for cl in zmagovalci:
        slovar[cl.player] += 1

print(slovar)
    


        



