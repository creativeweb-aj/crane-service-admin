from django import forms
from django.core.exceptions import ValidationError
from DjangoBaseSetup.messages.messages import ValidationMessages
from apps.about.models import About, KeyPoint, OurValue, Person, WorkingDay
from apps.customers.models import Testimonial
from apps.service.models import Service


class TestimonialForm(forms.ModelForm):
    client_name = forms.CharField(
        required=False,
        label='Client Name ',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Client Name'}
        ),
        error_messages={
            'required': ValidationMessages.client_name_field_is_required.value
        }
    )
    client_image = forms.ImageField(
        required=False,
        label='Client Image ',
        initial='',
        widget=forms.FileInput(
            attrs={'class': "form-control form-control-solid form-control-lg",
                   "accept": "image/png, image/gif, image/jpeg,image/jpg"}),
        error_messages={
            'required': ValidationMessages.client_image_field_is_required.value
        }
    )
    comment = forms.CharField(
        required=False,
        label='Comment',
        initial='',
        widget=forms.Textarea(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Comment'}
        ),
        error_messages={
            'required': ValidationMessages.comment_field_is_required.value
        }
    )

    class Meta:
        model = Testimonial
        fields = ['client_name', 'client_image', 'comment']

    def clean_client_name(self):
        data = self.cleaned_data
        value = data.get('client_name', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['client_name'].error_messages['required'])
        return value

    def clean_client_image(self):
        data = self.cleaned_data
        value = data.get('client_image', None)
        return value

    def clean_comment(self):
        data = self.cleaned_data
        value = data.get('comment', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['comment'].error_messages['required'])
        return value

