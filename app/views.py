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
       
  


        return render(
            request,
            "dashboard.html",
            {
                "username": username
                
            },
        )
 