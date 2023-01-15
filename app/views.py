from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testnet, TestnetUserInfo
from .models import Notifications, UserInfo, CheckList
from django.contrib.auth.models import User
from django.template import loader
from django.views.generic.base import TemplateView



EXP_FOR_LEVEL1 = 500
COEFF_FOR_LEVEL_UP = 1.4
TESTNET_CREATED_FOR_LEVEL1 = 5

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
        #nb_testnet_user = Testnet.objects.filter(id=self.request.user.id).count()
        

        #user = get_object_or_404(UserInfo, id=self.request.user.id)
        #user = get_object_or_404(UserInfo, id=2)
        #user.followers.add(request.user)


        nb_following = 0
        all_users = UserInfo.objects.all()
        for users in all_users:
            #users.followers.add(request.user)
            if users.followers.filter(id=request.user.id).exists():
                nb_following =+ 1

        #nb_followers = username.followers.count()
        created_on = username.date_joined
        nb_testnet_total = TestnetUserInfo.objects.filter(testnet_user=self.request.user.id).count()
        nb_testnet_created_by_user = Testnet.objects.filter(author=self.request.user.id).count()
        nb_testnet_copied_by_user = nb_testnet_total - nb_testnet_created_by_user




        # Followers of the current user
        queryset = UserInfo.objects.filter(user_id=self.request.user.id)
        nb_followers = queryset[0].followers.count()

        
        Last_Testnet = Testnet.objects.filter(id=self.request.user.id).order_by('-created_on')[:1]
        if Last_Testnet:
            Last_Testnet_name = Last_Testnet[0].testnet_name
        else:
            Last_Testnet_name = 'Not created yet'



        nb_notifications_user = Notifications.objects.filter(id=self.request.user.id).count()

        queryset = UserInfo.objects.all()
        
        user_info_exist = UserInfo.objects.filter(user_id=self.request.user.id).exists()
        if user_info_exist:
            user_info = get_object_or_404(queryset, user_id=self.request.user.id)
        # queryset = UserInfo.objects.all()
        #exp = username.exp
            exp = user_info.exp
            debank = user_info.debank
            bio = user_info.bio
            avatar = user_info.avatar
        else:
            # Creating user info table with basic value
            # We fill up the table with none value and 100 exp
            exp = 100
            debank = '...'
            bio = 'I just signed up to Testnet Organizer....'
            avatar = "https://res.cloudinary.com/dqnhlza2r/image/upload/w_1000,ar_16:9,c_fill,g_auto,e_sharpen/v1673725603/avatar_empty_gsx6it.webp"
            Creation_User_Info = UserInfo.objects.create(
                user_id=self.request.user.id,
                bio=bio,
                exp=exp,
                debank=debank,
                avatar=avatar
                )
            Creation_User_Info.save()
            
            
            #messages.success(self.request, 'User Info successfully added')    

       
        # user Level and Exp
        Level_user = 1
        Current_Level_XP = EXP_FOR_LEVEL1
        if exp > EXP_FOR_LEVEL1:
            Current_Level_XP = EXP_FOR_LEVEL1 * COEFF_FOR_LEVEL_UP
            while exp > Current_Level_XP:
                Level_user += 1
                Current_Level_XP = Current_Level_XP * COEFF_FOR_LEVEL_UP


        Pourcentage_accomplished_XP = int((exp/Current_Level_XP)*100)



        # User Testnet Info
        How_Much_testnet_To_Create = TESTNET_CREATED_FOR_LEVEL1
        if nb_testnet_created_by_user > TESTNET_CREATED_FOR_LEVEL1:
            while nb_testnet_created_by_user > How_Much_testnet_To_Create:
                How_Much_testnet_To_Create = int(TESTNET_CREATED_FOR_LEVEL1 * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Testnet = int((nb_testnet_created_by_user/How_Much_testnet_To_Create)*100)


        return render(
            request,
            "dashboard.html",
            {
                "username": username,
                "nb_testnet_user": nb_testnet_created_by_user,
                "nb_following": nb_following,
                "nb_followers": nb_followers,
                "nb_testnet_copied_by_user": nb_testnet_copied_by_user,
                "nb_notifications_user": nb_notifications_user,
                "exp": exp,
                "bio_user": bio,
                "debank_adress": debank,
                "avatar": avatar,
                "Last_Testnet_name": Last_Testnet_name,
                "Level_user": Level_user,
                "Pourcentage_accomplished_XP": Pourcentage_accomplished_XP,
                "Pourcentage_accomplished_Testnet": Pourcentage_accomplished_Testnet,
                "Current_Level_XP": int(Current_Level_XP),
                "How_Much_testnet_To_Create": How_Much_testnet_To_Create,
                "created_on": created_on
                
                
                
            },
        )
