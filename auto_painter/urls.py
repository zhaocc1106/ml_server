from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'auto_painter'
urlpatterns = [
    path('', views.auto_painter, name='auto_painter'),
    # path('list', views.list_view, name='list_view'),
    path('list', views.ListView.as_view(), name='list_view'),
    # path('<int:auto_painter_id>/', views.detail_view, name='detail_view'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail_view'),
    path('insert', views.insert, name='insert'),
]
