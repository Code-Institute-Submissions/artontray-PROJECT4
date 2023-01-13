from django.contrib import admin
from .models import Testnet, TestnetUserInfo, Notifications
from .models import UserInfo, CheckList
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):

	summernote_fields = ('content')




admin.site.register(UserInfo)
admin.site.register(CheckList)



@admin.register(Testnet)
class TestnetAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage Testnet via the admin panel
    """
    list_filter = ('testnet_name', 'created_on')
    list_display = ('author', 'slug', 'category', 'created_on')
    search_fields = ('testnet_name', 'description')
    summernote_fields = ('description', 'tasks_description')


@admin.register(TestnetUserInfo)
class TestnetUserAdmin(SummernoteModelAdmin):
    """
    Allows admin to manage User Testnet Info via the admin panel
    """
    list_display = ('testnet', 'testnet_user', 'created_on')
    summernote_fields = ('tasks_results')

@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    """
    Allows admin to manage user notifications via the admin panel
    """
    list_display = ('notification_owner', 'title', 'created_on')