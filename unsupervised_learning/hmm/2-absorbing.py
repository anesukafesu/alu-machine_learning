#!/usr/bin/env python3
'''
    function def absorbing(P): that
    determines if a markov chain is absorbing
'''


import numpy as np


def absorbing(P):
    '''
        Determines if a markov chain is absorbing
    '''
    if len(P.shape) != 2:
        return None
    n1, n2 = P.shape
    if (n1 != n2) or type(P) is not np.ndarray:
        return None
    D = np.diagonal(P)
    if (D == 1).all():
        return True
    if not (D == 1).any():
        return False

    for i in range(n1):
        # print('this is Pi {}'.format(P[i]))
        for j in range(n2):
            # print('this is Pj {}'.format(P[j]))
            if (i == j) and (i + 1 < len(P)):
                if P[i + 1][j] == 0 and P[i][j + 1] == 0:
                    return False
    return True
