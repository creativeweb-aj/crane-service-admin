from django import forms
from django.core.exceptions import ValidationError
from DjangoBaseSetup.messages.messages import ValidationMessages
from apps.service.models import Service


class ServiceForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        label='Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Name'}
        ),
        error_messages={
            'required': ValidationMessages.name_field_is_required.value
        }
    )
    description = forms.CharField(
        required=False,
        label='Description',
        initial='',
        widget=forms.Textarea(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Description'}
        ),
        error_messages={
            'required': ValidationMessages.description_field_is_required.value
        }
    )
    image = forms.ImageField(
        required=False,
        label='Image ',
        initial='',
        widget=forms.FileInput(
            attrs={'class': "form-control form-control-solid form-control-lg",
                   "accept": "image/png, image/gif, image/jpeg,image/jpg"}),
        error_messages={
            'required': ValidationMessages.image_field_is_required.value
        }
    )
    icon = forms.ImageField(
        required=False,
        label='Icon ',
        initial='',
        widget=forms.FileInput(
            attrs={'class': "form-control form-control-solid form-control-lg",
                   "accept": "image/png, image/gif, image/jpeg,image/jpg"}),
        error_messages={
            'required': ValidationMessages.icon_field_is_required.value
        }
    )

    class Meta:
        model = Service
        fields = ['name', 'description', 'image', 'icon']

    def clean_name(self):
        data = self.cleaned_data
        value = data.get('name', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return value

    def clean_description(self):
        data = self.cleaned_data
        value = data.get('description', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['description'].error_messages['required'])
        return value

    def clean_image(self):
        data = self.cleaned_data
        value = data.get('image', None)
        return value

    def clean_icon(self):
        data = self.cleaned_data
        value = data.get('icon', None)
        return value

