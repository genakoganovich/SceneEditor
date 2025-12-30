from unittest.mock import MagicMock

from object_editor.fsm.decorators.pyvista_decorator import PyVistaSceneManagerDecorator
from object_editor.fsm.scene_managers import SelectedSceneManager
from object_editor.fsm.actions import Action


def test_pyvista_highlight_object():
    """
    PyVista decorator должен вызвать highlight у plotter
    при Action.HIGHLIGHT_OBJECT
    """

    # fake plotter
    plotter = MagicMock()

    # fake state
    state = SelectedSceneManager(ctx=None)

    # decorator
    decorated = PyVistaSceneManagerDecorator(state, plotter)

    # симулируем post-action
    decorated.on_post_action(Action.HIGHLIGHT_OBJECT)

    # проверка: PyVista вызван
    plotter.add_mesh.assert_called_once()
