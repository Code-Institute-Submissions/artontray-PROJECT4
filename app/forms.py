from django import forms
from .models import Testnet
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, redirect

class TestnetForm(forms.ModelForm):
    #inputTestnetName = forms.CharField(label='Testnet name', max_length=60)

    class Meta:
        model = Testnet
        fields = "__all__"
        exclude = ['author', 'testnet_user', 'slug_original']

        widgets = {
          'description': forms.Textarea(attrs={'rows':2, 'cols':45}),
          'description': forms.TextInput(attrs={'placeholder': 'quick description'})
        }
        
        labels = {
            'testnet_name': 'Name',
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
        self.fields['github'].widget.attrs['placeholder'] = 'Provide Github link....'
        self.fields['discord'].widget.attrs['placeholder'] = 'Provide discord link....'
        self.fields['telegram'].widget.attrs['placeholder'] = 'Provide telegram link....'
        self.fields['instagram'].widget.attrs['placeholder'] = 'Provide instagram link....'
        self.fields['youtube'].widget.attrs['placeholder'] = 'Provide youtube link....'
        self.fields['whitepaper'].widget.attrs['placeholder'] = 'Provide whitepaper link....'
        self.fields['browser'].widget.attrs['placeholder'] = 'Provide browserlink....'
        self.fields['discord_user'].widget.attrs['placeholder'] = 'example : username#4565'
        self.fields['github_user'].widget.attrs['placeholder'] = 'example :  https://github.com/John-Doe'
        self.fields['email_user'].widget.attrs['placeholder'] = 'Provide Your email'
        self.fields['twitter_user'].widget.attrs['placeholder'] = 'example :  @Yourname'
        self.fields['telegram_user'].widget.attrs['placeholder'] = 'example :  @Yourname'
        self.fields['wallet1_name'].widget.attrs['placeholder'] = 'Metamask, Keplr, Martian....'
        self.fields['wallet1_type'].widget.attrs['placeholder'] = 'Extension, Desktop, web wallet...'
        self.fields['wallet1_adress'].widget.attrs['placeholder'] = '0x4125.........61ae'
        if self.instance.pk:
            self.fields['testnet_name'].disabled = True

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