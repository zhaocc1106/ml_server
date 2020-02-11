from django.urls import path
from . import views

app_name = 'auto_painter'
urlpatterns = [
    # path('', views.list, name='index'),
    # path('<int:auto_painter_id>/', views.detail, name='detail'),
    path('list', views.ListView.as_view(), name='list'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('', views.autoPainter, name='auto_painter')
]