from .models import Cat
from rest_framework import viewsets, permissions
from .serializers import CatSerializer
# Create your views here.
class CatViewSet(viewsets.ModelViewSet):
    
    queryset = Cat.objects.all()
    
    serializer_class = CatSerializer
    
    permission_classes = [permissions.AllowAny]