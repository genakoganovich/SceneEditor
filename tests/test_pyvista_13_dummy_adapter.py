from object_editor.fsm.adapters import DummyAdapter
from object_editor.fsm.actions import Action

def test_dummy_adapter_actions(capsys):
    adapter = DummyAdapter()

    adapter.pick_object(1)
    adapter.highlight_object(2)
    adapter.move_object(3, (10, 20, 30))
    adapter.delete_object(4)

    captured = capsys.readouterr()
    assert "[DUMMY] pick_object(1)" in captured.out
    assert "[DUMMY] highlight_object(2)" in captured.out
    assert "[DUMMY] move_object(3, (10, 20, 30))" in captured.out
    assert "[DUMMY] delete_object(4)" in captured.out
