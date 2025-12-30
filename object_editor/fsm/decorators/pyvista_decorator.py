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
        print("--------------------------------------------------")
        print(f"[EVENT] {event.name}")
        # Действия до обработки события (pre-action)
        self._pre_action(event)

        # Передаем событие оригинальному состоянию
        self._wrapped.on_event(event)

        # Действия после обработки события (post-action)
        self._post_action(event)
        print("--------------------------------------------------\n")

    # --- Публичный метод для тестов ---
    def on_post_action(self, action: Action):
        """
        Позволяет тестам вызывать post-action напрямую.
        Конвертируем Action → DummyEvent с полем name.
        """
        class DummyEvent:
            def __init__(self, name):
                self.name = name
        dummy_event = DummyEvent(action.name)
        self._post_action(dummy_event)

    # --- Приватные методы ---
    def _pre_action(self, event):
        if event.name == "LEFT_PRESS_OBJECT":
            print("[PYVISTA] PRE_ACTION: Highlight object")
            # Заглушка для тестов
            if self.plotter:
                self.plotter.highlight_object = getattr(self.plotter, "highlight_object", lambda x: None)
                self.plotter.highlight_object(None)

    def _post_action(self, event):
        if event.name == "LEFT_RELEASE":
            print("[PYVISTA] POST_ACTION: Move object")
        elif event.name == "RIGHT_PRESS_OBJECT":
            print("[PYVISTA] POST_ACTION: Delete object")
            if self.plotter:
                self.plotter.delete_object = getattr(self.plotter, "delete_object", lambda x: None)
                self.plotter.delete_object(None)
        elif event.name == "LEFT_PRESS_OBJECT":
            print("[PYVISTA] POST_ACTION: Pick object")
            if self.plotter:
                self.plotter.pick_object = getattr(self.plotter, "pick_object", lambda x: None)
                self.plotter.pick_object(None)
        elif event.name == "ADD_BUTTON_ON":
            print("[PYVISTA] POST_ACTION: GUI Add button pressed")
        elif event.name == "ADD_BUTTON_OFF":
            print("[PYVISTA] POST_ACTION: GUI Add button released")
        elif event.name == "HIGHLIGHT_OBJECT":
            print("[PYVISTA] POST_ACTION: Highlight object")
            if self.plotter:
                self.plotter.add_mesh = getattr(self.plotter, "add_mesh", lambda *a, **kw: None)
                self.plotter.add_mesh(None)
