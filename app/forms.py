from django import forms
from .models import Testnet
from .models import UserInfo
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect
from django.conf import settings

class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"
        exclude = ['user', 'exp', 'status','following']

        widgets = {
          'bio': forms.Textarea(attrs={'rows':5, 'cols':45}),
        }
        
        labels = {
            'bio': 'Describe Yourself',
            'debank': 'Your Debank link',
            'avatar': 'Change your Avatar',

        }


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        
        if not self.instance.pk:
            self.instance.user = self.user

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = ''

        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'
        self.fields['debank'].widget.attrs['placeholder'] = 'https://debank.com/profile/0x56.....ea'

        def clean(self):
            super().clean()
            return self.cleaned_data


class TestnetForm(forms.ModelForm):
    #inputTestnetName = forms.CharField(label='Testnet name', max_length=60)

    class Meta:
        model = Testnet
        fields = "__all__"
        exclude = ['author', 'testnet_user', 'slug_original', 'status_testnet']

        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':45}),
          'description': forms.TextInput(attrs={'placeholder': 'quick description'})
        }
        
        labels = {
            'testnet_name': 'Name',
            'discord_user': 'Discord',
            'website_user': 'Link with informations about this testnet',
        }




    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        
        if not self.instance.pk:
            self.instance.author = self.user
            self.instance.testnet_user = self.user

        
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'        
        self.fields['testnet_name'].widget.attrs['placeholder'] = 'Testnet Name'
        self.fields['network_name'].widget.attrs['placeholder'] = 'Goerli, Mumbai, Polygon Mainnet etc...'
        #self.fields['description'].widget.attrs['placeholder'] = ''
        self.fields['category'].widget.attrs['placeholder'] = 'Defi, Bridge, L2, NFT etc...'
        self.fields['network_status'].widget.attrs['placeholder'] = 'Testnet, Devnet, Mainnet etc...'
        self.fields['twitter'].widget.attrs['placeholder'] = 'Example @Testnet_1_official'
        self.fields['facebook'].widget.attrs['placeholder'] = 'facebook link'
        self.fields['website'].widget.attrs['placeholder'] = 'Provide the official website....'
        self.fields['github'].widget.attrs['placeholder'] = 'Provide Github username'
        self.fields['discord'].widget.attrs['placeholder'] = 'Provide discord link....'
        self.fields['telegram'].widget.attrs['placeholder'] = 'Provide telegram link....'
        self.fields['instagram'].widget.attrs['placeholder'] = 'Provide instagram link....'
        self.fields['youtube'].widget.attrs['placeholder'] = 'Provide youtube link....'
        self.fields['whitepaper'].widget.attrs['placeholder'] = 'Provide whitepaper link....'
        self.fields['browser'].widget.attrs['placeholder'] = 'Brave, Firefox, Opera etc...'
        self.fields['discord_user'].widget.attrs['placeholder'] = 'example : username#4565'
        self.fields['github_user'].widget.attrs['placeholder'] = 'example :  https://github.com/John-Doe'
        self.fields['email_user'].widget.attrs['placeholder'] = 'Provide Your email'
        self.fields['twitter_user'].widget.attrs['placeholder'] = 'example :  @Yourname'
        self.fields['telegram_user'].widget.attrs['placeholder'] = 'example :  @Yourname'
        self.fields['website_user'].widget.attrs['placeholder'] = 'Provide a link'
        self.fields['wallet1_name'].widget.attrs['placeholder'] = 'Metamask, Keplr, Martian....'
        self.fields['wallet1_type'].widget.attrs['placeholder'] = 'Extension, Desktop, web wallet...'
        self.fields['wallet1_adress'].widget.attrs['placeholder'] = '0x4125.........61ae'
        self.fields['wallet1_priv_key'].widget.attrs['placeholder'] = 'only if test wallet'
        self.fields['wallet1_seed'].widget.attrs['placeholder'] = 'only if test wallet'
        self.fields['wallet1_clue'].widget.attrs['placeholder'] = 'Be smart and give some details that ONLY YOU can understand'
        self.fields['wallet1_password'].widget.attrs['placeholder'] = 'Wallet password'
        self.fields['wallet1_session'].widget.attrs['placeholder'] = 'Browser session'
        self.fields['wallet1_link'].widget.attrs['placeholder'] = 'link to download this wallet'
        self.fields['wallet2_name'].widget.attrs['placeholder'] = 'Metamask, Keplr, Martian....'
        self.fields['wallet2_type'].widget.attrs['placeholder'] = 'Extension, Desktop, web wallet...'
        self.fields['wallet2_adress'].widget.attrs['placeholder'] = '0x4125.........61ae'
        self.fields['wallet2_priv_key'].widget.attrs['placeholder'] = 'only if test wallet'
        self.fields['wallet2_seed'].widget.attrs['placeholder'] = 'only if test wallet'
        self.fields['wallet2_clue'].widget.attrs['placeholder'] = 'Be smart and give some details that ONLY YOU can understand'
        self.fields['wallet2_password'].widget.attrs['placeholder'] = 'Wallet password'
        self.fields['wallet2_session'].widget.attrs['placeholder'] = 'Browser session'
        self.fields['wallet2_link'].widget.attrs['placeholder'] = 'link to download'
        self.fields['tasks_description'].widget.attrs['placeholder'] = 'Give description of what to do to participate to this testnet'
        self.fields['tasks_results'].widget.attrs['placeholder'] = 'Save your transaction links, data about your participation, copy email etc...'
        
        #if self.instance.pk:
            #self.fields['testnet_name'].disabled = True
        if not self.instance.author == self.user:
            self.fields['wallet1_name'].disabled = True
            for input_name in self.fields:

                array_input = [
                    'telegram_user',
                    'testnet_name',
                    'github_user',
                    'discord_user',
                    'twitter_user',
                    'email_user',
                    'wallet1_adress',
                    'wallet1_priv_key',
                    'wallet1_seed',
                    'wallet1_clue',
                    'wallet1_password',
                    'wallet1_session',
                    'tasks_results',
                    'wallet2_adress',
                    'wallet2_priv_key',
                    'wallet2_seed',
                    'wallet2_clue',
                    'wallet2_password',
                    'wallet2_session'

                    

                ]

                if input_name in array_input:
                    pass
                else:
                    self.fields[input_name].disabled = True

    def clean(self):
        super().clean()

        if self.instance.pk:
            return self.cleaned_data
        base_slug = slugify(self.cleaned_data["testnet_name"])
        suffix = 0
        while True:
            if not suffix:
                slug_original = base_slug
            else:
                slug_original = "%s-%d" % (base_slug, suffix)
            if not self._meta.model.objects.filter(slug_original=slug_original).exists():
                break
            suffix += 1
        self.cleaned_data["slug_original"] = slug_original
        self.instance.slug_original = slug_original
        return self.cleaned_data