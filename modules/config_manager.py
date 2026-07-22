import json

class ConfigManager:
    def __init__(self):
        self.gesture_mappings = {}
        self.load_mappings_from_file()
    
    def load_mappings_from_file(self):
        """Load gesture mappings from config file"""
        try:
            with open('gesture_config.json', 'r') as f:
                self.gesture_mappings = json.load(f)
        except:
            # SIMPLIFIED DEFAULT MAPPINGS - ONLY PRESENTATION CONTROLS
            self.gesture_mappings = {
                'next_slide': [0, 0, 0, 0, 1],           # Pinky
                'previous_slide': [1, 0, 0, 0, 0],       # Thumb
                'pointer': [0, 1, 1, 0, 0],              # Index+Middle
                'draw': [0, 1, 0, 0, 0],                 # Index only
                'erase': [0, 1, 1, 1, 0],                # Index+Middle+Ring
                'clear_all': [1, 1, 1, 1, 1]             # All fingers
            }
            self.save_mappings_to_file()
    
    def save_mappings_to_file(self):
        """Save gesture mappings to config file"""
        try:
            with open('gesture_config.json', 'w') as f:
                json.dump(self.gesture_mappings, f, indent=2)
            return True
        except Exception as e:
            print(f"❌ Error saving config: {e}")
            return False
    
    def get_gesture_icon(self, action):
        fingers = self.gesture_mappings.get(action, [0,0,0,0,0])
        finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        raised_fingers = [name for i, name in enumerate(finger_names) if fingers[i] == 1]
        
        if not raised_fingers:
            return "✊"
        elif raised_fingers == ["Thumb"]:
            return "👍"
        elif raised_fingers == ["Pinky"]:
            return "🖖"
        elif raised_fingers == ["Index", "Middle"]:
            return "✌️"
        elif raised_fingers == ["Index"]:
            return "👆"
        elif raised_fingers == ["Index", "Middle", "Ring"]:
            return "🤟"
        elif len(raised_fingers) == 5:
            return "🖐️"
        else:
            return f"{len(raised_fingers)}👆"