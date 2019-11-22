"""urls management"""
from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.index, name='index'),
    path('credits/', views.credits, name='credits'),
    path('search/', views.search, name='search'),
    path('substitute/<str:product_id>/', views.detail, name='detail'),
    path('favorite/<str:product_id>/', views.favorite, name='favorite'),
]
