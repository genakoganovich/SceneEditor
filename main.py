# main.py
import pyvista as pv

from object_editor.fsm.scene_managers.idle_scene_manager import IdleSceneManager
from object_editor.fsm.decorators.pyvista_decorator_real import PyVistaSceneManagerDecorator
from object_editor.fsm.actions import Action


def main():
    # -----------------------------
    # PyVista Plotter
    # -----------------------------
    plotter = pv.Plotter()

    # -----------------------------
    # Scene objects
    # -----------------------------
    cube = pv.Cube(center=(0, 0, 0))
    sphere = pv.Sphere(center=(2, 0, 0))

    plotter.add_mesh(cube, color="red")
    plotter.add_mesh(sphere, color="blue")

    # -----------------------------
    # Non-blocking window
    # -----------------------------
    plotter.show(interactive_update=True)

    # -----------------------------
    # FSM + decorator
    # -----------------------------
    idle_state = IdleSceneManager(ctx=None)

    decorated_state = PyVistaSceneManagerDecorator(
        idle_state,
        plotter=plotter,
    )

    # -----------------------------
    # FSM start
    # -----------------------------
    decorated_state.on_enter()
    plotter.update()

    events = [
        Action.ADD_BUTTON_ON,
        Action.LEFT_PRESS_OBJECT,
        Action.RIGHT_PRESS_OBJECT,
        Action.ADD_BUTTON_OFF,
    ]

    for event in events:
        print("\n--------------------")
        print(f"[DECORATOR] Event: {event}")
        print("--------------------")

        # 👉 ставь breakpoint прямо здесь
        decorated_state.on_event(event)

        # 👉 и здесь
        plotter.update()

    decorated_state.on_exit()
    plotter.update()


if __name__ == "__main__":
    main()
