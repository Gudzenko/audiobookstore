from rest_framework import serializers
from main.models import Audio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Serializers')

class AudioSerializer(serializers.ModelSerializer):
    audio_file = serializers.SerializerMethodField()

    class Meta:
        model = Audio
        fields = ['id', 'audio_name', 'audio_file', 'created_at']

    def get_audio_file(self, obj):
        return self.context['request'].build_absolute_uri(obj.audio_file.url)
