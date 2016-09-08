#!/usr/bin/python2
from card import Card
from player import Player
from random import shuffle

class Basic(object):
    def __init__(self,np):
        self.players = []
        for i in range(np):
            self.players.append(Player(type(self).__colors[i]))
        self.tiles = []
        for i in type(self).__tiles:
            self.tiles.extend([i[0]]*i[1])
        shuffle(self.tiles)
        self.startTiles = type(self).__startTiles
        shuffle(self.startTiles)

    __colors = ('red','blue','black','yellow','green')
    __startTiles = [Card(('city','road','field','city'))]
    __tiles = [(Card(('city','road','field','road')),3),
               (Card(('city','road','road','road')),3),
               (Card(('city','road','road','field')),3),
               (Card(('city','field','road','road')),3),
               (Card(('city','field','field','field')),5),
               (Card(('city','city','field','field')),2),
               (Card(('city','city','field','field'),'city'),3),
               (Card(('city','city','field','field'),'city','pennant'),2),
               (Card(('city','field','city','field')),3),
               (Card(('city','field','city','field'),'city'),1),
               (Card(('city','field','city','field'),'city','pennant'),2),
               (Card(('city','city','city','field')),3),
               (Card(('city','city','city','field'),None,'pennant'),1),
               (Card(('city','city','city','city'),None,'pennant'),1),
               (Card(('city','city','road','road')),3),
               (Card(('city','city','road','road'),None,'pennant'),2),
               (Card(('city','city','city','road')),1),
               (Card(('city','city','city','road'),None,'pennant'),2),
               (Card(('road','road','field','field')),9),
               (Card(('road','field','road','field')),8),
               (Card(('road','road','road','field')),4),
               (Card(('road','road','road','road')),1),
               (Card(('field','field','field','field'),'cloister'),4),
               (Card(('road','field','field','field'),'cloister'),2)]
