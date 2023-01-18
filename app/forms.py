from django import forms
from .models import Testnet

class AddNewTestnet(forms.ModelForm):
    #inputTestnetName = forms.CharField(label='Testnet name', max_length=60)

    class Meta:
        model = Testnet
        #fields = "__all__"
        exclude = ['author']