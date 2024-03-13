from django import forms
from django.core.exceptions import ValidationError
from apps.users.models import User
from apps.work_management.models import Staff


class StaffForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(user_role_id=2, is_staff=False, is_active=True, is_delete=False).order_by('first_name'),
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
