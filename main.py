from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window
import math

# Window को Transparent और No-Border सेट करें
Window.clearcolor = (0, 0, 0, 0)

class GuidelineOverlay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_pos = [300, 300]
        self.angle = 45  # शुरुआती एंगल
        self.length = 200 # हरी लाइन की लंबाई
        self.ext_length = 200 # लाल लाइन की लंबाई
        self.draw_lines()

    def draw_lines(self):
        self.canvas.clear()
        
        # 1. Start Position से Green Line की कैलकुलेशन
        rad = math.radians(self.angle)
        mid_x = self.start_pos[0] + self.length * math.cos(rad)
        mid_y = self.start_pos[1] + self.length * math.sin(rad)
        
        # 2. Green Line से Red Line की कैलकुलेशन
        end_x = mid_x + self.ext_length * math.cos(rad)
        end_y = mid_y + self.ext_length * math.sin(rad)

        with self.canvas:
            # Green Line (Aiming Line)
            Color(0, 1, 0, 1)  # RGB: Green
            Line(points=[self.start_pos[0], self.start_pos[1], mid_x, mid_y], width=2)
            
            # Red Line (Extension Line)
            Color(1, 0, 0, 1)  # RGB: Red
            Line(points=[mid_x, mid_y, end_x, end_y], width=2)

    # स्क्रीन पर टच करके लाइन को मूव करने का लॉजिक
    def on_touch_move(self, touch):
        self.start_pos = [touch.x, touch.y]
        self.draw_lines()

class AimApp(App):
    def build(self):
        return GuidelineOverlay()

if __name__ == '__main__':
    AimApp().run()
