# crafts_panel/urls.py
from django.urls import path
from . import views

app_name = 'crafts_panel'

urlpatterns = [
    path('api/panel/<int:panel_id>/', views.panel_detail_api, name='panel_detail_api'),
    path('panel/<int:panel_id>/', views.panel_detail, name='panel_detail'),
    path('admin/panel/', views.PanelCreateView.as_view(), name='panel-create'),
    path('panel/<int:pk>/', views.PanelDetailView.as_view(), name='panel-detail'),
]
 