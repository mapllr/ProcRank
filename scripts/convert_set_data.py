import numpy as np


class Convert:
    def __init__(self):
        pass

    def nparr(self, x, y):
        return np.array(x), np.array(y)

    def nparr_sort(self, x, y):
        pair = list(zip(x,y))
        pair_sorted = sorted(pair, key=lambda p: p[0])
        xs, ys = zip(*pair_sorted)
        return np.array(xs[-10:]),np.array(ys[-10:])

