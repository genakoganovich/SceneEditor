class BaseSceneManager:
    name = "Base"

    def __init__(self, ctx):
        self.ctx = ctx  # FSM context
        self.selected_object_type = None  # выбранный тип объекта

    def on_enter(self):
        print(f"[ENTER] {self.name}")

    def on_exit(self):
        print(f"[EXIT] {self.name}")

    def on_event(self, event):
        print(f"[{self.name}] event: {event}")
