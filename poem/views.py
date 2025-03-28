from rest_framework import viewsets
from .models import Poem
from .serializers import PoemSerializer


class LogViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.filter(is_active=True).all()
    serializer_class = PoemSerializer
