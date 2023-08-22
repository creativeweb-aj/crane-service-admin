from django import forms
from django.core.exceptions import ValidationError
from DjangoBaseSetup.messages.messages import ValidationMessages
from apps.about.models import About, KeyPoint, OurValue, Person, WorkingDay
from apps.service.models import Service


class AboutForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        label='Title ',
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

    class Meta:
        model = About
        fields = ['title', 'description']

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


class KeyPointForm(forms.ModelForm):
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
    name = forms.CharField(
        required=False,
        label='Name ',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Name'}
        ),
        error_messages={
            'required': ValidationMessages.name_field_is_required.value
        }
    )

    class Meta:
        model = KeyPoint
        fields = ['icon', 'name']

    def clean_icon(self):
        data = self.cleaned_data
        value = data.get('icon', None)
        return value

    def clean_name(self):
        data = self.cleaned_data
        value = data.get('name', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['name'].error_messages['required'])
        return value


class OurValueForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        label='Title ',
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

    class Meta:
        model = OurValue
        fields = ['title', 'description']

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


class PersonForm(forms.ModelForm):
    name = forms.CharField(
        required=False,
        label='Name ',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Name'}
        ),
        error_messages={
            'required': ValidationMessages.name_field_is_required.value
        }
    )
    designation = forms.CharField(
        required=False,
        label='Designation',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Designation'}
        ),
        error_messages={
            'required': ValidationMessages.designation_field_is_required.value
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
        model = Person
        fields = ['name', 'designation', 'image']

    def clean_title(self):
        data = self.cleaned_data
        value = data.get('title', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['title'].error_messages['required'])
        return value

    def clean_designation(self):
        data = self.cleaned_data
        value = data.get('designation', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['designation'].error_messages['required'])
        return value

    def clean_image(self):
        data = self.cleaned_data
        value = data.get('image', None)
        return value


DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]


class WorkingDayForm(forms.ModelForm):
    day = forms.ChoiceField(
        choices=DAY_CHOICES,
        label='Select Day',
        required=False,
        initial='',
        widget=forms.Select(
            attrs={'class': "form-control form-control-solid form-control-lg"}),
        error_messages={
            'required': ValidationMessages.day_field_is_required.value
        }
    )
    start_time = forms.CharField(
        required=False,
        label='Start Time',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg timepicker", 'placeholder': 'Start Time'}
        ),
        error_messages={
            'required': ValidationMessages.start_time_field_is_required.value
        }
    )
    end_time = forms.CharField(
        required=False,
        label='End Time',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg timepicker", 'placeholder': 'End Time'}
        ),
        error_messages={
            'required': ValidationMessages.end_time_field_is_required.value,
            'max_time': ValidationMessages.max_time_is_required.value
        }
    )

    class Meta:
        model = WorkingDay
        fields = ['day', 'start_time', 'end_time']

    def clean_day(self):
        data = self.cleaned_data
        value = data.get('day', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['day'].error_messages['required'])
        return value

    def clean_start_time(self):
        data = self.cleaned_data
        value = data.get('start_time', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['start_time'].error_messages['required'])
        return value

    def clean_end_time(self):
        data = self.cleaned_data
        startTime = data.get('start_time', None)
        value = data.get('end_time', None)
        if value == "" or value is None:
            raise ValidationError(self.fields['end_time'].error_messages['required'])
        elif startTime > value:
            raise ValidationError(self.fields['end_time'].error_messages['max_time'])
        return value
