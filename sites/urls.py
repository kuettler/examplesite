from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:site_id>/', views.site, name='site'),
]
