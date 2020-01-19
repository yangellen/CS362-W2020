# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:04:42 2020

@author: Ellen Yang 
"""
import testUtility
import Dominion
import random
from collections import defaultdict

#Accidently pass the wrong parameter, thus decrease the number of victory cards in the supply

#Get player names
player_names = testUtility.playerName()

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box
box = testUtility.getBox(nV)

supply_order = testUtility.getSupplyOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])

numPlayer = len(player_names)
#The supply always has these cards
#Accidently put down numPlayer twice.
#nV should be 12 for more than 3 players, but we have have 3 here.

testUtility.supplyAlways(supply,numPlayer,numPlayer,nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayer(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
