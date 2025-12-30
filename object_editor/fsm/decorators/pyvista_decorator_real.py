# object_editor/fsm/decorators/pyvista_decorator_real.py

import pyvista as pv
from object_editor.fsm.actions import Action
from object_editor.fsm.scene_managers.base_scene_manager import BaseSceneManager


class PyVistaSceneManagerDecorator(BaseSceneManager):
    """
    Реальный PyVista-декоратор для SceneManager.
    Оборачивает состояние FSM и выполняет действия с PyVista.
    """

    def __init__(self, wrapped_state: BaseSceneManager, plotter: pv.Plotter):
        super().__init__(wrapped_state.ctx)
        self._wrapped = wrapped_state
        self.plotter = plotter

    # ------------------------------------------------------------------
    # FSM lifecycle
    # ------------------------------------------------------------------
    def on_enter(self):
        print(f"\n{'=' * 40}")
        print(f"[DECORATOR] Entering {type(self._wrapped).__name__}")
        print(f"{'=' * 40}")

        self._wrapped.on_enter()
        self.plotter.update()

    def on_exit(self):
        print(f"\n{'=' * 40}")
        print(f"[DECORATOR] Exiting {type(self._wrapped).__name__}")
        print(f"{'=' * 40}")

        self._wrapped.on_exit()
        self.plotter.update()

    def on_event(self, event: Action):
        print(f"\n{'-' * 20}")
        print(f"[DECORATOR] Event: {event}")
        print(f"{'-' * 20}")

        self._pre_action(event)
        self._wrapped.on_event(event)
        self._post_action(event)

        self.plotter.update()

    # ------------------------------------------------------------------
    # Pre / Post actions
    # ------------------------------------------------------------------
    def _pre_action(self, event: Action):
        if event == Action.LEFT_PRESS_OBJECT:
            print("[PYVISTA] PRE_ACTION: Highlight object")
            self.highlight_object()

    def _post_action(self, event: Action):
        if event == Action.LEFT_RELEASE:
            print("[PYVISTA] POST_ACTION: Move object")
            self.move_object()

        elif event == Action.RIGHT_PRESS_OBJECT:
            print("[PYVISTA] POST_ACTION: Delete object")
            self.delete_object()

        elif event == Action.LEFT_PRESS_OBJECT:
            print("[PYVISTA] POST_ACTION: Pick object")
            self.pick_object()

        elif event == Action.ADD_BUTTON_ON:
            print("[PYVISTA] POST_ACTION: GUI Add button pressed")

        elif event == Action.ADD_BUTTON_OFF:
            print("[PYVISTA] POST_ACTION: GUI Add button released")

    # ------------------------------------------------------------------
    # PyVista actions
    # ------------------------------------------------------------------
    def _last_actor(self):
        """Безопасно получить последний actor"""
        if not self.plotter.renderer or not self.plotter.renderer.actors:
            return None
        return list(self.plotter.renderer.actors.values())[-1]

    def highlight_object(self):
        actor = self._last_actor()
        if not actor:
            return

        # Желтая подсветка
        actor.GetProperty().SetColor(1.0, 1.0, 0.0)
        actor.GetProperty().SetLineWidth(3)
        self.plotter.update()

    def pick_object(self):
        print("[PYVISTA] Object picked (demo)")
        # Здесь позже будет реальный picking

    def delete_object(self):
        actor = self._last_actor()
        if not actor:
            return

        self.plotter.remove_actor(actor)
        self.plotter.update()

    def move_object(self):
        actor = self._last_actor()
        if not actor:
            return

        x, y, z = actor.GetPosition()
        actor.SetPosition(x + 1.0, y, z)
        self.plotter.update()
