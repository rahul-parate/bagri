from django.urls import path

from . import views

urlpatterns = [
    path('firstme/', views.FirstView.as_view(), name='firstme'),
]