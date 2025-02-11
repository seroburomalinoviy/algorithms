class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, instance, owner):
        if instance is None:
            print('here')
            return self
        value = self.func(instance)
        setattr(instance, self.name, value)
        return value


# Пример использования


class DataLoader:
    def __init__(self, data_source):
        self.data_source = data_source

    @LazyProperty
    def data(self):
        print("Загрузка данных...")
        # Имитация долгой загрузки данных
        return [x for x in range(1001)]


loader = DataLoader("some_source")
print("До обращения к свойству data")
print(loader.data)
print("После обращения к свойству data")
print(loader.data)
