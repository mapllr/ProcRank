import matplotlib.pyplot as plt


class Plot:
    def __init__(self):
        pass

    def make_plot(self, x, y):
        plt.plot(x, y)
        plt.show()

    def make_bar(self, x, y):
        plt.bar(x, y)
        plt.show()

    def make_barh(self, x, y):
        plt.barh(x, y)
        plt.show()

    def make_hist(self, x, y):
        plt.hist(x, y)
        plt.show()

