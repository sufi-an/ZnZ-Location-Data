from django import forms
from .models import company_master, User
from django.contrib.auth.forms import PasswordResetForm
from django.utils.translation import gettext as _


from django.contrib.auth.forms import SetPasswordForm

class MySetPasswordForm(SetPasswordForm):
    
    def save(self, *args, commit=True, **kwargs):
        user = super().save(*args, commit=False, **kwargs)
        user.is_set_new_password = True
        if commit:
            user.save()
            
        return user

class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=2000)
    BIN_number = forms.CharField(max_length=30)
    industry = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    other_employees = forms.BooleanField()

    class Meta:
    	model = company_master
    	fields = '__all__'



class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = _("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email

