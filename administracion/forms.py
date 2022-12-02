from django import forms
from .models import Bus, Chofer,Atractivo

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = '__all__'

class AtractivoForm(forms.ModelForm):
    class Meta:
        model = Atractivo
        fields = '__all__'
