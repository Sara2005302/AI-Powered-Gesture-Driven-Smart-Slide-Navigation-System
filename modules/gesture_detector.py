import cv2
import numpy as np
import time
import pyautogui

class GestureDetector:
    def __init__(self, config_manager):
        self.config = config_manager
        self.previous_hand_positions = []
        self.swipe_threshold = 80
        self.min_swipe_points = 6
        self.last_swipe_time = 0
        self.swipe_cooldown = 1.0
    
    def detect_swipe_gesture(self, cx, cy):
        """Detect swipe gestures for navigation"""
        current_time = time.time()
        if current_time - self.last_swipe_time < self.swipe_cooldown:
            return None
            
        self.previous_hand_positions.append((cx, cy))
        if len(self.previous_hand_positions) > 8:
            self.previous_hand_positions.pop(0)
        
        if len(self.previous_hand_positions) >= 4:
            start_x, start_y = self.previous_hand_positions[0]
            end_x, end_y = self.previous_hand_positions[-1]
            
            delta_x = end_x - start_x
            delta_y = end_y - start_y
            
            # Horizontal swipe detection for navigation
            if abs(delta_x) > 60 and abs(delta_y) < 50:
                self.last_swipe_time = current_time
                self.previous_hand_positions.clear()
                return "right" if delta_x > 0 else "left"
        
        return None
    
    def process_swipe_gestures(self, hands, cx, cy):
        """Process swipe gestures - SIMPLIFIED (no media controls)"""
        if not hands:
            return None, "👋"
        
        current_gesture = None
        gesture_icon = "👋"
        
        # SWIPE GESTURES ONLY - NO MEDIA CONTROLS
        swipe = self.detect_swipe_gesture(cx, cy)
        if swipe == "right":
            current_gesture = "Next Slide (Swipe)"
            gesture_icon = "➡️"
        elif swipe == "left":
            current_gesture = "Previous Slide (Swipe)" 
            gesture_icon = "⬅️"
        
        return current_gesture, gesture_icon