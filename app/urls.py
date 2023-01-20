from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.StatistiqueApp.as_view(), name="home"),
    path('dashboard/', views.ShowDashboard.as_view(), name='dashboard'),
    path('dashboard/<slug:username>', views.ShowDashboard.as_view(), name='dashboard'),
    path('showtestnet/<slug:slug>', views.ShowTestnet.as_view(), name='showtestnet'),
    path('showtestnetall/<slug:username>', views.ShowTestnetall.as_view(), name='showtestnetall'),
    path('addtestnet/', views.AddTestnet, name='addtestnet'),
]
