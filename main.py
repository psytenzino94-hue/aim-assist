from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window
import math

# Clear Background
Window.clearcolor = (0, 0, 0, 0)

class GuidelineOverlay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_pos = [Window.width / 2, Window.height / 3]
        self.angle = 45  # Angle in degrees
        self.length = 250
        self.draw_lines()

    def draw_lines(self):
        self.canvas.clear()
        
        rad = math.radians(self.angle)
        
        # 1. Aim Line (Green)
        mid_x = self.start_pos[0] + self.length * math.cos(rad)
        mid_y = self.start_pos[1] + self.length * math.sin(rad)
        
        # Screen Boundaries for Bounce
        max_x = Window.width
        max_y = Window.height
        
        # 2. Reflection Line (Red) - Simple Wall Bounce Simulation
        ext_length = 300
        end_x = mid_x + ext_length * math.cos(rad)
        end_y = mid_y + ext_length * math.sin(rad)
        
        # Check Wall Bounce (Horizontal walls)
        bounce_x = end_x
        bounce_y = end_y
        if end_x > max_x or end_x < 0:
            bounce_x = max_x if end_x > max_x else 0
            # Reverse X direction after hit
            bounce_end_x = bounce_x - (end_x - bounce_x)
        else:
            bounce_end_x = end_x
            
        if end_y > max_y or end_y < 0:
            bounce_y = max_y if end_y > max_y else 0
            bounce_end_y = bounce_y - (end_y - bounce_y)
        else:
            bounce_end_y = end_y

        with self.canvas:
            # Green Aiming Line
            Color(0, 1, 0, 1)
            Line(points=[self.start_pos[0], self.start_pos[1], mid_x, mid_y], width=2.5)
            
            # Red Bounce Line
            Color(1, 0, 0, 1)
            Line(points=[mid_x, mid_y, bounce_x, bounce_y, bounce_end_x, bounce_end_y], width=2.5)

    def on_touch_down(self, touch):
        self.start_pos = [touch.x, touch.y]
        self.draw_lines()

    def on_touch_move(self, touch):
        # Calculate angle based on touch movement direction
        dx = touch.x - self.start_pos[0]
        dy = touch.y - self.start_pos[1]
        if dx != 0 or dy != 0:
            self.angle = math.degrees(math.atan2(dy, dx))
        self.draw_lines()

class AimApp(App):
    def build(self):
        return GuidelineOverlay()

if __name__ == '__main__':
    AimApp().run()
