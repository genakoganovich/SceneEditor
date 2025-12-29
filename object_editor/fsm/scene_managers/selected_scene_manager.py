from .base_scene_manager import BaseSceneManager

class SelectedSceneManager(BaseSceneManager):
    name = "Selected"

    def on_enter(self):
        super().on_enter()
        print("[Selected] highlight object")

    def on_event(self, event):
        super().on_event(event)
        if event in ["RIGHT_PRESS_OBJECT", "RIGHT_PRESS_EMPTY", "LEFT_PRESS_EMPTY"]:
            return "Idle"
        elif event == "LEFT_PRESS_OBJECT":
            return "Selected"  # выбор другого объекта
        return None
