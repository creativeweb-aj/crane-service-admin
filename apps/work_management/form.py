from django import forms
from django.core.exceptions import ValidationError
from apps.users.models import User
from apps.work_management.models import Staff, Customer, Work


class StaffForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(user_role_id=2, is_staff=False, is_active=True, is_delete=False).order_by(
            'first_name'),
        required=False,
        label='User',
        widget=forms.Select(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Select a User'}
        )
    )
    staff_type = forms.ChoiceField(
        choices=Staff.STAFF_TYPE_CHOICES,
        required=False,
        label='Staff Type',
        widget=forms.Select(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Select a Staff Type'}
        )
    )
    salary = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Salary',
        widget=forms.NumberInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Salary'}
        )
    )

    class Meta:
        model = Staff
        fields = ['user', 'staff_type', 'salary']

    def clean_user(self):
        user = self.cleaned_data.get('user')
        if user is None:
            raise ValidationError("This field is required.")
        return user

    def clean_staff_type(self):
        staff_type = self.cleaned_data.get('staff_type')
        if not staff_type:
            raise ValidationError("This field is required.")
        return staff_type

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is None:  # Assuming salary can be optional; adjust validation as needed
            raise ValidationError("This field is required.")
        return salary


class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField(
        required=False,
        label='Customer Name',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Customer Name'}
        ),
        error_messages={
            'required': "Customer name is required"
        }
    )
    customer_email = forms.EmailField(
        required=False,
        label='Email Address',
        initial='',
        widget=forms.EmailInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Email Address'}
        ),
        error_messages={
            'required': "Customer email is required"
        }
    )
    customer_mobile = forms.CharField(
        required=False,
        label='Mobile Number',
        initial='',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Mobile Number'}
        ),
        error_messages={
            'required': "Customer mobile number is required"
        }
    )
    customer_address = forms.CharField(
        required=False,
        label='Address',
        initial='',
        widget=forms.Textarea(
            attrs={'class': "form-control form-control-solid form-control-lg", 'rows': 3, 'placeholder': 'Address'}
        ),
        error_messages={
            'required': "Customer address is required"
        }
    )

    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email', 'customer_mobile', 'customer_address']

    def clean_customer_name(self):
        data = self.cleaned_data['customer_name']
        if not data:
            raise ValidationError(self.fields['customer_name'].error_messages['required'])
        return data

    def clean_customer_email(self):
        data = self.cleaned_data['customer_email']
        if not data:
            raise ValidationError(self.fields['customer_email'].error_messages['required'])
        return data

    def clean_customer_mobile(self):
        data = self.cleaned_data['customer_mobile']
        if not data:
            raise ValidationError(self.fields['customer_mobile'].error_messages['required'])
        return data

    def clean_customer_address(self):
        data = self.cleaned_data['customer_address']
        if not data:
            raise ValidationError(self.fields['customer_address'].error_messages['required'])
        return data


class WorkForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.filter(is_active=True, is_delete=False),
        required=False,
        label='Customer',
        widget=forms.Select(
            attrs={'class': "form-control form-control-solid form-control-lg"}
        ),
        error_messages={
            'required': "Customer field is required"
        }
    )
    work_title = forms.CharField(
        required=False,
        label='Work Title',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Work Title'}
        ),
        error_messages={
            'required': "Work title field is required"
        }
    )
    work_detail = forms.CharField(
        required=False,
        label='Work Detail',
        widget=forms.Textarea(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Work Detail', 'rows': 3}
        ),
        error_messages={
            'required': "Work detail field is required"
        }
    )
    work_location = forms.CharField(
        required=False,
        label='Work Location',
        widget=forms.TextInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Work Location'}
        ),
        error_messages={
            'required': "Work location field is required"
        }
    )
    start_date_time = forms.DateTimeField(
        required=False,
        label='Start Date and Time',
        widget=forms.DateTimeInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'YYYY-MM-DD HH:MM',
                   'type': 'datetime-local'},
            format='%Y-%m-%d %H:%M'
        ),
        error_messages={
            'required': "Start date time field is required"
        }
    )
    end_date_time = forms.DateTimeField(
        required=False,
        label='End Date and Time',
        widget=forms.DateTimeInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'YYYY-MM-DD HH:MM',
                   'type': 'datetime-local'},
            format='%Y-%m-%d %H:%M'
        ),
        error_messages={
            'required': "End date time field is required"
        }
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Amount',
        widget=forms.NumberInput(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Amount'}
        ),
        error_messages={
            'required': "Amount field is required"
        }
    )
    note = forms.CharField(
        required=False,
        label='Note',
        widget=forms.Textarea(
            attrs={'class': "form-control form-control-solid form-control-lg", 'placeholder': 'Note', 'rows': 3}
        ),
        error_messages={
            'required': "Note field is required"
        }
    )
    drivers = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.filter(staff_type='driver', is_active=True, is_delete=False),
        required=False,
        label='Drivers',
        widget=forms.SelectMultiple(
            attrs={'class': "form-control form-control-solid form-control-lg"}
        ),
        error_messages={
            'required': "At least one driver is required"
        }
    )
    helpers = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.filter(staff_type='helper', is_active=True, is_delete=False),
        required=False,
        label='Helpers',
        widget=forms.SelectMultiple(
            attrs={'class': "form-control form-control-solid form-control-lg"}
        ),
        error_messages={
            'required': "At least one helper is required"
        }
    )

    class Meta:
        model = Work
        fields = ['customer', 'work_title', 'work_detail', 'work_location', 'start_date_time', 'end_date_time',
                  'amount', 'note', 'drivers', 'helpers']

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        # Setting the input format for datetime fields
        self.fields['start_date_time'].input_formats = ('%Y-%m-%d %H:%M',)
        self.fields['end_date_time'].input_formats = ('%Y-%m-%d %H:%M',)

    def clean_customer(self):
        data = self.cleaned_data['customer']
        if not data:
            raise ValidationError(self.fields['customer'].error_messages['required'])
        return data

    def clean_work_title(self):
        data = self.cleaned_data['work_title']
        if not data:
            raise ValidationError(self.fields['work_title'].error_messages['required'])
        return data

    def clean_work_detail(self):
        data = self.cleaned_data['work_detail']
        if not data:
            raise ValidationError(self.fields['work_detail'].error_messages['required'])
        return data

    def clean_work_location(self):
        data = self.cleaned_data['work_location']
        if not data:
            raise ValidationError(self.fields['work_location'].error_messages['required'])
        return data

    def clean_start_date_time(self):
        data = self.cleaned_data['start_date_time']
        if not data:
            raise ValidationError(self.fields['start_date_time'].error_messages['required'])
        return data

    def clean_end_date_time(self):
        data = self.cleaned_data['end_date_time']
        if not data:
            raise ValidationError(self.fields['end_date_time'].error_messages['required'])
        return data

    def clean_amount(self):
        data = self.cleaned_data['amount']
        if not data:
            raise ValidationError(self.fields['amount'].error_messages['required'])
        return data

    def clean_note(self):
        data = self.cleaned_data['note']
        # if not data:
        #     raise ValidationError(self.fields['note'].error_messages['required'])
        return data
