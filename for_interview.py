class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(obj, self.name, value)
        return value


# Пример использования
class DataLoader:
    def __init__(self, data_source):
        self.data_source = data_source

    @LazyProperty
    def data(self):
        print("Загрузка данных...")
        # Имитация долгой загрузки данных
        return [x for x in range(101)]


loader = DataLoader("some_source")

print("До обращения к data")
print(loader.data)
print("После обращения к data")
print(loader.data)



