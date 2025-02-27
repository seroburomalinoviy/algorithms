class MySimpleSet:
    def __init__(self, length, hash_parameter):
        self.length = length
        self.map = [[] for _ in range(self.length)]
        self.hash_parameter = hash_parameter

    def _make_hash(self, value):
        return value % self.hash_parameter

    def add(self, value):
        self.map[self._make_hash(value)].append(value)

    def show(self):
        for index, i in enumerate(self.map):
            print(f"[{index}]: {i}")

    def find(self, value) -> bool:
        if value in self.map[self._make_hash(value)]:
            return True
        return False

    def delete(self, value):
        slc = self.map[self._make_hash(value)]
        for i in range(len(slc)):
            if slc[i] == value:
                slc[i] = slc[-1]
                slc.pop()
                # del slc[-1]
                return


my_set = MySimpleSet(10,10)
my_set.add(12)
my_set.add(81)
my_set.add(94)
my_set.add(33)
my_set.add(65)
my_set.add(17)
my_set.add(37)
my_set.add(57)
my_set.add(67)
my_set.add(49)
my_set.show()

print(f"{my_set.find(12)=}")
print(f"{my_set.find(65)=}")
print(f"{my_set.find(37)=}")

print(f"{my_set.find(0)=}")
print(f"{my_set.find(100000)=}")

my_set.delete(17)

my_set.show()

# ЗАДАЧА

"""
Найти в заданной последовательности числа, которые в сумме дают заданное число
A + B = X, если таких нет вернуть 0, 0
"""


def number_finder(input_lst, target_num):
    st = MySimpleSet(length=1000, hash_parameter=100)
    for i in input_lst:
        if st.find(target_num - i):
            return target_num - i, i
        st.add(i)
    return 0, 0


lst = [1, 32, 63, 40, 5000, 69, 788, 8, 89, 170]
num = 5001
print(number_finder(lst, num))
