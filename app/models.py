from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField
from django.utils.functional import cached_property


STATUS = ((0, "User"), (1, "Admin"))
READ = ((0, "Unread"), (1, "Read"))


class Testnet(models.Model):
    """
    Model for Testnet Table
    """
    testnet_name = models.CharField(max_length=60, unique=True, blank=False, null=False)
    slug = AutoSlugField(populate_from='testnet_name', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnet_author")
    testnet_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnet_user")    
    network_name = models.CharField(max_length=25)
    network_status = models.CharField(max_length=25)
    description = models.TextField()
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
    copied_nb = models.IntegerField(default=0)
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
    def created_on(self):
        return self.user.date_joined

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
            self._nb_testnet = Testnet.objects.all().filter(author=self.user.id).count()

        return self._nb_testnet

    @property
    def nb_copied_testnet(self):
        if not hasattr(self, "_nb_copied_testnet"):
            self._nb_copied_testnet = Testnet.objects.all().exclude(author=self.user.id).filter(testnet_user=self.user.id).count()
            
                

        return self._nb_copied_testnet


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
