from django.urls import path

from . import views

urlpatterns = [
    path('carbonfootprint_calculation', views.carbonfootprint_calculation),
    path('treek_calculation', views.treek_calculation),
]