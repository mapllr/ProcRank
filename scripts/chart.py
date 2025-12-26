from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt


class Chart:
    def __init__(self):
        pass

    def plot(self, x, y):
        plt.plot(x, y)
        plt.show()

    def bar(self, x, y):
        plt.bar(x, y)
        ax = plt.gca()
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_minor_locator(MultipleLocator(0.1))
        plt.show()

    def barh(self, x, y):
        plt.barh(x, y)
        plt.show()
