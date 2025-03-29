from django.shortcuts import render
from django.views import View

from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets

from .serializers import PoemSerializer
from .models import Poem


class PoemApiView(viewsets.ModelViewSet):
    queryset = Poem.objects.filter(is_active=True).all()
    serializer_class = PoemSerializer
    

class DivinationApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = PoemSerializer

    def get(self, request: Request):
        divination = Poem.objects.order_by('?').first()
        serializer = self.get_serializer(divination)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IndexView(View):
    def get(self, request):
        return render(request, 'poem/index.html')


class DivinationView(View):
    def get(self, request):
        divination = Poem.objects.order_by('?').first()

        context = {
            "divination": divination
        }

        return render(request, 'poem/divination.html', context)
