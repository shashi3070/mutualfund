from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getindexdata/', views.GetIndexData, name='GetIndexData'),
]