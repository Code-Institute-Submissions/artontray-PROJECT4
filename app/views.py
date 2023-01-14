from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testnet, TestnetUserInfo
from .models import Notifications, UserInfo, CheckList
from django.contrib.auth.models import User
# from .forms import CommentForm
from django.template import loader
from django.views.generic.base import TemplateView





class StatistiqueApp(generic.ListView):
    """
    This view is used to display some statistics from the app
    """
    def get(self, request):
        """
        Get the Testnet Total number and the User total number 
        """
        
        nb_testnet_total = Testnet.objects.all().count()
        nb_user_total = User.objects.all().count()
  


        return render(
            request,
            "index.html",
            {
                "nb_testnet": nb_testnet_total,
                "nb_user": nb_user_total
            },
        )


class ShowDashboard(generic.ListView):
    """
    This view is used to display User Dashboard informations
    """
    def get(self, request):
        """
        Get the Testnet Info
        """
        queryset = User.objects.all()
        username = get_object_or_404(queryset, id=self.request.user.id)
        nb_testnet_user = Testnet.objects.filter(id=self.request.user.id).count()
        

        #user = get_object_or_404(UserInfo, id=self.request.user.id)
        #user = get_object_or_404(UserInfo, id=3)
        #user.followers.remove(request.user)
        nb_following = 0
        all_users = UserInfo.objects.all()
        for users in all_users:
            if users.followers.filter(id=request.user.id).exists():
                nb_following =+ 1

        nb_followers = username.followers.count()
        
        nb_testnet_total = TestnetUserInfo.objects.filter(id=self.request.user.id).count()
        nb_testnet_created_by_user = Testnet.objects.filter(id=self.request.user.id).count()
        nb_testnet_copied_by_user = nb_testnet_total - nb_testnet_created_by_user

        #nb_following = get_object_or_404(queryset, id=self.request.user.id).count()
        #nb_following = UserInfo.number_of_following(self.request.user)
        # queryset = UserInfo.objects.filter(id=self.request.user.id)
        # nb_followers = queryset.followers.count()


        nb_notifications_user = Notifications.objects.filter(id=self.request.user.id).count()

        #queryset = UserInfo.objects.all()
        #username = get_object_or_404(queryset, id=self.request.user.id)
        user_info = UserInfo.objects.filter(id=self.request.user.id)
        # queryset = UserInfo.objects.all()
        #exp = username.exp

        if user_info:
            exp = user_info[0].exp
        else:
            # We fill up the table with none value and 100 exp
            o = UserInfo.objects.create(
                user_id=self.request.user.id,
                bio='Nothing here',
                exp=100,
                debank='...',
                avatar="https://res.cloudinary.com/dqnhlza2r/image/upload/w_1000,ar_16:9,c_fill,g_auto,e_sharpen/v1673725603/avatar_empty_gsx6it.webp"
                )
            o.save()
            exp = 100
            #messages.success(self.request, 'Comment successfully added')    



        return render(
            request,
            "dashboard.html",
            {
                "username": username,
                "nb_testnet_user": nb_testnet_user,
                "nb_following": nb_following,
                "nb_followers": nb_followers,
                "nb_testnet_copied_by_user": nb_testnet_copied_by_user,
                "nb_notifications_user": nb_notifications_user,
                "exp": exp,
                
                
            },
        )
