import logging
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Audio
from .serializers import AudioSerializer
from core.user.serializers import UserSerializer, User


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Main')


class AudiosViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        file = request.data['audio_file']
        instance.audio_file.save(file.name, file, save=True)
        instance.audio_name = request.data['audio_name']
        instance.save()
        return Response(self.get_serializer(instance).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    return HttpResponse("Hello world!")