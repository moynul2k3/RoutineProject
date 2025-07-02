from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('routeen-list/', views.routeenList, name='routeenlist'),
    path('routeen/<int:pk>/', views.routeen, name='routeen'),
]
