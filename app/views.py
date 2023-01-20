from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testnet
from .models import Notifications, UserInfo, CheckList
from django.contrib.auth.models import User
from django.template import loader,RequestContext
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import AddNewTestnet
from functools import reduce





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






def AddTestnet(request):

    if request.method == 'POST':

        form = AddNewTestnet(request.POST)
    
        if form.is_valid():
        #request.cleaned_data
        #form.author = request.user
        #form.testnet_user = request.user
            form.save()
            return HttpResponseRedirect('/dashboard/')
           


    else:
        form = AddNewTestnet()

    return render(request, 'addtestnet.html', {'form': form})



 







class ShowTestnet(generic.DetailView):
    """
    This view is used to display User Testnet 
    """
    model = Testnet

    template_name = "showtestnet.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    def get_object(self, queryset=None):
        if self.slug_url_kwarg in self.kwargs:
            return super().get_object(queryset)
        else:
            return self.request.user



class ShowTestnetall(generic.DetailView):
    """
    This view is used to display All User Testnet 
    """
    model = User

    template_name = "showtestnetall.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    def get_object(self, queryset=None):
        if self.slug_url_kwarg in self.kwargs:
            return super().get_object(queryset)
        else:
            return self.request.user

    def get_context_data(self, **context):
        # User Testnet listing only the 5 lastest
        testnet_user = Testnet.objects.filter(author=self.request.user)
        paginate_by = 4

        context.update ({
                "testnet_user": testnet_user,




                
            }
        )
        return context



class ShowDashboard(generic.DetailView):
    """
    This view is used to display User Dashboard informations
    """
    model = User
    template_name = "dashboard.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    #object_user = self.kwargs['object_user']
    
    def get_object(self, queryset=None):
        if self.slug_url_kwarg in self.kwargs:
            return super().get_object(queryset)
        else:
            return self.request.user
            
                

    def get_context_data(self, **context):

        request = self.request
        object_user = self.request.user
        nb_following = self.object.user_info.nb_following
        nb_followers = self.object.user_info.nb_followers
        nb_testnet = self.object.user_info.nb_testnet


 





        # User Testnet listing only the 5 lastest
        testnet_user = Testnet.objects.filter(author=self.request.user.id)[:5]
        paginate_by = 4

        context.update ({
                "testnet_user": testnet_user,




                
            }
        )
        return context


       