from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Ellipse
from kivy.core.window import Window
import math

Window.clearcolor = (0, 0, 0, 0)

class CarromAimOverlay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_pos = [Window.width / 2, Window.height / 3]
        self.angle = 45
        self.length = 220
        self.ext_length = 350
        self.draw_guidelines()

    def draw_guidelines(self):
        self.canvas.clear()
        
        # Carrom Board boundary margins (Screen ke andar board border)
        margin_x = Window.width * 0.08
        margin_y = Window.height * 0.15
        board_left = margin_x
        board_right = Window.width - margin_x
        board_top = Window.height - margin_y
        board_bottom = margin_y

        rad = math.radians(self.angle)
        
        # Target Point (Mid Point)
        mid_x = self.start_pos[0] + self.length * math.cos(rad)
        mid_y = self.start_pos[1] + self.length * math.sin(rad)

        # Reflection End Point
        end_x = mid_x + self.ext_length * math.cos(rad)
        end_y = mid_y + self.ext_length * math.sin(rad)

        # Wall Bounce calculation relative to Carrom Board Frame
        bounce_x, bounce_y = end_x, end_y
        bounce_end_x, bounce_end_y = end_x, end_y

        if end_x > board_right:
            bounce_x = board_right
            bounce_end_x = bounce_x - (end_x - bounce_x)
        elif end_x < board_left:
            bounce_x = board_left
            bounce_end_x = bounce_x + (board_left - end_x)

        if end_y > board_top:
            bounce_y = board_top
            bounce_end_y = bounce_y - (end_y - bounce_y)
        elif end_y < board_bottom:
            bounce_y = board_bottom
            bounce_end_y = bounce_y + (board_bottom - end_y)

        with self.canvas:
            # Striker / Touch Point Marker
            Color(1, 1, 1, 0.8)
            Ellipse(pos=(self.start_pos[0]-12, self.start_pos[1]-12), size=(24, 24))

            # Aiming Line (Green)
            Color(0, 1, 0, 0.9)
            Line(points=[self.start_pos[0], self.start_pos[1], mid_x, mid_y], width=3)
            
            # Target Puck Marker
            Color(1, 1, 0, 1)
            Ellipse(pos=(mid_x-10, mid_y-10), size=(20, 20))

            # Bounce Line (Red)
            Color(1, 0, 0, 0.9)
            Line(points=[mid_x, mid_y, bounce_x, bounce_y, bounce_end_x, bounce_end_y], width=2.5)

    def on_touch_down(self, touch):
        self.start_pos = [touch.x, touch.y]
        self.draw_guidelines()

    def on_touch_move(self, touch):
        dx = touch.x - self.start_pos[0]
        dy = touch.y - self.start_pos[1]
        if dx != 0 or dy != 0:
            self.angle = math.degrees(math.atan2(dy, dx))
        self.draw_guidelines()

class CarromAimApp(App):
    def build(self):
        return CarromAimOverlay()

if __name__ == '__main__':
    CarromAimApp().run()
