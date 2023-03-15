from ursina import *
from person import Person

app = Ursina()

cart_1 = Person(model="quad", color=color.blue)
cart_2 = Person(model="quad", color=color.red)

cart_3 = Person(model="quad", color=color.pink)
cart_4 = Person(model="quad", color=color.white)

app.run()