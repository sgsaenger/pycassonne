#!/usr/bin/python2

class River(object):
    __name = "The River"
    __colors = []
    __figures = []
    __tiles = []
    __startTiles = [(Card(['river','field','field','field'],bonus=['spring']),1),
                    (Card(['river','field','river','field']),2),
                    (Card(['river','river','field','field']),2),
                    (Card(['river','river','road','road'],[[2,3]]),1),
                    (Card(['river','river','city','city'],[[2,3]]),1),
                    (Card(['river','field','river','road'],bonus=['cloister']),1),
                    (Card(['river','city','river','road']),1),
                    (Card(['river','city','river','city']),1),
                    (Card(['river','road','river','road'],[[1,3]]),1),
                    (Card(['river','field','field','field'],bonus=['lake']),1)]


class RiverII(object):
    __name = "The River II"
    __colors = []
    __figures = []
    __tiles = []
    __startTiles = [(Card(['river','field','field','field'],bonus=['spring']),1),
                    (Card(['river','river','river','field'],bonus=['branch']),1),
                    (Card(['river','river','field','field']),1),
                    (Card(['river','river','road','road'],[[2,3]]),1),
                    (Card(['river','river','field','field'],bonus=['pigs']),1),
                    (Card(['river','river','city','city'],[[2,3]],bonus=['pennant']),1),
                    (Card(['river','city','river','city'],[[1,3]]),1),
                    (Card(['river','road','river','city']),1),
                    (Card(['river','field','river','field'],bonus=['cloister']),1),
                    (Card(['river','road','river','road'],[[1,3]],bonus=['inn']),1),
                    (Card(['river','field','city','field']),1),
                    (Card(['river','field','field','field'],bonus=['volcano','lake']),1)]

class King(object):
    __name = "King and Robber"
    __colors = []
    __figures = []
    __startTiles = [];
    __tiles = [(Card(['city','city','city','city'],[[0,2],[1,3]]),1),
               (Card(['city','city','road','road'],[[0,1]]),1),
               (Card(['city','field','field','road']),1),
               (Card(['city','road','road','road'],[[1,2]]),1),
               (Card(['city','field','field','field'],bonus=['cloister']),1)]


class InnsCathedrals(object):
    __name = "Inns and Cathedrals"
    __colors = []
    __figures = []
    __startTiles = [];
    __tiles = [(Card(['road','field','road','field'],bonus=['cloister']),1),
               (Card(['city','city','city','city'],[[1,2,3,4]],['cathedral']),2),
               (Card(['city','city','city','city']),1),
               (Card(['city','city','city','field']),1),
               (Card(['city','road','city','road']),1),
               (Card(['city','city','city','field'],[[1,2]]),1),
               (Card(['city','field','field','field']),1),
               (Card(['city','field','road','field']),1),
               (Card(['city','city','road','field'],[[0,1]]),1),
               (Card(['city','road','city','road'],[[0,2]],['pennant']),1),
               (Card(['city','city','field','road'],[[0,1]],['inn']),1),
               (Card(['city','field','road','road'],[[2,3]],['inn']),1),
               (Card(['field','road','road','road'],bonus=['inn']),1),
               (Card(['field','road','road','field'],bonus=['inn']),1),
               (Card(['field','field','road','road'],[[2,3]],['inn']),1),
               (Card(['road','road','road','road'],[[0,1],[2,3]]),1)]
