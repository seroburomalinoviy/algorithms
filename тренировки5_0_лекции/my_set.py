class MySimpleSet:
    def __init__(self):
        self.length = 10
        self.map = [[] for _ in range(self.length)]
        self.hash_parameter = 10

    def _make_hash(self, value):
        return value % self.hash_parameter

    def add(self, value):
        self.map[self._make_hash(value)].append(value)

    def show(self):
        for index, i in enumerate(self.map):
            print(f"[{index}]: {i}")


my_set = MySimpleSet()
my_set.add(12)
my_set.add(81)
my_set.add(94)
my_set.add(33)
my_set.add(65)
my_set.add(17)
my_set.add(37)
my_set.add(49)

my_set.show()

