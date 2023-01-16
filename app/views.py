from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testnet, TestnetUserInfo
from .models import Notifications, UserInfo, CheckList
from django.contrib.auth.models import User
from django.template import loader
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy



EXP_FOR_LEVEL1 = 500
FOLLOWERS_FOR_LEVEL1 = 5
COEFF_FOR_LEVEL_UP = 1.4
TESTNET_CREATED_FOR_LEVEL1 = 5
TESTNET_TO_COPY_FOR_LEVEL1 = 2

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
        Get the User, Testnet, UserInfo informations to display on Dashboard
        """

        def get_username(id_user):
            """
            Return username as an Object
            """
            queryset = User.objects.all()
            username = get_object_or_404(queryset, id=id_user)
            return username
        
        username = get_username(self.request.user.id)
        

        def get_Following_user_nb(all_users):
            """
            User is following how much other users?
            """
            nb_following = 0
            all_users = UserInfo.objects.all()
            for users in all_users:
                users.followers.add(1)
                if users.followers.filter(id=request.user.id).exists():
                    nb_following += 1
            return nb_following

        nb_following = get_Following_user_nb(UserInfo.objects.all())
        

        def get_register_date(username):
            """
            return date when user created the account
            """
            return username.date_joined

        
        created_on = get_register_date(username)


        def get_created_testnet_nb(username):
            """
            return the amount of testnet created by the user
            """
            return Testnet.objects.filter(author=username).count()

        def get_testnet_total(username):
            """
            return the amount of testnet total (copied and created)
            """           
            return TestnetUserInfo.objects.filter(testnet_user=username).count()


        def get_testnet_copied(username):
            """
            return the amount of copied testnet from the user
            """     
            return get_testnet_total(username) - get_created_testnet_nb(username)



        def get_Last_Testnet_name(username):
            """
            return the Last Testnet Name created by User
            """    
            Last_Testnet = Testnet.objects.filter(author=username).first()
            if Last_Testnet:
                Last_Testnet_name = Last_Testnet.testnet_name
            else:
                Last_Testnet_name = 'Not created yet'
            return Last_Testnet_name  

        
        Last_Testnet_name = get_Last_Testnet_name(username)


        def get_notifications_nb(username):
            """
            return the number of users notifications
            """   
            return Notifications.objects.filter(notification_owner=username).count()

        
        def check_user_info_exist(username):
            """
            return True if user info exist on Table UserInfo
            """   
            user_info_exist = UserInfo.objects.filter(user_id=username).exists()
            return user_info_exist

        queryset = UserInfo.objects.all()
        

        if check_user_info_exist(username):
            user_info = get_object_or_404(queryset, user_id=self.request.user.id)

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
            
            
            messages.success(self.request, 'User Info successfully added')    
            
       # Followers of the current user
        queryset = UserInfo.objects.filter(user_id=self.request.user.id)
        nb_followers = queryset[0].followers.count()


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
        if get_created_testnet_nb(username) > TESTNET_CREATED_FOR_LEVEL1:
            while get_created_testnet_nb(username) > How_Much_testnet_To_Create:
                How_Much_testnet_To_Create = int(How_Much_testnet_To_Create * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Testnet = int((get_created_testnet_nb(username)/How_Much_testnet_To_Create)*100)

        # User Followers info
        
        How_Much_Followers_To_Have = FOLLOWERS_FOR_LEVEL1
        if nb_followers > FOLLOWERS_FOR_LEVEL1:
            while nb_followers > How_Much_Followers_To_Have:
                How_Much_Followers_To_Have = int(How_Much_Followers_To_Have * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Followers = int((nb_followers/How_Much_Followers_To_Have)*100)


        # User COpied Testnet info
        How_Much_Copied_Testnet_To_Have = TESTNET_TO_COPY_FOR_LEVEL1
        if get_testnet_copied(username) > TESTNET_TO_COPY_FOR_LEVEL1:
            while get_testnet_copied(username) > How_Much_Copied_Testnet_To_Have:
                How_Much_Copied_Testnet_To_Have = int(How_Much_Copied_Testnet_To_Have * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Copied_Testnet = int((get_testnet_copied(username)/How_Much_Copied_Testnet_To_Have)*100)


        # User Testnet listing 
        testnet_user = Testnet.objects.filter(author=self.request.user.id)
        paginate_by = 4

        return render(
            request,
            "dashboard.html",
            {
                "username": username,
                "nb_testnet_user": get_created_testnet_nb(username),
                "nb_following": nb_following,
                "nb_followers": nb_followers,
                "nb_testnet_copied_by_user": get_testnet_copied(username),
                "nb_notifications_user": get_notifications_nb(username),
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
                "Pourcentage_accomplished_Followers": Pourcentage_accomplished_Followers,
                "How_Much_Followers_To_Have": How_Much_Followers_To_Have,
                "Pourcentage_accomplished_Copied_Testnet":Pourcentage_accomplished_Copied_Testnet,
                "How_Much_Copied_Testnet_To_Have":How_Much_Copied_Testnet_To_Have,
                "testnet_user":testnet_user,
                "created_on": created_on
                
                
                
            },
        )
