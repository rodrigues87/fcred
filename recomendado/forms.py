from django import forms
from recomendado.models import Recomendado


class RecomendadoForm(forms.ModelForm):
    class Meta:
        model = Recomendado
        fields = '__all__'
