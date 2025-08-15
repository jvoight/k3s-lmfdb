import lasVegas
from importlib import reload
reload(lasVegas)
import genus
reload(genus)

import os
from functools import reduce

from sage.arith.misc import kronecker, prime_divisors, inverse_mod, factor
from sage.arith.functions import LCM_list
from sage.combinat.integer_vector_weighted import WeightedIntegerVectors
from sage.functions.other import ceil
from sage.interfaces.magma import magma
from sage.matrix.constructor import matrix
from sage.matrix.special import block_diagonal_matrix, diagonal_matrix, block_matrix
from sage.structure.element import Matrix
from sage.misc.functional import is_even, is_odd, sqrt
from sage.misc.misc_c import prod
from sage.quadratic_forms.genera.genus import Genus_Symbol_p_adic_ring
from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring
from sage.quadratic_forms.genera.genus import is_GlobalGenus, is_2_adic_genus
from sage.quadratic_forms.genera.genus import LocalGenusSymbol
from sage.rings.finite_rings.integer_mod_ring import Zmod
from sage.rings.integer_ring import ZZ
from sage.rings.integer import Integer
from sage.modules.free_quadratic_module import FreeQuadraticModule_submodule_with_basis_pid, FreeQuadraticModule
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice, local_modification
from sage.rings.finite_rings.finite_field_constructor import GF
from sage.structure.factorization_integer import IntegerFactorization
from sage.quadratic_forms.genera.normal_form import p_adic_normal_form
from sage.matrix.constructor import zero_matrix
from random import randint
from math import prod
from itertools import product


if __name__ == "__main__":
    signaturePair = (ZZ(4),ZZ(4))
    det = 2**4*3**3*13**4
    testCases = genus.all_genus_symbols(signaturePair[0], signaturePair[1], det)
    print(f"{len(testCases)} symbols to compute representatives of")
    for test in testCases:
        # assert is_GlobalGenus(test), f"Test case of:\n{test}is not even a valid genus!"
        print(f"Symbols:\n{"\n".join([str(i.symbol_tuple_list()) for i in test.local_symbols()])}\n ____")
        assert(Genus(test.representative()) == test)
        lasVegas.dubeyHolensteinLatticeRepresentative(test,check = False,superDumbCheck = True)

    # test = GenusSymbol_global_ring((3,4), 
    #                                [
    #                                    Genus_Symbol_p_adic_ring(2,[[0, 4, 1, 0, 0], [1, 2, 3, 0, 0], [2, 1, 1, 1, 1]]),
    #                                    Genus_Symbol_p_adic_ring(3,[[0, 3, 1], [1, 3, 1], [2, 1, 1]]),
    #                                 ])
    # print(lasVegas.dubeyHolensteinLatticeRepresentative(test, True))