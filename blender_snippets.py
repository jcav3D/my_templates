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


import bpy
import os


# Script pour créer un plan par image trouvé dans un dossier

# Modifier le dossier où sont stockées les images qui seront chargées dans la scène
folder_path = "V:\FORMATIONS\LA_HORDE\CQP_ETCN\MODULE_05\Images\OK"

# Des extensions d'image qui sont acceptées par le script
image_extensions = {".jpg", ".jpeg", ".png", ".tiff", ".bmp", ".tga"}

# Position du premier plan
x_offset = 0


# Parcourir les fichiers du dossier
for filename in os.listdir(folder_path):
    if any(filename.lower().endswith(ext) for ext in image_extensions):
        full_path = os.path.join(folder_path, filename)

        # Charger l'image
        try:
            img = bpy.data.images.load(full_path)
        except:
            print(f"Erreur lors du chargement de : {filename}")
            continue

        # Créer un plan
        bpy.ops.mesh.primitive_plane_add(size=2, location=(x_offset, 0, 0))
        plane = bpy.context.active_object
        plane.scale = (1.6, 0.9, 1)


        # Créer un matériau avec l'image
        mat = bpy.data.materials.new(name=f"Mat_{filename}")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
        tex_image.image = img
        mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

        # Assigner le matériau au plan
        plane.data.materials.append(mat)

        # Déplacer le prochain plan
        x_offset += 3.2  # espace entre les plans

