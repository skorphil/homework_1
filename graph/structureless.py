import graphics as gr

window = gr.GraphWin("Russian game", 300, 100)
my_circle = gr.Circle(gr.Point(250, 20), 10)
ground = gr.Rectangle(gr.Point(0, 60), gr.Point(300, 100))
house = gr.Rectangle(gr.Point(50, 40), gr.Point(100, 80))
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(300, 60))
roof = gr.Polygon(gr.Point(50, 40), gr.Point(75, 30), gr.Point(100, 40))
tree = gr.Rectangle(gr.Point(170, 20), gr.Point(180, 80))

sky.draw(window)
sky.setFill("cyan")
sky.setOutline("cyan")

my_circle.draw(window)
my_circle.setFill("yellow")
my_circle.setOutline("yellow")

ground.draw(window)
ground.setFill("green")
ground.setOutline("green")

house.draw(window)
house.setFill("brown")

roof.draw(window)
roof.setFill("brown")

tree.draw(window)
tree.setFill("brown")


window.getMouse()
window.close()
