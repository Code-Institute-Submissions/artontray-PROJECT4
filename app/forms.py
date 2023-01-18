from django import forms
from .models import Testnet

class AddNewTestnet(forms.ModelForm):
    #inputTestnetName = forms.CharField(label='Testnet name', max_length=60)

    class Meta:
        model = Testnet
        #fields = "__all__"
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super(AddNewTestnet, self).__init__(*args, **kwargs)

        self.fields['network_name'].widget.attrs['placeholder'] = 'Goerli, Mumbai, Polygon Mainnet etc...'
        self.fields['description'].widget.attrs['placeholder'] = 'quick description'
        self.fields['category'].widget.attrs['placeholder'] = 'Defi, Bridge, L2, NFT etc...'
        self.fields['network_status'].widget.attrs['placeholder'] = 'Testnet, Devnet, Mainnet etc...'
        
        