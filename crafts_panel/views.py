from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Panel
from .serializers import PanelSerializer

@api_view(['GET'])
def panel_list(request):
    panels = Panel.objects.filter(published=True)
    serializer = PanelSerializer(panels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def panel_detail(request, pk):
    panel = get_object_or_404(Panel, pk=pk)
    serializer = PanelSerializer(panel)
    return Response(serializer.data)



"""    from rest_framework import generics, status
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
        }) """