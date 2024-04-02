# crafts_panel/urls.py
from django.urls import path
from . import views

app_name = 'crafts_panel'

urlpatterns = [
    path('panels/', views.panel_list, name='panel-list'),
    path('panels/<int:pk>/', views.panel_detail, name='panel-detail'),
]
 