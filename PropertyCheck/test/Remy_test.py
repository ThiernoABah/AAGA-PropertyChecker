import sys
import unittest
from math import factorial
import RemyProjet as remy1
import RemyTreeV2 as remy2
from collections import defaultdict

if sys.version_info.major == 2:
    pass
else:
    pass


class RemyV1Test(unittest.TestCase):
    def test_gen_perm_remy1(self):
        n = 4
        perms = remy1.gen_perm(n)
        nb_result = factorial(4)
        # check le bon nombre d'element dans perms
        assert len(perms) == nb_result
        # vérifier qu'il n'y pas de duplication
        set_perms = set(tuple(i) for i in perms)
        assert len(perms) == len(set_perms)

    def test_create_all_tree_remy1(self):
        n = 4
        dict_result = defaultdict(int)
        for i in remy1.gen_perm(n):
            tree = remy1.ArbreRemy(n)
            dict_result[remy1.treeToStr(tree.growingTreeComplete(n, i))] += 1

        set_unif = set(dict_result.values())

        assert len(set_unif) != 1

    def test_gen_perm_remy2(self):
        n = 4
        nb_result = factorial(2 * (n - 1) + 1) / factorial(n - 1)
        perms = remy2.gen_perm(n)
        # check le bon nombre d'element dans perms
        assert len(perms) == nb_result
        # vérifier qu'il n'y pas de duplication
        set_perms = set(tuple(i) for i in perms)
        assert len(perms) == len(set_perms)

    def test_create_all_tree_remy2(self):
        n = 2
        dict_result = defaultdict(lambda: 0)
        for i in remy2.gen_perm(n):
            dict_result[remy2.treeToStr(remy2.remy_uniform_random(n, i))] += 1

        set_unif = set(dict_result.values())

        assert len(set_unif) == 1
