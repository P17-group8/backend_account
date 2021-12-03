from django.db import models
from django.db.models.deletion import PROTECT, SET_NULL
from .plaza import Plaza

class Factura(models.Model):
    id_factura    = models.BigAutoField(primary_key=True)
    id_operador   = models.BigIntegerField() 
    id_vehículo   = models.BigIntegerField() 
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida  = models.DateTimeField(null=True)
    costo         = models.IntegerField(default=0)
    plaza         = models.OneToOneField(Plaza, on_delete=PROTECT, null=False)
    