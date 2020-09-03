from django import forms
from dietas.models import Dieta


class DietaForm(forms.ModelForm):
    class Meta:
        model = Dieta
        fields = ['nome', 'alimentos','usuario']
