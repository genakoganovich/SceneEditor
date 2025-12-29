# object_editor/fsm/transitions.py

from .events import Event
from .scene_managers import (
    IdleSceneManager,
    AddIdleSceneManager,
    AddSceneManager,
    SelectedSceneManager,
)

# Таблица переходов FSM
# Ключ: (текущее состояние, событие)
# Значение: новое состояние
TRANSITIONS = {

    # ================= Idle =================

    # Включили Add → AddIdle (тип ещё не выбран)
    (IdleSceneManager, Event.ADD_BUTTON_ON): AddIdleSceneManager,

    # В Idle остальные события ничего не меняют
    (IdleSceneManager, Event.LEFT_PRESS_OBJECT): IdleSceneManager,
    (IdleSceneManager, Event.LEFT_PRESS_EMPTY): IdleSceneManager,
    (IdleSceneManager, Event.RIGHT_PRESS_OBJECT): IdleSceneManager,
    (IdleSceneManager, Event.RIGHT_PRESS_EMPTY): IdleSceneManager,
    (IdleSceneManager, Event.ADD_BUTTON_OFF): IdleSceneManager,
    (IdleSceneManager, Event.SELECT_OBJECT_TYPE): IdleSceneManager,


    # ================= AddIdle =================
    # Add включён, но тип объекта НЕ выбран

    # Выбрали тип объекта → полноценный Add
    (AddIdleSceneManager, Event.SELECT_OBJECT_TYPE): AddSceneManager,

    # Клик по объекту → выбрать его
    (AddIdleSceneManager, Event.LEFT_PRESS_OBJECT): SelectedSceneManager,

    # Клик по пустоте → ничего
    (AddIdleSceneManager, Event.LEFT_PRESS_EMPTY): AddIdleSceneManager,

    # Правый клик по объекту → удалить и выйти в Idle
    (AddIdleSceneManager, Event.RIGHT_PRESS_OBJECT): IdleSceneManager,

    # Правый клик по пустоте → ничего
    (AddIdleSceneManager, Event.RIGHT_PRESS_EMPTY): AddIdleSceneManager,

    # Выключили Add → Idle
    (AddIdleSceneManager, Event.ADD_BUTTON_OFF): IdleSceneManager,


    # ================= Add =================
    # Add включён, тип объекта выбран

    # Клик по пустоте → добавить объект → вернуться в AddIdle
    (AddSceneManager, Event.LEFT_PRESS_EMPTY): AddIdleSceneManager,

    # Клик по объекту → выбрать объект
    (AddSceneManager, Event.LEFT_PRESS_OBJECT): SelectedSceneManager,

    # Правый клик по объекту → удалить и выйти в Idle
    (AddSceneManager, Event.RIGHT_PRESS_OBJECT): IdleSceneManager,

    # Правый клик по пустоте → ничего
    (AddSceneManager, Event.RIGHT_PRESS_EMPTY): AddSceneManager,

    # Выключили Add → Idle
    (AddSceneManager, Event.ADD_BUTTON_OFF): IdleSceneManager,

    # Сменили тип объекта → остаёмся в Add
    (AddSceneManager, Event.SELECT_OBJECT_TYPE): AddSceneManager,


    # ================= Selected =================

    # Клик по пустоте → снять выделение
    (SelectedSceneManager, Event.LEFT_PRESS_EMPTY): IdleSceneManager,
    (SelectedSceneManager, Event.RIGHT_PRESS_EMPTY): IdleSceneManager,

    # Клик по объекту → выбрать другой
    (SelectedSceneManager, Event.LEFT_PRESS_OBJECT): SelectedSceneManager,

    # Правый клик по объекту → удалить → Idle
    (SelectedSceneManager, Event.RIGHT_PRESS_OBJECT): IdleSceneManager,

    # Отпустили кнопку мыши → Idle
    (SelectedSceneManager, Event.LEFT_RELEASE): IdleSceneManager,

    # Add не влияет на выделение
    (SelectedSceneManager, Event.ADD_BUTTON_ON): SelectedSceneManager,
    (SelectedSceneManager, Event.ADD_BUTTON_OFF): SelectedSceneManager,
    (SelectedSceneManager, Event.SELECT_OBJECT_TYPE): SelectedSceneManager,
}
