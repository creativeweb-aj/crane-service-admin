from django import forms
from django.core.exceptions import ValidationError
from DjangoBaseSetup.messages.messages import ValidationMessages
from apps.project.models import Crane, Project


class CraneForm(forms.ModelForm):
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
            'required': ValidationMessages.email_body_field_is_required.value
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

    class Meta:
        model = Crane
        fields = ['image', 'name', 'description']

    def clean_name(self):
        data = self.cleaned_data
        name = data.get('name')
        if name == "" or name is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return name

    def clean_description(self):
        data = self.cleaned_data
        value = data.get('description')
        if value == "" or value is None:
            raise ValidationError(self.fields['description'].error_messages['required'])
        return value

    def clean_image(self):
        data = self.cleaned_data
        value = data.get('image', None)
        # if value == "" or value is None:
        #     raise ValidationError(self.fields['image'].error_messages['required'])
        return value


class ProjectForm(forms.ModelForm):
    crane = forms.ModelChoiceField(
        queryset=Crane.objects.filter(is_delete=False),
        label='Crane',
        empty_label='Select Crane',
        required=False,
        initial='',
        widget=forms.Select(attrs={'class': "form-control form-control-solid form-control-lg"}),
        error_messages={
            'required': ValidationMessages.crane_field_is_required.value,
            'not_exist': ValidationMessages.crane_not_found.value
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
    title = forms.CharField(
        required=False,
        label='Title',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Title'}
        ),
        error_messages={
            'required': ValidationMessages.title_field_is_required.value
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
    address = forms.CharField(
        required=False,
        label='Address',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Address'}
        ),
        error_messages={
            'required': ValidationMessages.address_field_is_required.value
        }
    )

    class Meta:
        model = Project
        fields = ['crane', 'image', 'title', 'description', 'address']

    def clean_crane(self):
        data = self.cleaned_data
        value = data.get('crane', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['crane'].error_messages['required'])
        return value

    def clean_image(self):
        data = self.cleaned_data
        value = data.get('image', None)
        # if value == "" or value is None:
        #     raise ValidationError(self.fields['image'].error_messages['required'])
        return value

    def clean_title(self):
        data = self.cleaned_data
        value = data.get('title', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['title'].error_messages['required'])
        return value

    def clean_description(self):
        data = self.cleaned_data
        value = data.get('description', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['description'].error_messages['required'])
        return value

    def clean_address(self):
        data = self.cleaned_data
        value = data.get('address', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['address'].error_messages['required'])
        return value
