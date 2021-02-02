import graphics as gr

window = gr.GraphWin("Russian game", 300, 100)


def draw_wall(x=50, y=40, color="brown"):
    """Draw house wall"""
    house = gr.Rectangle(gr.Point(x, y), gr.Point(x + 50, y + 40))

    house.draw(window)
    house.setFill(color)


def draw_roof(x=50, y=40, color="brown"):
    """Draw house roof"""

    roof = gr.Polygon(gr.Point(x, y), gr.Point(x + 25, y - 10), gr.Point(x + 50, y))

    roof.draw(window)
    roof.setFill(color)


def draw_scene():
    """Draw environment"""
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(300, 60))
    ground = gr.Rectangle(gr.Point(0, 60), gr.Point(300, 100))
    my_circle = gr.Circle(gr.Point(250, 20), 10)

    sky.draw(window)
    sky.setFill("cyan")
    sky.setOutline("cyan")

    my_circle.draw(window)
    my_circle.setFill("yellow")
    my_circle.setOutline("yellow")

    ground.draw(window)
    ground.setFill("green")
    ground.setOutline("green")


def draw_tree():
    """Draw tree"""
    tree = gr.Rectangle(gr.Point(170, 20), gr.Point(180, 80))
    tree.draw(window)
    tree.setFill("brown")


def draw_house(x=50, y=40, color="brown"):
    """Draw whole house
    x, y - top left corner"""
    draw_wall(x, y, color)
    draw_roof(x, y, color)


draw_scene()
draw_house(x=100, y=50, color="red")
draw_house(x=200, y=40, color="black")
draw_house()
draw_tree()

window.getMouse()
window.close()
