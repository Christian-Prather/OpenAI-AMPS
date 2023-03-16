from ursina import *
from ursina.prefabs.tilemap import Tilemap
from person import Person
from kiosk import Kiosk
from cart import Cart

import pandas as pd
import pytmx

START_PEOPLE = 15


active_people = []
# walls = []
kiosks = {}


def gen_world():
    # Get tiles
    tmxdata = pytmx.TiledMap('dia.tmx')

    layer = tmxdata.get_layer_by_name('walls')
    for x, y, surf in layer.tiles():
        wall = Entity(model="quad", x=x-15, y=-y + 10,
                      scale=(1, 1, 1), collider="box")
        # print(x, y)
        # walls.append(wall)

    layer = tmxdata.get_layer_by_name('kiosks')
    for x, y, surf in layer.tiles():
        kiosk = Kiosk(model="quad", x=x-15, y=-y + 10,
                      scale=(1, 1, 1), collider="box", color=color.blue)
        kiosks[kiosk.__hash__] = (kiosk.x, kiosk.y)

    print(layer.data)

    for i in range(START_PEOPLE):
        person = Person(model="quad", scale=(0.5, 0.5, 0.5))
        active_people.append(person)

    cart_1 = Cart(model="quad", scale=(1, 1, 1), color=color.orange)
    # cart_2 = Cart(model="quad", scale=(1, 1, 1), color=color.orange, x = 4)


def people_lifetime(life_counter):

    life_counter[0] += 1 * time.dt
    if life_counter[0] > 20:
        index = random.randint(0, len(active_people)-1)
        # print(index)
        person = active_people.pop(index)
        person.disable()

        life_counter[0] = 0


def main():
    app = Ursina()

    camera.orthographic = True

    gen_world()
    print(len(kiosks))
    # print(len(active_people))
    life_counter = [0]

    while True:
        people_lifetime(life_counter=life_counter)
        app.step()
    # app.run()


main()
