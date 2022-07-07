from ursina import *
from random import randint

def update():
    blue = randint(0,255)
    yellow = randint(0,255)
    red = randint(0,255)
    cube.color = color.rgb (blue, yellow, red)

    cube1.rotation_x = cube1.rotation_x + time.dt * 100

    cube.x = cube.x + time.dt
    cube.rotation_x = cube.rotation_x + time.dt * 100

    cube2.x = cube2.x + time.dt
    cube2.y = cube2.y - time.dt
    cube2.rotation_x = cube2.rotation_x + time.dt * 100

    cube3.x = cube3.x + time.dt
    cube3.y = cube3.y + time.dt
    cube3.rotation_x = cube3.rotation_x + time.dt * 100


    cube4.x = cube4.x - time.dt
    cube4.rotation_y = cube4.rotation_y - time.dt * 100

    cube5.x = cube5.x - time.dt
    cube5.y = cube5.y - time.dt
    cube5.rotation_y = cube5.rotation_y - time.dt * 100

    cube6.x = cube6.x - time.dt
    cube6.y = cube6.y + time.dt
    cube6.rotation_y = cube6.rotation_y - time.dt * 100

cube1 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5))
cube = Entity (model = 'cube', rotation = (45,45,45), scale = (.5))
cube2 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5), color = color.blue)
cube3 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5), color = color.red)
cube4 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5), color = color.yellow)
cube5 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5), color = color.green)
cube6 = Entity (model = 'cube', rotation = (45,45,45), scale = (.5), color = color.black)



app = Ursina()
app.run()
