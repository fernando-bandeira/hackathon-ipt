from stl import mesh
import numpy as np


def diff_meshes(mesh1, mesh2):

    healthy_blisk = mesh.Mesh.from_file(mesh1)
    damaged_blisk = mesh.Mesh.from_file(mesh2)

    healthy_idx = 0
    damaged_idx = 0
    healthy_vectors = healthy_blisk.vectors
    damaged_vectors = damaged_blisk.vectors
    healthy_points = healthy_blisk.points
    vector_list = []
    point_list = []

    while damaged_idx < len(damaged_blisk.vectors):
        if not np.array_equal(damaged_vectors[damaged_idx], healthy_vectors[healthy_idx]):
            vector_list.append(healthy_vectors[healthy_idx])
            point_list.append(healthy_points[healthy_idx])
            healthy_idx += 1

        healthy_idx += 1
        damaged_idx += 1

    vector_array = np.array(vector_list)
    point_array = np.array(point_list)

    diff_mesh = mesh.Mesh(np.zeros(vector_array.shape[0], dtype=mesh.Mesh.dtype))
    diff_mesh.vectors = vector_array
    diff_mesh.points = point_array
    return diff_mesh
