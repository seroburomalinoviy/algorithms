from dataclasses import dataclass


@dataclass
class Plants:
    color: str  # атрибут экземпляра доступен для записи и чтения если класс не заморожен
    height: float  # атрибут экземпляра доступен для записи и чтения если класс не заморожен
    is_tree: bool = False  # атрибут класса которых хранит значение по умолчанию для атрибута экземпляра
    is_on_earth = True  # атрибут класса

