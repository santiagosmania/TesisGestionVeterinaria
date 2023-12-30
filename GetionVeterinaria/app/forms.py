from django import forms
from .models import Opcion

class OpcionForm(forms.Form):
    opcion = forms.ModelChoiceField(queryset=Opcion.objects.all())
    def __init__(self, *args, **kwargs):
        super(OpcionForm, self).__init__(*args, **kwargs)
        opciones = Opcion.objects.all().values_list('id', 'nombre')
        self.fields['opcion'].choices = opciones