import datetime                                     #DONT IMPORT DATETIME SUBMODULEs
from rest_framework                                 import generics#, status
from app_factura.serializers                        import FacturaSerializer
from app_factura.models                             import Factura, Plaza
from app_factura.utils                              import precio

class FacturaDetailView(generics.RetrieveAPIView):
    queryset           = Factura.objects.all()
    serializer_class   = FacturaSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class FacturaUpdateView(generics.UpdateAPIView):
    queryset           = Factura.objects.all()
    serializer_class   = FacturaSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class CheckOutView(generics.UpdateAPIView):
    queryset           = Factura.objects.all()
    serializer_class   = FacturaSerializer
    def update(self, request, *args, **kwargs):
        #Le pone la hora de salida
        setattr(request.data, '_mutable', True)
        date_time_now = datetime.datetime.now(datetime.timezone.utc)
        request.data['fecha_salida'] = date_time_now 
        
        #Le pone el precio a la factura
        factura = self.get_object()
        print(date_time_now, factura.fecha_entrada)
        tiempo_en_segundos = (date_time_now - factura.fecha_entrada).total_seconds()
        request.data['costo'] = precio(tiempo_en_segundos)


        #Pone la plaza en disponible
        plaza = Plaza.objects.get(id=request.data['plaza'])
        plaza.isAvailable = True
        plaza.save()
        
        return super().update(request, *args, **kwargs)

class FacturaDeleteView(generics.DestroyAPIView):
    queryset           = Factura.objects.all()
    serializer_class   = FacturaSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

