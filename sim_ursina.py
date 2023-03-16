from ursina import *
from ursina.prefabs.tilemap import Tilemap
from person import Person
import pandas as pd
import pytmx

START_PEOPLE = 15

active_people = []
# walls = []


def gen_world():
    # Get tiles
    tmxdata = pytmx.TiledMap('dia.tmx')

    layer = tmxdata.get_layer_by_name('walls')
    for x, y, surf in layer.tiles():
        wall = Entity(model="quad", x=x-15, y=-y + 10,
                        scale=(1, 1, 1), collider="box")
        # print(x, y)
        # walls.append(wall)

    print(layer.data)

    for i in range(START_PEOPLE):
        person = Person(model="quad", scale=(0.5, 0.5, 0.5))
        active_people.append(person)



def main():
    app = Ursina()

    camera.orthographic = True
    life_counter = 0

    gen_world()
    print(len(active_people))
    

    while True:
        life_counter += 1 * time.dt
        if life_counter >10:
            index = random.randint(0,len(active_people)-1)
            # print(index)
            person = active_people.pop(index)
            person.disable()

            life_counter = 0
            
        app.step()
    # app.run()


main()