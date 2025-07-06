# bouger un objet de façon aleatoire
import bpy
import random
from mathutils import Vector

def pos():
    return random.uniform(-5,5)

def set_random_location(name):
    bpy.data.objects[name].location = Vector((
        pos(),
        pos(),
        pos(),
    ))

set_random_location("Cube")    
