# object_editor/fsm/decorators/pyvista_decorator.py

import pyvista as pv
from object_editor.fsm.actions import Action
from object_editor.fsm.scene_managers.base_scene_manager import BaseSceneManager


class PyVistaSceneManagerDecorator(BaseSceneManager):
    """
    Декоратор для SceneManager, добавляющий визуализацию с PyVista.
    Можно оборачивать любое состояние FSM.
    """

    def __init__(self, wrapped_state: BaseSceneManager, plotter: pv.Plotter):
        super().__init__(wrapped_state.ctx)
        self._wrapped = wrapped_state
        self.plotter = plotter

    def on_enter(self):
        print(f"[DECORATOR] Entering {type(self._wrapped).__name__}")
        self._wrapped.on_enter()

    def on_exit(self):
        print(f"[DECORATOR] Exiting {type(self._wrapped).__name__}")
        self._wrapped.on_exit()

    def on_event(self, event):
        # Действия до обработки события (pre-action)
        self._pre_action(event)

        # Передаем событие оригинальному состоянию
        self._wrapped.on_event(event)

        # Действия после обработки события (post-action)
        self._post_action(event)

    def _pre_action(self, event):
        # Например, подсветка объекта перед выбором
        if event.name == "LEFT_PRESS_OBJECT":
            print("[PYVISTA] PRE_ACTION: Highlight object")
            # Здесь можно добавить код PyVista для подсветки
            # self.plotter.add_mesh(..., color='yellow')

    def _post_action(self, event):
        # Действия после события
        if event.name == "LEFT_RELEASE":
            print("[PYVISTA] POST_ACTION: Move object")
            # Здесь можно переместить объект в PyVista сцене
        elif event.name == "RIGHT_PRESS_OBJECT":
            print("[PYVISTA] POST_ACTION: Delete object")
            # Здесь удаляем объект из PyVista сцены
        elif event.name == "LEFT_PRESS_OBJECT":
            print("[PYVISTA] POST_ACTION: Pick object")
            # Например, обновляем выделение
        elif event.name == "ADD_BUTTON_ON":
            print("[PYVISTA] POST_ACTION: GUI Add button pressed")
        elif event.name == "ADD_BUTTON_OFF":
            print("[PYVISTA] POST_ACTION: GUI Add button released")
