import pgzrun
def draw():
    screen.fill((128,128,128))
    screen.draw.text("Hello World",topleft=(180,270),fontsize=30,color="yellow")
    screen.draw.line((10,10),(100,100),(255,0,0))

WIDTH = 300
HEIGHT = 300

pgzrun.go()
