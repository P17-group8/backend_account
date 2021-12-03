from rest_framework                                 import status, views
from rest_framework.response                        import Response
from app_factura.serializers                        import FacturaSerializer
from app_factura.models                             import Plaza

class FacturaCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        #Diciendo que la plaza está ocupada
        plaza = Plaza.objects.get(id=request.data['plaza'])
        plaza.isAvailable = False
        plaza.save()

        return Response(status=status.HTTP_201_CREATED)  