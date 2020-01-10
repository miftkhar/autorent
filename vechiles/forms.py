# get a way to log the errors:
from django.forms import CheckboxSelectMultiple
from . import models
from django import forms
from dal import autocomplete
from django.utils.encoding import force_text
import logging
log = logging.getLogger(__name__)
# convert the errors to text


class FeatureForm(forms.ModelForm):
    #feature = forms.MultipleChoiceField(choices=models.Feature, widget=forms.CheckboxSelectMultiple( ))
    formfield_overrides = {
        models.CarFeature: {'widget': CheckboxSelectMultiple},
    }


class CarForm(forms.ModelForm):
    def is_valid(self):
        log.info(force_text(self.errors))
        return super(CarForm, self).is_valid()

    make = forms.ModelChoiceField(
        queryset=models.Make.objects.all(),
        widget=autocomplete.ModelSelect2(url='make-autocomplete'))

    model = forms.ModelChoiceField(
        queryset=models.VModel.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='model-autocomplete',
            forward=('make',)))

    version = forms.ModelChoiceField(
        queryset=models.Version.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='version-autocomplete',
            forward=('model',)))

    class Meta:
        model = models.Car
        fields = '__all__'
        # widgets = {
        #     'description': CKEditorWidget(attrs={'lang': 'es'}),
        # }

    class Media:
        js = (
            'city_autocomplete.js',
        )

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        #self.fields['make'].required = False
        #self.fields['model'].required = False
