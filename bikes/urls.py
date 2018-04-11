from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addbike/', views.addbike, name='addbike'),
    path('bikelist/', views.BikeListView.as_view(), name='bikelist'),
]
