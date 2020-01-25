from hypothesis import given, example, settings
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
from hypothesis.strategies import text, lists, integers

from PropertyCheck.algorithms.BinaryHeap import BinaryHeap, Union
from PropertyCheck.algorithms.ternary_trie import *


class TSTMachine(RuleBasedStateMachine):
    Arbre = Bundle('arbre')

    @rule(target=Arbre)
    def newArbre(self):
        return gener_feuille()

    @rule(arbre=Arbre, mot=text())
    def search(self, arbre, mot):
        return search(arbre, mot)

    @rule(arbre=Arbre.filter(lambda self: self != None), mot=text())
    def insert(self, arbre, mot):
        insert(arbre, mot)
        assert search(arbre, mot)

    @rule(target=Arbre, a=Arbre, b=Arbre)
    def fusion(self, a, b):
        a_b = fusion(a, b)
        words_a_b = a.get_words("").union(b.get_words(""))

        # for word in words_a_b:
        #    nb = (nb + 1) if search(a_b, word) else nb
        # assert nb == len(words_a_b)

        for word in words_a_b:
            assert search(a_b, word)


TestTernary = TSTMachine.TestCase
