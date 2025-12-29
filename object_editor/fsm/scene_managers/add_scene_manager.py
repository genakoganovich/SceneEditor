from .base_scene_manager import BaseSceneManager

class AddSceneManager(BaseSceneManager):
    name = "Add"

    def on_enter(self):
        super().on_enter()
        print(f"[Add] Object type selected: {self.selected_object_type}")

    def on_event(self, event):
        super().on_event(event)
        if event == "LEFT_PRESS_EMPTY":
            print("[Add] handling add logic")
            self.selected_object_type = None
            return "Idle"
        elif event == "LEFT_PRESS_OBJECT":
            return "Selected"
        return None
