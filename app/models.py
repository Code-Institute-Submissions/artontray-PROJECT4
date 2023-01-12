from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from cloudinary.models import CloudinaryField


STATUS = ((0, "User"), (1, "Admin"))
READ = ((0, "Unread"), (1, "Read"))


class Testnet(models.Model):
    """
    Model for Testnet Table
    """
    testnet_name = models.CharField(max_length=60, unique=True)
    slug = AutoSlugField(populate_from='testnet_name', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnets")
    network_name = models.CharField(max_length=25)
    network_status = models.CharField(max_length=25)
    description = models.TextField()
    category = models.CharField(max_length=25)
    twitter = models.CharField(max_length=25)
    facebook = models.CharField(max_length=25)
    website = models.CharField(max_length=255)
    github = models.CharField(max_length=25)
    discord = models.CharField(max_length=25)
    telegram = models.CharField(max_length=25)
    instagram = models.CharField(max_length=255)
    youtube = models.CharField(max_length=120)
    whitepaper = models.CharField(max_length=255)
    browser = models.CharField(max_length=25)
    tasks_description = models.TextField()
    wallet1_name = models.CharField(max_length=25)
    wallet1_type = models.CharField(max_length=25)
    wallet1_link = models.CharField(max_length=255)
    wallet2_name = models.CharField(max_length=25)
    wallet2_type = models.CharField(max_length=25)
    wallet2_link = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    copied_nb = models.IntegerField(default=0)

    class Meta:
        """
        To display the testnet by created_on in descending order
        """
        ordering = ['-created_on']

    def get_absolute_url(self):
        """
        Get url after editing a testnet
        """
        return reverse('testnet_details', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.testnet_name}"



class TestnetUserInfo(models.Model):
    """
    Model for Testnet User Info Table
    """
    testnet = models.ForeignKey(
        Testnet, on_delete=models.CASCADE, related_name="testnet_user_info")
    testnet_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testnet_user")
    wallet1_adress = models.CharField(max_length=255)
    wallet1_seed = models.CharField(max_length=255, default="none")
    wallet1_priv_key = models.CharField(max_length=255, default="none")
    wallet1_password = models.CharField(max_length=30, default="none")
    wallet1_session = models.CharField(max_length=30, default="none")
    wallet1_clue = models.TextField(blank=True)
    wallet2_adress = models.CharField(max_length=255, default="none")
    wallet2_seed = models.CharField(max_length=255, default="none")
    wallet2_priv_key = models.CharField(max_length=255, default="none")
    wallet2_password = models.CharField(max_length=30, default="none")
    wallet2_session = models.CharField(max_length=30, default="none")
    wallet2_clue = models.TextField(blank=True)
    twitter = models.CharField(max_length=21)
    email = models.EmailField()
    website = models.CharField(max_length=255)
    github = models.CharField(max_length=25)
    discord = models.CharField(max_length=25)
    telegram = models.CharField(max_length=25)
    browser = models.CharField(max_length=25)
    tasks_results = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)



    class Meta:
        """
        To display the copied testnet by created_on in descending order
        """
        ordering = ['-created_on']


    def __str__(self):
        return f"{self.testnet}"






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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_id")
    bio = models.TextField()
    exp = models.IntegerField(default=100)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    debank = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    avatar = CloudinaryField('image', default='placeholder')
    followers = models.ManyToManyField(
        User, related_name='followers', blank=True)


    class Meta:
        """
        To display the user Info by created_on in descending order
        """
        ordering = ['-created_on']

    def number_of_followers(self):
        return self.followers.count()


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
