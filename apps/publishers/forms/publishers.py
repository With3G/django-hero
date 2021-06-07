from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *


class PublisherForm(forms.ModelForm):

    name = forms.CharField(
        label=_('Name'),
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = Publisher
        fields = ('name', )

    def __init__(self, *args, **kwargs):
        self.required = kwargs.pop('required', None)
        self.readonly = kwargs.pop('readonly', None)
        self.disabled = kwargs.pop('disabled', None)
        super().__init__(*args, **kwargs)

        if self.required:
            if self.required == 'all':
                for x in self.fields:
                    self.fields[x].widget.attrs['required'] = True
            else:
                for field in self.required:
                    self.fields[field].widget.attrs['required'] = True

        if self.readonly:
            if self.readonly == 'all':
                for x in self.fields:
                    self.fields[x].widget.attrs['readonly'] = True
            else:
                for field in self.readonly:
                    self.fields[field].widget.attrs['readonly'] = True

        if self.disabled:
            if self.disabled == 'all':
                for x in self.fields:
                    self.fields[x].widget.attrs['disabled'] = True
            else:
                for field in self.disabled:
                    self.fields[field].widget.attrs['disabled'] = True
