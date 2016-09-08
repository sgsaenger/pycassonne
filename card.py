#!/usr/bin/python2
class Card(object):
    def __init__(self,edges,connections=[],bonus=[]):
        self.edges = self.__evalEdges(edges)
        self.connections = self._evalConnections(connections)
        self.bonus = self.__evalBonus(bonus)

    __stdareas = ['field','city','road','river']
    __bonus = [None,'pennant','cloister',
            'spring','branch','lake',   #river
            'inn','cathredal' #inns and cathedrals
            'volcano','pigs']

    def __evalEdges(self,edges):
        if len(edges)<4:
            raise ValueError("Need to specify 4 edges")
        for e in edges:
            if not e in type(self).__stdareas:
                raise ValueError("Invalid edge-type: "+ str(e))
        return tuple(edges)

    def __evalConnections(self,cons):
        for c in cons:
            test=[]
            for i in c:
                test.append(self.edges[i])
            if len(set(test))>1:
                raise ValueError("Only edges of the same type can be connected")

    def __evalBonus(self,bonus):
        for b in bonus:
            if not b in type(self).__bonus:
                raise ValueError("Invalid bonus property: "+str(b))
        return b

    def offerPosition(self):
        return self.edges

    def offerFigure(self):
        return set(self.edges+self.m)
