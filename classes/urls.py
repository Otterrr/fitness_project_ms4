from django.urls import path
from . import views

urlpatterns = [
    path('', views.classes, name="classes"),
    path('<int:classes_id>/', views.classes_detail, name="classes_detail"),
]
