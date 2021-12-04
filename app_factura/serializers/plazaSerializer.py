from rest_framework import serializers
from app_factura.models import Plaza

class PlazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plaza
        fields = ['id','isAvailable',]
    def to_representation(self, obj):
        plaza = Plaza.objects.get(id=obj.id)
        return {
            'idPlaza': plaza.id,
            'isAvailable': plaza.isAvailable,
        }
