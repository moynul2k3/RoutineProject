from django.urls import path
from . import views

urlpatterns = [
    path('my_shedule/', views.shedule_view, name='my_shedule')
]
