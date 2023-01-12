from django.contrib import admin
from .models import Testnet, TestnetUserInfo, Notifications
from .models import UserInfo, CheckList
# Register your models here.
admin.site.register(Testnet)
admin.site.register(TestnetUserInfo)
admin.site.register(Notifications)
admin.site.register(UserInfo)
admin.site.register(CheckList)