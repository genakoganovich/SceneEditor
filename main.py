# main.py

import pyvista as pv
from object_editor.fsm.context import FSMContext
from object_editor.fsm.events import Event
from object_editor.fsm.scene_managers import IdleSceneManager
from object_editor.fsm.decorators.pyvista_decorator import PyVistaSceneManagerDecorator

if __name__ == "__main__":
    # Создаем PyVista сцены
    plotter = pv.Plotter()
    plotter.show(auto_close=False)  # Не закрываем окно сразу

    # Создаём начальное состояние FSM
    idle_state = IdleSceneManager(ctx=None)
    decorated_idle = PyVistaSceneManagerDecorator(idle_state, plotter)
    fsm_ctx = FSMContext(decorated_idle)  # передаём уже готовый объект

    # Теперь пример событий
    fsm_ctx.dispatch(Event.ADD_BUTTON_ON)
    fsm_ctx.dispatch(Event.LEFT_PRESS_OBJECT)
    fsm_ctx.dispatch(Event.RIGHT_PRESS_OBJECT)
    fsm_ctx.dispatch(Event.ADD_BUTTON_OFF)

    # Обновляем визуализацию PyVista
    plotter.update()  # обновление сцены вместо plotter.app.processEvents()
