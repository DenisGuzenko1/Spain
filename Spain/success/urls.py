from django.urls import path

from success import views

urlpatterns = [
    path('', views.success, name='success')
]
