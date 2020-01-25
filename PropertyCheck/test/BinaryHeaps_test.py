from hypothesis import given, example, settings
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
from hypothesis.strategies import text, lists, integers

from TernarySearchTree.algorithms.BinaryHeap import BinaryHeap, Union


@given(lists(integers()))
def test_pop_in_sorted_order(ls):
    h = BinaryHeap()
    h.ConsIter(ls)
    r = []
    while not h.estVide():
        r.append(h.SupMin())
    assert r == sorted(ls)


class HeapMachine(RuleBasedStateMachine):
    Heaps = Bundle('heaps')

    @rule(target=Heaps)
    def newheap(self):
        return BinaryHeap()

    @rule(heap=Heaps, value=integers())
    def push(self, heap, value):
        heap.Ajout(value)

    @rule(heap=Heaps.filter(lambda self: self.estVide() != True))
    def pop(self, heap):
        correct = heap.getMin()
        result = heap.SupMin()
        assert correct == result

    @rule(target=Heaps, heap1=Heaps, heap2=Heaps)
    def merge(self, heap1, heap2):
        res = Union(heap1, heap2)
        assert res.getTaille() == heap1.getTaille() + heap2.getTaille()
        return res


TestHeaps = HeapMachine.TestCase
