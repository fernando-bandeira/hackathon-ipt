from .models import DiffMesh
from rest_framework import serializers


class DiffMeshSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiffMesh
        fields = '__all__'
