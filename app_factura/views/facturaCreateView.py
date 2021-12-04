from django.core import exceptions
from rest_framework                                 import status, views
from rest_framework.response                        import Response
from app_factura.serializers                        import FacturaSerializer
from app_factura.models                             import Plaza

class FacturaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        plaza = Plaza.objects.get(id=request.data['plaza'])
        
        #Validando que la plaza no esté ocupada
        if plaza.isAvailable == False:
            raise exceptions.FieldError

        #Diciendo que la plaza está ocupada
        plaza.isAvailable = False
        plaza.save()

        return Response(status=status.HTTP_201_CREATED)  