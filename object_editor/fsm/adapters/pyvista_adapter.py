# object_editor/fsm/adapters/pyvista_adapter.py

class PyVistaAdapter:
    """
    Контракт (интерфейс) для работы с PyVista.
    FSM и декораторы работают ТОЛЬКО с этим API.
    """

    def pick_object(self, object_id=None):
        raise NotImplementedError

    def highlight_object(self, object_id=None):
        raise NotImplementedError

    def move_object(self, object_id=None, position=None):
        raise NotImplementedError

    def delete_object(self, object_id=None):
        raise NotImplementedError
