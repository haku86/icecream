from django import forms
from django.forms import ModelForm

from .models import Flavour


class FlavourCreateForm(ModelForm):
    class Meta:
        model = Flavour
        fields = ("name", "color",)

    def __init__(self, *args, **kwargs):
        super(FlavourCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Raspberry Love'
        self.fields['color'].widget.attrs['class'] = 'form-control'
        self.fields['color'].widget.attrs['placeholder'] = '#e94a39'
    
class FlavourUpdateForm(FlavourCreateForm):
    class Meta(FlavourCreateForm.Meta):
        fields = ("name", "color", "scoops_remaining",)    

class ScoopsUpdateForm(ModelForm):
    class Meta:
        model = Flavour
        exclude = ("slug", "name", "color", "scoops_remaining",)    