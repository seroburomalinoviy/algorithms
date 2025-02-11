

class A:
    def __init__(self, iters):
        self.iters = iters
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.iters) == self.index:
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.iters[self.index - 1]


a = [1,2,3,4,5]

_a = A(a)
for i in _a:
    print(i)

for i in _a:
    print(i)






