from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.StatistiqueApp.as_view(), name="home"),
    path('dashboard/', views.ShowDashboard.as_view(), name='dashboard'),
    path('dashboard/<slug:username>', views.ShowDashboard.as_view(), name='dashboard'),
    path('users/', views.ShowUsers.as_view(), name='showusers'),
    #path('search/<slug:searching_user>', views.SearchingUser.as_view(), name='searching_users'),
    path('notifications/<slug:username>', views.ShowNotifications.as_view(), name='show_notifications'),
    path('showtestnet/<slug:slug>', views.ShowTestnet.as_view(), name='showtestnet'),
    path('showtestnetall/<slug:username>', views.ShowTestnetall.as_view(), name='showtestnetall'),
    path('addfavorite/<int:id>', views.AddFavoriteUser.as_view(), name='add_favorite_user'),
    
    path('deletefavorite/<int:id>', views.DeleteFavoriteUser.as_view(), name='delete_favorite_user'),
    path('notification/<int:id>/update', views.UpdateNotifications.as_view(), name='updatenotification'),
    path('addtestnet/', views.AddTestnet.as_view(), name='addtestnet'),
    path('copytestnet/<slug:slug>', views.CopyTestnet.as_view(), name='copy_testnet'),
    path('edittestnet/<slug:slug>', views.UpdateTestnet.as_view(), name='update_testnet'),
]
