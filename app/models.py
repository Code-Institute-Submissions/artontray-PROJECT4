from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from django.utils.functional import cached_property
from django.conf import settings

STATUS = ((0, "User"), (1, "Admin"))
READ = ((0, "Unread"), (1, "Read"))



class Testnet(models.Model):
    """
    Model for Testnet Table
    """
    testnet_name = models.CharField(max_length=60, unique=True, blank=False, null=False, db_index=True)
    slug = AutoSlugField(populate_from='testnet_name', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnet_author")
    testnet_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnet_user")    
    slug_original = models.CharField(max_length=60, blank=False, null=False)
    network_name = models.CharField(max_length=25)
    network_status = models.CharField(max_length=25)
    description = models.TextField(db_index=True)
    category = models.CharField(max_length=25)
    twitter = models.CharField(max_length=25, blank=True)
    facebook = models.CharField(max_length=25, blank=True)
    website = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=25, blank=True)
    discord = models.CharField(max_length=25, blank=True)
    telegram = models.CharField(max_length=25, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    youtube = models.CharField(max_length=120, blank=True)
    whitepaper = models.CharField(max_length=255, blank=True)
    browser = models.CharField(max_length=25, blank=True)
    tasks_description = models.TextField()
    wallet1_name = models.CharField(max_length=25, blank=True)
    wallet1_type = models.CharField(max_length=25, blank=True)
    wallet1_link = models.CharField(max_length=255, blank=True)
    wallet1_adress = models.CharField(max_length=255, blank=True)
    wallet1_seed = models.CharField(max_length=255, blank=True)
    wallet1_priv_key = models.CharField(max_length=255, blank=True)
    wallet1_password = models.CharField(max_length=30, blank=True)
    wallet1_session = models.CharField(max_length=30, blank=True)
    wallet1_clue = models.TextField(blank=True)
    wallet2_name = models.CharField(max_length=25, blank=True)
    wallet2_type = models.CharField(max_length=25, blank=True)
    wallet2_link = models.CharField(max_length=255, blank=True)
    wallet2_adress = models.CharField(max_length=255, blank=True)
    wallet2_seed = models.CharField(max_length=255, blank=True)
    wallet2_priv_key = models.CharField(max_length=255, blank=True)
    wallet2_password = models.CharField(max_length=30, blank=True)
    wallet2_session = models.CharField(max_length=30, blank=True)
    wallet2_clue = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    copied_nb = models.IntegerField(default=0, blank=True)
    twitter_user = models.CharField(max_length=21, blank=True)
    email_user = models.EmailField(blank=True)
    website_user = models.CharField(max_length=255, blank=True)
    github_user = models.CharField(max_length=25, blank=True)
    discord_user = models.CharField(max_length=25, blank=True)
    telegram_user = models.CharField(max_length=25, blank=True)
    browser_user = models.CharField(max_length=25, blank=True)
    tasks_results = models.TextField(blank=True)


    class Meta:
        """
        To display the testnet by created_on in descending order
        """
        ordering = ['-created_on']


    #@property
   # def is_owner_current_user(self):

       # def sample_view(request):
       #     current_user = request.user

       # if not hasattr(self, "_is_owner_current_user"):
          #  self._is_owner_current_user = Testnet.objects.all().filter(slug=self.slug).filter(author=request.user)
            

       # return self._is_owner_current_user




    def __str__(self):
        return f"{self.testnet_name}"






class Notifications(models.Model):
    """
    Model for Notifications Table
    """
    notification_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notification_owner")
    title = models.CharField(max_length=35)    
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    read = models.IntegerField(choices=READ, default=0)


    class Meta:
        """
        To display the user notifications created_on in descending order
        """
        ordering = ['-created_on']


    def __str__(self):
        return f"{self.title}"



class UserInfo(models.Model):
    """
    Model for User General Info Table
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_info")
    bio = models.TextField()
    exp = models.IntegerField(default=100)
    status = models.IntegerField(choices=STATUS, default=0)
    debank = models.CharField(max_length=255)
    avatar = CloudinaryField('image', default='placeholder')
    following = models.ManyToManyField(
        User, related_name='following', blank=True)


    class Meta:
        """
        To display the user Info by created_on in descending order
        """
        ordering = ['-user__date_joined']

    @property
    def is_followed_by_user(self, request):
        if not hasattr(self, "_is_followed_by_user"):
            user = UserInfo.objects.get(user=self.user)
            self._is_followed_by_user = user.following.filter(id=request.user.id).exists()
            
    def user_follows(self):
        return self.user.following
            

    @property
    def created_on(self):
        return self.user.date_joined

    @property
    def get_object_user(self):
        return self.user

    @property
    def nb_following(self):
        if not hasattr(self, "_nb_following"):
            self._nb_following = self.following.count()

        return self._nb_following

    @property
    def nb_followers(self):
        if not hasattr(self, "_nb_followers"):
            self._nb_followers = UserInfo.objects.all().filter(following=self.user.id).count()

        return self._nb_followers


    @property
    def nb_testnet(self):
        if not hasattr(self, "_nb_testnet"):
            self._nb_testnet = Testnet.objects.all().filter(author=self.user.id,testnet_user=self.user.id).count()

        return self._nb_testnet

    @property
    def show_testnet_user(self):
        if not hasattr(self, "_show_testnet_user"):
            self._show_testnet_user = Testnet.objects.all().filter(testnet_user=self.user.id)[:5]

        return self._show_testnet_user    

    @property
    def nb_copied_testnet(self):
        if not hasattr(self, "_nb_copied_testnet"):
            self._nb_copied_testnet = Testnet.objects.all().exclude(author=self.user.id).filter(testnet_user=self.user.id).count()

        return self._nb_copied_testnet

    @property
    def nb_notifications(self):
        if not hasattr(self, "_nb_notifications"):
            self._nb_notifications = Notifications.objects.all().filter(notification_owner=self.user.id, read=0).count()

        return self._nb_notifications

    @property
    def last_testnet(self):
        if not hasattr(self, "_last_testnet"):
            self._last_testnet = Testnet.objects.all().filter(author=self.user,testnet_user=self.user).first()
            if self._last_testnet:
                self._last_testnet = self._last_testnet.testnet_name
            else:
                self._last_testnet = 'Not created yet'
        return self._last_testnet

    @property
    def last_testnet_slug(self):
        if not hasattr(self, "_last_testnet_slug"):
            self._last_testnet_slug = Testnet.objects.all().filter(author=self.user,testnet_user=self.user).first()
            if self._last_testnet_slug:
                self._last_testnet_slug = self._last_testnet_slug.slug
            else:
                self._last_testnet_slug = ''
        return self._last_testnet_slug




    @property
    def get_level_user(self):
        Level_user = 1
        Current_Level_XP = settings.EXP_FOR_LEVEL1
        exp = self.exp
        if exp > settings.EXP_FOR_LEVEL1:
            Current_Level_XP = settings.EXP_FOR_LEVEL1 * settings.COEFF_FOR_LEVEL_UP
            while exp > Current_Level_XP:
                Level_user += 1
                Current_Level_XP = Current_Level_XP * settings.COEFF_FOR_LEVEL_UP

        if not hasattr(self, "_get_level_user"):
            self._get_level_user = Level_user

        return self._get_level_user

    @property
    def current_nb_testnet_to_do(self):
        if not hasattr(self, "_current_nb_testnet_to_do"):
            self._current_nb_testnet_to_do = int(settings.TESTNET_CREATED_FOR_LEVEL1+(settings.COEFF_FOR_LEVEL_UP**self.get_level_user))

        return self._current_nb_testnet_to_do 
       

    @property
    def current_level_xp_max(self):
        if not hasattr(self, "_current_level_xp_max"):
            self._current_level_xp_max = int(settings.EXP_FOR_LEVEL1*(settings.COEFF_FOR_LEVEL_UP**self.get_level_user))

        return self._current_level_xp_max

    @property
    def pourc_accomplished_exp(self):
        return (self.exp/self.current_level_xp_max)*100    

    @property
    def pourc_accomplished_testnet(self):
        result = int((self.nb_testnet/self.current_nb_testnet_to_do)*100) 
        if result >= 100:
            return 100
        return result

    @property
    def current_follow_max(self):
        return int(settings.FOLLOWERS_FOR_LEVEL1+(settings.COEFF_FOR_LEVEL_UP**self.get_level_user))

    @property
    def pourc_accomplished_followers(self):
        result = int((self.nb_followers/self.current_follow_max)*100)
        if result >= 100:
            return 100
        return result

    @property
    def current_copied_testnet_max(self):
        return int(settings.TESTNET_TO_COPY_FOR_LEVEL1+(settings.COEFF_FOR_LEVEL_UP**self.get_level_user))

    @property
    def pourc_accomplished_copied_testnet(self):
        result = int((self.nb_copied_testnet/self.current_copied_testnet_max)*100) 
        if result >= 100:
            return 100
        return result




    def __str__(self):
        return f"{self.user}"


class CheckList(models.Model):
    """
    Model for CheckList Info Table
    """
    checklist_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="checklist_owner")
    title = models.CharField(max_length=35)   
    message = models.TextField()
    created_on = models.DateTimeField(auto_now=True)


    class Meta:
        """
        To display the user checklist created_on in descending order
        """
        ordering = ['-created_on']


    def __str__(self):
        return f"{self.title}"
