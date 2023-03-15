from ursina import *
from person import Person

app = Ursina()

cart_1 = Person(model="quad", color=color.blue, scale=(0.3, 0.3, 0.3))
cart_2 = Person(model="quad", color=color.red, scale=(0.3, 0.3, 0.3))

cart_3 = Person(model="quad", color=color.pink, scale=(0.3, 0.3, 0.3))
cart_4 = Person(model="quad", color=color.white, scale=(0.3, 0.3, 0.3))

app.run()
