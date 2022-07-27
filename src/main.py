from game import Window

window = Window(1152, 864)

@window.draw
def draw():
    window.draw()
@window.update
def update(dt):
    window.update(dt)