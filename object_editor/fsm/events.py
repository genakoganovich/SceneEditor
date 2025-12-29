# fsm/events.py

from enum import Enum, auto

class Event(Enum):
    """События, которые диспатчятся в конечный автомат сцены."""

    # GUI кнопки
    ADD_BUTTON_ON = auto()
    ADD_BUTTON_OFF = auto()
    SELECT_OBJECT_TYPE = auto()  # пользователь выбрал тип объекта (Cube, Sphere, Cylinder)

    # Клики мыши
    LEFT_PRESS_EMPTY = auto()     # клик по пустому месту
    LEFT_PRESS_OBJECT = auto()    # клик по объекту
    LEFT_RELEASE = auto()         # отпускание левой кнопки
    RIGHT_PRESS_OBJECT = auto()   # правый клик по объекту
    RIGHT_PRESS_EMPTY = auto()    # правый клик по пустому месту
