from django.db.models import query
from rest_framework                                 import generics#, status
from app_factura.models                             import Plaza
from app_factura.serializers.plazaSerializer        import PlazaSerializer


class PlazaDetailView(generics.RetrieveAPIView):
    queryset           = Plaza.objects.all()
    serializer_class   = PlazaSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AvailablePlazas(generics.ListAPIView):
    queryset = Plaza.objects.filter(isAvailable=True)
    serializer_class   = PlazaSerializer
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class PlazaUpdateView(generics.UpdateAPIView):
    queryset           = Plaza.objects.all()
    serializer_class   = PlazaSerializer
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class PlazaDeleteView(generics.DestroyAPIView):
    queryset           = Plaza.objects.all()
    serializer_class   = PlazaSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)