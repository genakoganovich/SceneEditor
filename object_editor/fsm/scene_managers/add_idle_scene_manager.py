from .base_scene_manager import BaseSceneManager

class AddIdleSceneManager(BaseSceneManager):
    name = "AddIdle"

    def on_enter(self):
        super().on_enter()
        print("[AddIdle] No object type selected")

    def on_event(self, event):
        super().on_event(event)
        if event == "LEFT_PRESS_OBJECT":
            return "Selected"
        elif event == "SELECT_OBJECT_TYPE":
            return "Add"
        return None
