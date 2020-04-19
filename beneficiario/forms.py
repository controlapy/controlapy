from django import forms

from .models import Beneficiario

class BeneficiarioForm(forms.ModelForm):

    class Meta:
        model = Beneficiario
        fields = ('cedula', )