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

    __name = "Base game"
    __colors = ['red','blue','black','yellow','green']
    __figures = []
    __startTiles = [(Card(['city','road','field','road'],[[1,3]]),1)]
    __tiles = [(Card(['city','road','field','road'],[[1,3]]),3),
               (Card(['city','road','road','road']),3),
               (Card(['city','road','road','field'],[[1,2]]),3),
               (Card(['city','field','road','road'],[[2,3]]),3),
               (Card(['city','field','field','field']),5),
               (Card(['city','city','field','field']),2),
               (Card(['city','city','field','field'],[[0,1]]),3),
               (Card(['city','city','field','field'],[[0,1]],['pennant']),2),
               (Card(['city','field','city','field']),3),
               (Card(['city','field','city','field'],[[0,2]]),1),
               (Card(['city','field','city','field'],[[0,2]],['pennant']),2),
               (Card(['city','city','city','field'],[[0,1,2]]),3),
               (Card(['city','city','city','field'],[[0,1,2]],['pennant']),1),
               (Card(['city','city','city','city'],[[0,1,2,3]],['pennant']),1),
               (Card(['city','city','road','road'],[[0,1],[2,3]]),3),
               (Card(['city','city','road','road'],[[0,1],[2,3]],['pennant']),2),
               (Card(['city','city','city','road'],[[0,1,2]]),1),
               (Card(['city','city','city','road'],[[0,1,2]],['pennant']),2),
               (Card(['road','road','field','field'],[[0,1]]),9),
               (Card(['road','field','road','field'],[[0,2]]),8),
               (Card(['road','road','road','field']),4),
               (Card(['road','road','road','road']),1),
               (Card(['field','field','field','field'],bonus=['cloister']),4),
               (Card(['road','field','field','field'],bonus=['cloister']),2)]
