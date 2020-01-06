import random

class Remy:
    FG = -12
    FD = -13
    P = -14
    num = -1

    def __init__(self, FG, FD, P, num):
        self.FG = FG
        self.FD = FD
        self.P = P
        self.num = num

class ArbreRemy:
    arbre = None
    def __init__(self, N):
        self.arbre = [Remy(-12, -13, -14, i) for i in range (2*N+1)]

    def changeLeaves(self, a, b):
        parentA = self.arbre[a].P
        parentB = self.arbre[b].P
        if(self.arbre[parentA].FD == a):
            self.arbre[parentA].FD = b
        else:
            self.arbre[parentA].FG = b
        self.arbre[a].P = parentB
        if(self.arbre[parentB].FD == b):
            self.arbre[parentB].FD = a
        else:
            self.arbre[parentB].FG = a
        self.arbre[b].P = parentA

    def growingTree(self, n):
        self.arbre[0].FG = 1
        self.arbre[0].FD = 2
        self.arbre[0].num = 1
        self.arbre[1].P = self.arbre[2].P = 0
        self.arbre[1].FD = self.arbre[1].FG = -1
        self.arbre[2].FD = self.arbre[2].FG = -1

        for i in range(2, n+1):
            nb = random.randint(0, i)
            self.changeLeaves(i-1, nb+i-1)
            self.arbre[i-1].FD = 2*i-1
            self.arbre[i-1].FG = 2*i
            self.arbre[i-1].num = i
            self.arbre[2*i-1].P = self.arbre[2+i].P = i-1
            self.arbre[2*i-1].FD = self.arbre[2*i-1].FG = -1
            self.arbre[2*i].FD = self.arbre[2*i].FG = -1
