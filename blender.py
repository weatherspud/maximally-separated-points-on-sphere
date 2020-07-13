import bpy
from bpy_extras.object_utils import object_data_add


def add_object(self, context):
    vertices = [
        Vector((1, 2, 3)),
        Vector((1, 2, 4)),
        Vector((2, 3, 4))
    ]
    edges = []
    faces = [
        [0, 1, 2]
    ]
    mesh = bpy.data.meshes.new(name="polyhedron")
    mesh.from_pydata(vertices, edges, faces)
    object_data_add(context, mesh, operator=self)
