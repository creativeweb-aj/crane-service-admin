from django import forms
from django.core.exceptions import ValidationError
from apps.users.models import User
from apps.work_management.models import Staff, Customer


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
