from rest_framework import generics, status
from django.views.generic import DetailView
from django.http import JsonResponse
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser
from .models import Panel
from .serializers import PanelSerializer
from django.shortcuts import render

class PanelCreateView(generics.CreateAPIView):
    queryset = Panel.objects.all()
    serializer_class = PanelSerializer
    permission_classes = [IsAdminUser]


    def perform_create(self, serializer):
        if not self.request.user.is_staff:
            raise PermissionDenied("You do not have permission to create a panel post.")
        serializer.save()

def panel_detail(request, panel_id):
    panel = Panel.objects.get(pk=panel_id)
    return render(request, 'panel_detail.html', {'panel': panel})

def panel_detail_api(request, panel_id):
    panel = Panel.objects.get(pk=panel_id)
    return JsonResponse({
        'title': panel.title,
        'image': panel.image.url if panel.image else None,
        'content': panel.content,
    })