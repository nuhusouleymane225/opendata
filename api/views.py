from rest_framework import viewsets, permissions
from .serializers import PharmaSerializer

# Create your views here.
from .models import Pharma



class PharmaViewSet(viewsets.ModelViewSet):
    queryset = Pharma.objects.all()
    serializer_class = PharmaSerializer
    

