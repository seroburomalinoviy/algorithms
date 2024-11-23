from dataclasses import dataclass


class Output:
    def out(self):
        print(f'This is {self.name}')


@dataclass
class Phone(Output):
    name: str
    screensize: float


@dataclass
class Camera(Output):
    name: str
    pixels: int


@dataclass
class PhoneCamera(Output):
    name: str
    screensize: float
    camera: Camera


class Fabrika:
    def __init__(self):
        pass

    @staticmethod
    def set_device(*args, **kwargs) -> Camera | Phone | PhoneCamera:
        if tuple(kwargs.keys()) == Phone.__dict__['__match_args__']:
            phone = Phone(name=kwargs['name'], screensize=kwargs['screensize'])
            return phone
        elif tuple(kwargs.keys()) == Camera.__dict__['__match_args__']:
            camera = Camera(name=kwargs['name'], pixels=kwargs['pixels'])
            return camera
        elif tuple(kwargs.keys()) == PhoneCamera.__dict__['__match_args__']:
            phone_camera = PhoneCamera(name=kwargs['name'], screensize=kwargs['screensize'], camera=kwargs['camera'])
            return phone_camera
        else:
            raise KeyError


def main():

    camera = Fabrika.set_device(name='Canon', pixels=1000)
    camera.out()
    phone_camera = Fabrika.set_device(name='Phone', screensize=10.0, camera=camera)
    phone_camera.out()
    phone = Fabrika.set_device(name='PhoneX', screensize=10.0)
    phone.out()
    print(PhoneCamera.__mro__)


main()

"""
Есть компания которая выпускает три типа девайсов: камера, телефон и телефон с камерой.
У каждого девайса есть свои свойства, для камеры это название и разрешение;
у телефона название и размер экрана; у телефона с камерой это девайс камеры, название и размер экрана
1. Необходимо написать класс-фабрику, с помощью которой нужно создать все девайсы и вывести для каждого девайса 
фразу "This is {name}".
"""




