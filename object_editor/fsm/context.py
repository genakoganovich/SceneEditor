from .transitions import TRANSITIONS
from .action_executor import ActionExecutor


class FSMContext:
    def __init__(self, initial_state_cls):
        self.executor = ActionExecutor(self)

        self.state = initial_state_cls(self)
        self.state.on_enter()

    def dispatch(self, event):
        state_cls = type(self.state)

        # PRE
        self.executor.run_pre(self.state, event)

        key = (state_cls, event)
        if key in TRANSITIONS:
            new_state_cls = TRANSITIONS[key]
            print(f"[FSM] {state_cls.__name__} → {new_state_cls.__name__}")

            self.state.on_exit()
            self.state = new_state_cls(self)
            self.state.on_enter()
        else:
            self.state.on_event(event)

        # POST
        self.executor.run_post(self.state, event)
