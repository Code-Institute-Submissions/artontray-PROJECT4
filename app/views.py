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
from .forms import AddNewTestnet


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





def AddTestnet(request):

    if request.method == 'POST':

        form = AddNewTestnet(request.POST)

        if form.is_valid():

            #return HttpResponseRedirect('/dashboard/')
            return render(
            request,
            "index.html",
            {
                "nb_testnet": form.cleaned_data['inputTestnetName'],
                "nb_user": 999
            },
        )


    else:
        form = AddNewTestnet()

    return render(request, 'addtestnet.html', {'form': form})





class ShowDashboard(generic.DetailView):
    """
    This view is used to display User Dashboard informations
    """
    model = User
    template_name = "dashboard.html"
    slug_field = 'object_user'
    slug_url_kwarg = 'object_user'
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



        def get_created_testnet_nb(object_user):
            """
            return the amount of testnet created by the user
            """
            return Testnet.objects.filter(author=object_user).count()

        def get_testnet_total(object_user):
            """
            return the amount of testnet total (copied and created)
            """           
            return TestnetUserInfo.objects.filter(testnet_user=object_user).count()


        def get_testnet_copied(object_user):
            """
            return the amount of copied testnet from the user
            """     
            return get_testnet_total(object_user) - get_created_testnet_nb(object_user)



        def get_Last_Testnet_name(object_user):
            """
            return the Last Testnet Name created by User
            """    
            Last_Testnet = Testnet.objects.filter(author=object_user).first()
            if Last_Testnet:
                Last_Testnet_name = Last_Testnet.testnet_name
            else:
                Last_Testnet_name = 'Not created yet'
            return Last_Testnet_name  

        
        Last_Testnet_name = get_Last_Testnet_name(object_user)


        def get_notifications_nb(object_user):
            """
            return the number of users notifications
            """   
            return Notifications.objects.filter(notification_owner=object_user).count()

        
        def check_user_info_exist(object_user):
            """
            return True if user info exist on Table UserInfo
            """   
            user_info_exist = UserInfo.objects.filter(user_id=object_user).exists()
            return user_info_exist

        queryset = UserInfo.objects.all()
        

        if check_user_info_exist(object_user):
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
        #nb_followers = queryset[0].followers.count()


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
        if get_created_testnet_nb(object_user) > TESTNET_CREATED_FOR_LEVEL1:
            while get_created_testnet_nb(object_user) > How_Much_testnet_To_Create:
                How_Much_testnet_To_Create = int(How_Much_testnet_To_Create * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Testnet = int((get_created_testnet_nb(object_user)/How_Much_testnet_To_Create)*100)

        # User Followers info
        
        How_Much_Followers_To_Have = FOLLOWERS_FOR_LEVEL1
        if nb_followers > FOLLOWERS_FOR_LEVEL1:
            while nb_followers > How_Much_Followers_To_Have:
                How_Much_Followers_To_Have = int(How_Much_Followers_To_Have * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Followers = int((nb_followers/How_Much_Followers_To_Have)*100)


        # User COpied Testnet info
        How_Much_Copied_Testnet_To_Have = TESTNET_TO_COPY_FOR_LEVEL1
        if get_testnet_copied(object_user) > TESTNET_TO_COPY_FOR_LEVEL1:
            while get_testnet_copied(object_user) > How_Much_Copied_Testnet_To_Have:
                How_Much_Copied_Testnet_To_Have = int(How_Much_Copied_Testnet_To_Have * COEFF_FOR_LEVEL_UP)      

        Pourcentage_accomplished_Copied_Testnet = int((get_testnet_copied(object_user)/How_Much_Copied_Testnet_To_Have)*100)


        # User Testnet listing 
        testnet_user = Testnet.objects.filter(author=self.request.user.id)
        paginate_by = 4

        context.update ({
                "object_user": object_user,
                "nb_testnet_user": get_created_testnet_nb(object_user),
                "nb_following": nb_following,
                "nb_followers": nb_followers,
                "nb_testnet_copied_by_user": get_testnet_copied(object_user),
                "nb_notifications_user": get_notifications_nb(object_user),
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
                "created_on": self.object.date_joined
                
            }
        )
        return context


       