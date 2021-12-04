from rest_framework import serializers
from app_factura.models import Factura
from app_factura.models import Plaza
from django.utils.timezone import make_naive

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ['id_operador', 'id_vehículo', 'fecha_entrada','fecha_salida','costo','plaza']
    def to_representation(self, obj):
        factura = Factura.objects.get(id_factura=obj.id_factura)
        plaza = Plaza.objects.get(id=factura.plaza.id)
        return{
            'id_factura': factura.id_factura,   
            'id_operador': factura.id_operador, 
            'id_vehículo': factura.id_vehículo,
            'fecha_entrada': make_naive(factura.fecha_entrada).strftime("%d %B %Y %X "),
            'fecha_salida': make_naive(factura.fecha_salida).strftime("%d %B %Y %X"),
            'costo': factura.costo,
            'plaza':{
                'id': plaza.id,
                'isAvailable': plaza.isAvailable,
            }
        }
