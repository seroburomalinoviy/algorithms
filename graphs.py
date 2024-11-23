import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import numpy as np


def factorial(n) -> list:
    fact_range = []
    for i in range(1, n + 1):
        k = 1
        for j in range(1, i):
            k = k * j
        fact_range.append(k)
    return fact_range


class Grapher(ABC):
    def create_graph(self, *args, **kwargs):
        fig, ax = plt.subplots()
        ax.grid(axis='y', linestyle='-')
        ax.grid(axis='x', linestyle='-')
        plt.xticks(self.x)
        plt.yticks(self.y)
        ax.plot(self.x, self.y, *args, **kwargs)

        plt.show()


class FactorialGraph(Grapher):
    def __init__(self, n):
        self.x = [_ for _ in range(1, n+1)]
        self.y = factorial(n)
        print('OX', self.x)
        print('OY', self.y)


class SequenceGraph(Grapher):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('OX', self.x)
        print('OY', self.y)



# attempt1 = FactorialGraph(n=10)
# attempt1.create_graph()
X = list(range(1, 19))
Y = [i*527 for i in range(1, 19)]

attmp1 = SequenceGraph(x=X, y=Y)
attmp1.create_graph(color='green', marker='o', linestyle='dashed',linewidth=1, markersize=6)