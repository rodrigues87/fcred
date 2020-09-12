from django import forms
from indicacao.models import Indicacao


class IndicacaoForm(forms.ModelForm):
    class Meta:
        model = Indicacao
        fields = ['nome_indicado', 'telefone_indicado', 'autorizado', 'efetivada']
