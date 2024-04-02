from rest_framework import serializers
from .models import Panel

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ['id', 'owner', 'title', 'content', 'image', 'alt_text', 'video_url', 'created_at', 'published']
