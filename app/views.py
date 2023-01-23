from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Testnet
from .models import Notifications, UserInfo, CheckList
from django.contrib.auth.models import User
from django.template import loader,RequestContext
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TestnetForm
from functools import reduce
from django.conf import settings




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


def add_exp_user(user):
    user_info = UserInfo.objects.get(user=user)
    user_info.exp += settings.EXP_PER_ACTION*settings.COEFF_FOR_LEVEL_UP
    user_info.save()

def add_notification_user(user, message, title):
    creation_notification = Notifications.objects.create(
                notification_owner=user,
                message=message,
                title=title
                )
    creation_notification.save()


class FormTestnetMixin:
    model = Testnet
    success_url = '/dashboard/'
    form_class = TestnetForm
    success_msg = "Le testnet a bien été enregistré \o/"
    action = "none"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, self.success_msg)
        if self.action=='AddTestnet':
            add_exp_user(self.request.user)
            add_notification_user(self.request.user, "You had a new testnet successfully" , "New testnet created")
        

        return super().form_valid(form)


class AddTestnet(FormTestnetMixin, generic.CreateView):
    action = "AddTestnet"
    success_msg = "Le testnet a bien été créé \o/"

class UpdateTestnet(FormTestnetMixin,LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    action = 'UpdateTestnet'

    def test_func(self):
        testnet = self.get_object()
        """avoiding updating others testnet"""
        return testnet.testnet_user.username == self.request.user.username

    success_msg = "Le testnet a bien été modifié \o/"

# Autre façon de faire, en fonction, mais ça gère moins de chose:
# def add_testnet(request):
#     if request.method == 'POST':
#         form = AddNewTestnet(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Le testnet a bien été créé \o/")
#             return HttpResponseRedirect('/dashboard/')
#     else:
#         form = AddNewTestnet(user=request.user)
#     return render(request, 'addtestnet.html', {'form': form})


class AddFavoriteUser(generic.DetailView):
    def get(self, request, id, *args, **kwargs):
        current_user = UserInfo.objects.get(user=request.user.id)
        user_to_follow = User.objects.get(id=id)
        current_user.following.add(user_to_follow)
        current_user.save()
        add_exp_user(user_to_follow)
        add_notification_user(user_to_follow, "%s is following you!" % (self.request.user) , "New follower +1")
        add_notification_user(self.request.user, "You are now following %s" % (user_to_follow) , "Following a new user +1")
        
        return HttpResponseRedirect(reverse('dashboard', args=[request.user.username]))


class UpdateNotifications(LoginRequiredMixin, View):

    def get(self, request, id, *args, **kwargs):
        queryset = Notifications.objects.filter(notification_owner=request.user.id)
        notif = get_object_or_404(queryset, id=id)
        if notif.read == 0:
            notif.read = 1
            notif.save()
        return HttpResponseRedirect(reverse('show_notifications', args=[request.user.username]))
        



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



class ShowNotifications(generic.DetailView):
    """
    This view is used to display All User Notifications
    """
    model = User

    template_name = "shownotifications.html"
    slug_field = 'username'
    slug_url_kwarg = 'username'
    def get_object(self, queryset=None):
        if self.slug_url_kwarg in self.kwargs:
            return super().get_object(queryset)
        else:
            return self.request.user

    def get_context_data(self, **context):
        # User Testnet listing only the 5 lastest
        notifications_user_unread = Notifications.objects.filter(notification_owner=self.request.user, read=0)[:5]
        notifications_user_read = Notifications.objects.filter(notification_owner=self.request.user, read=1)[:25]
        paginate_by = 4

        context.update ({
                "notifications_user_unread": notifications_user_unread,
                "notifications_user_read": notifications_user_read,


            }
        )
        return context


class ShowTestnetall(generic.ListView):
    """
    This view is used to display All User Testnet 
    """
    model = Testnet
    template_name = "showtestnetall.html"
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        self.testnet_user = self.get_user()
        return super().get(request, *args, **kwargs)
    
    def get_user(self):
        if "username" in self.kwargs:
            return get_object_or_404(User, username=self.kwargs["username"])
        return self.request.user

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(testnet_user=self.testnet_user)
        search = self.request.GET.get("searching", None)
        if search:
            qs = qs.filter(
                Q(testnet_name__icontains=search) 
                | Q(description__icontains=search)
            )
        return qs

    def get_context_data(self, **context):
        # User Testnet listing only the 5 lastest
        context = super().get_context_data(**context)
        context.update({
                "testnet_user": self.testnet_user,
                "searching": self.request.GET.get("searching", None),
            }
        )
        return context

class ShowUsers(generic.DetailView):
    """
    This view is used to display User Dashboard informations
    """
    model = User
    template_name = "users.html"
    paginate_by = 6
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
        
        show_best_users = UserInfo.objects.all().order_by('-exp')[:10]

        context.update ({
                "show_best_users": show_best_users,




                
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

        def check_user_info_exist(object_user):
            """
            return True if user info exist on Table UserInfo
            """   
            user_info_exist = UserInfo.objects.filter(user_id=object_user.id).exists()
            return user_info_exist
        if not check_user_info_exist(object_user):
            # Creating user info table with basic value
            # We fill up the table with none value and 100 exp
            exp = 100
            debank = '...'
            bio = 'I just signed up to Testnet Organizer....'
            avatar = "https://res.cloudinary.com/dqnhlza2r/image/upload/v1674505891/png-transparent-youtube-user-computer-icons-information-youtube-hand-silhouette-avatar_ely5ye.png"
            Creation_User_Info = UserInfo.objects.create(
                user_id=self.request.user.id,
                bio=bio,
                exp=exp,
                debank=debank,
                avatar=avatar
                )
            Creation_User_Info.save()

        # User Testnet listing only the 5 lastest
        testnet_user = Testnet.objects.filter(author=object_user.id)[:5]
        paginate_by = 4

        context.update ({
                "testnet_user": testnet_user,
            }
        )
        return context


       