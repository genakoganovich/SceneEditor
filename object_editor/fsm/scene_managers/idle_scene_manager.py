from .base_scene_manager import BaseSceneManager

class IdleSceneManager(BaseSceneManager):
    name = "Idle"

    def on_enter(self):
        super().on_enter()
        print("[Idle] GUI reset")

    def on_event(self, event):
        super().on_event(event)
        if event == "ADD_BUTTON_ON":
            return "Add"
        return None
