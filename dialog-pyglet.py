import pyglet
from pyglet.window import mouse
from pyglet.gl import *
from pyglet import *

# Constants for window size and dialog position
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DIALOG_WIDTH = 400
DIALOG_HEIGHT = 200
DIALOG_X = (WINDOW_WIDTH - DIALOG_WIDTH) // 2
DIALOG_Y = (WINDOW_HEIGHT - DIALOG_HEIGHT) // 2

# Define a button class
class Button:
    def __init__(self, x, y, width, height, label):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.is_hovered = False

    def draw(self):
        # Draw button background
        color = (200, 200, 200) if not self.is_hovered else (150, 150, 150)
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
            ('v2f', [self.x, self.y,
                      self.x + self.width, self.y,
                      self.x + self.width, self.y + self.height,
                      self.x, self.y + self.height]),
            ('c3B', color * 4)
        )
        # Draw button label
        label = pyglet.text.Label(self.label,
                                   x=self.x + self.width // 2,
                                   y=self.y + self.height // 2,
                                   anchor_x='center', anchor_y='center')
        label.draw()

    def contains(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

# Define the dialog class
class Dialog:
    def __init__(self):
        self.buttons = [
            Button(DIALOG_X + 50, DIALOG_Y + 50, 100, 40, 'OK'),
            Button(DIALOG_X + 250, DIALOG_Y + 50, 100, 40, 'Cancel')
        ]

    def draw(self):
        # Draw dialog background
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
            ('v2f', [DIALOG_X, DIALOG_Y,
                      DIALOG_X + DIALOG_WIDTH, DIALOG_Y,
                      DIALOG_X + DIALOG_WIDTH, DIALOG_Y + DIALOG_HEIGHT,
                      DIALOG_X, DIALOG_Y + DIALOG_HEIGHT]),
            ('c3B', (100, 100, 100) * 4)
        )
        # Draw buttons
        for button in self.buttons:
            button.draw()

    def on_mouse_motion(self, x, y):
        for button in self.buttons:
            button.is_hovered = button.contains(x, y)

    def on_mouse_press(self, x, y, button):
        for btn in self.buttons:
            if btn.contains(x, y):
                print(f"{btn.label} button clicked!")

# Create a Pyglet window
window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)

# Create a dialog instance
dialog = Dialog()

@window.event
def on_draw():
    window.clear()
    dialog.draw()

@window.event
def on_mouse_motion(x, y, dx, dy):
    dialog.on_mouse_motion(x, y)

@window.event
def on_mouse_press(x, y, button, modifiers):
    dialog.on_mouse_press(x, y, button)

# Run the application
pyglet.app.run()
