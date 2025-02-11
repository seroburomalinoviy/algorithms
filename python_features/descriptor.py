class Cache:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        val = self.func(instance)
        setattr(instance, self.name, val)
        return val


class Descriptor:
    def __set_name__(self, owner, name):
        self.var_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.var_name]

    def __set__(self, instance, value):
        instance.__dict__[self.var_name] = value


class A:
    my_x = Descriptor()

    @Cache
    def data(self):
        return [x for x in range(101)]


d = A()
print(d.data)
print(d.data)
d.my_x = 10
print(d.my_x)