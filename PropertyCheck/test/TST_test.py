from hypothesis import given, example, settings
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
from hypothesis.strategies import text, lists, integers

from PropertyCheck.algorithms.BinaryHeap import BinaryHeap, Union
from PropertyCheck.algorithms.ternary_trie import *
import unittest


class TSTMachine(RuleBasedStateMachine):
    Arbre = Bundle('arbre')

    @rule(target=Arbre)
    def newArbre(self):
        return gener_feuille()

    @rule(arbre=Arbre, mot=text())
    def search(self, arbre, mot):
        return search(arbre, mot)

    @rule(target=Arbre, arbre=Arbre, mot=text(alphabet=('azertyuiopqsdfghjklmwxcvbn'), min_size=1))
    def insert(self, arbre, mot):
        res = insert(arbre, mot)
        assert search(res, mot)
        return res

    @rule(target=Arbre, a=Arbre, b=Arbre)
    def fusion(self, a, b):
        a_b = fusion(a, b)
        words_a_b = a.get_words("").union(b.get_words(""))

        for word in words_a_b:
            assert search(a_b, word)
        return a_b


TestTernary = TSTMachine.TestCase
if __name__ == '__main__':
    unittest.main()

print(TestTernary)
