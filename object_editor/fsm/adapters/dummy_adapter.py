# object_editor/fsm/adapters/dummy_adapter.py

from .pyvista_adapter import PyVistaAdapter

class DummyAdapter(PyVistaAdapter):
    """
    Заглушка для тестов. Просто логирует вызовы.
    """

    def pick_object(self, object_id=None):
        print(f"[DUMMY] pick_object({object_id})")

    def highlight_object(self, object_id=None):
        print(f"[DUMMY] highlight_object({object_id})")

    def move_object(self, object_id=None, position=None):
        print(f"[DUMMY] move_object({object_id}, {position})")

    def delete_object(self, object_id=None):
        print(f"[DUMMY] delete_object({object_id})")
