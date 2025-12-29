# object_editor/fsm/action_executor.py

from object_editor.fsm.action_registry import ACTION_REGISTRY


class ActionExecutor:
    """
    Выполняет побочные действия FSM.
    Пока только логирует — без PyVista.
    """

    def execute(self, state, event, ctx):
        key = (type(state), event)
        actions = ACTION_REGISTRY.get(key, [])

        for action in actions:
            self._execute_action(action, ctx)

    def _execute_action(self, action, ctx):
        # Пока просто логируем
        print(f"[ACTION] {action}")
