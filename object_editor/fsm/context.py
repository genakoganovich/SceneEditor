# object_editor/fsm/context.py

from .transitions import TRANSITIONS

class FSMContext:
    """Finite State Machine context"""

    def __init__(self, initial_state_cls):
        self.state = initial_state_cls(self)
        self.state.on_enter()

    def dispatch(self, event):
        """Отправка события FSM"""
        state_cls = type(self.state)
        key = (state_cls, event)

        if key in TRANSITIONS:
            new_state_cls = TRANSITIONS[key]
            print(f"[FSM] Dispatch {event}")
            print(f"[FSM] {state_cls.__name__} → {new_state_cls.__name__}")

            self.state.on_exit()
            self.state = new_state_cls(self)
            self.state.on_enter()
        else:
            self.state.on_event(event)

