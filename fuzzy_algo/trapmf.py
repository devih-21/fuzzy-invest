import numpy as np
from fuzzy_algo.trimf import trimf

def trapmf(x, abcd):

    assert len(abcd) == 4, 'abcd parameter must have exactly four elements.'
    a, b, c, d = np.r_[abcd]
    assert a <= b and b <= c and c <= d, 'abcd requires the four elements \
                                          a <= b <= c <= d.'
    y = np.ones(len(x))

    idx = np.nonzero(x <= b)[0]
    y[idx] = trimf(x[idx], np.r_[a, b, b])

    idx = np.nonzero(x >= c)[0]
    y[idx] = trimf(x[idx], np.r_[c, c, d])

    idx = np.nonzero(x < a)[0]
    y[idx] = np.zeros(len(idx))

    idx = np.nonzero(x > d)[0]
    y[idx] = np.zeros(len(idx))

    return y