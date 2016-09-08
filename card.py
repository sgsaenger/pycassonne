#!/usr/bin/python2
class Card(object):
    def __init__(self,edges,middle=None,bonus=None):
        #defined clockwise
        self.edges = self.__evalEdges(edges)
        self.middle = self.__evalMiddle(middle)
        self.bonus = self.__evalBonus(bonus)

    __stdareas = ['field','city','road']
    __midareas = [None,'cloister','city']
    __bonus = [None,'pennant']

    def __evalEdges(self,edges):
        if len(edges)<4:
            raise ValueError("Need to specify 4 edges")
        for e in edges:
            if not e in type(self).__stdareas:
                raise ValueError("Invalid edge-type: "+ str(e))
        return tuple(edges)


    def __evalMiddle(self,m):
        if not m in type(self).__midareas:
            raise ValueError("Invalid middle-type: "+str(m))
        if m == 'cloister':
            if 'city' in self.edges:
                raise ValueError("No Cloisters beside cities!")
            elif self.edges.count('field')<3:
                raise ValueError("A maximum of one road may lead to a cloister")
        elif m == 'city':
            if self.edges.count('city')<2:
                raise ValueError("City centers are only possible for cities with\
                        at least two edges!")
            elif self.edges.count("city")>2:
                return None
        return m
    
    def __evalBonus(self,b):
        if not b in type(self).__bonus:
            raise ValueError("Invalid bonus property: "+str(b))
        if b == "pennant" and self.edges.count("city")<2:
            raise ValueError("Pennant only possible for cities with at least\
                    two edges!")
        return b

    def offerPosition(self):
        return self.edges

    def offerFigure(self):
        return set(self.edges+self.m)

    def roadsConnected(self):
        return self.edges.count('road') == 2

    def cityConnected(self):
        n = self.edges.count('city')
        if n == 2:
            return card.m == 'city'
        elif n > 2:
            return True
        else:
            return False
