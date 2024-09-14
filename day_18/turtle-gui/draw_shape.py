import random
COLOR = [
    'Aquamarine', 'Coral', 'Turquoise', 'Lavender',
    'Crimson', 'Indigo', 'Chartreuse', 'Fuchsia',
    'OrangeRed', 'DarkOliveGreen', 'GoldenRod', 'SlateBlue',
    'MediumPurple', 'SeaGreen', 'DeepPink', 'Tomato',
    'LightSeaGreen', 'SaddleBrown', 'RoyalBlue', 'DarkMagenta'
]

class DrawShape:
    def __init__(self, turtle, angle):
        self.total_angle = angle
        self.turtle = turtle
        self.draw()

    def draw(self):
        # draw square
        self.turtle.pencolor(random.choice(COLOR))
        for _ in range(self.total_angle):
            #    mini.speed()
            self.turtle.right(360/self.total_angle)
            self.turtle.forward(100)