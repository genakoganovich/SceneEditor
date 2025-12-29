from .action_registry import PRE_ACTIONS, POST_ACTIONS


class ActionExecutor:
    def __init__(self, ctx):
        self.ctx = ctx  # здесь позже будет PyVista

    def run_pre(self, state, event):
        for action in PRE_ACTIONS.get((type(state), event), []):
            print(f"[PRE_ACTION] {action}")

    def run_post(self, state, event):
        for action in POST_ACTIONS.get((type(state), event), []):
            print(f"[POST_ACTION] {action}")
