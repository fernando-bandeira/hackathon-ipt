from django.db import models


class DiffMesh(models.Model):
    stl_file = models.FileField(upload_to='diff_meshes/')
