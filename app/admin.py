from django.contrib import admin
from .models import Testnet, Notifications
from .models import UserInfo, CheckList
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):

	summernote_fields = ('content')







@admin.register(Testnet)
class TestnetAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage Testnet via the admin panel
    """
    list_filter = ('testnet_name', 'created_on')
    list_display = ('id', 'author', 'testnet_user', 'slug', 'category', 'created_on')
    search_fields = ('testnet_name', 'description')
    summernote_fields = ('description', 'tasks_description')



@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    """
    Allows admin to manage user notifications via the admin panel
    """
    list_display = ('notification_owner', 'title', 'created_on')


@admin.register(UserInfo)
class NotificationsAdmin(admin.ModelAdmin):
    """
    Allows admin to manage user notifications via the admin panel
    """
    list_display = ('user', 'exp', 'created_on')


@admin.register(CheckList)
class NotificationsAdmin(admin.ModelAdmin):
    """
    Allows admin to manage user notifications via the admin panel
    """
    list_display = ('checklist_owner', 'title', 'created_on')

