from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth import password_validation
from django.utils.translation import gettext,gettext_lazy as _



#cusmoterregistrationform
class CustomerRegistration(UserCreationForm):
    
    first_name=forms.CharField(error_messages={'required':'Must Be Field'})
    Last_name=forms.CharField(error_messages={'required':'Must Be Field'})
    
    
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="ConfirmPassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email1=forms.CharField(required=False,label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    email2=forms.CharField(required=True,label="ConfirmEmail",widget=forms.EmailInput(attrs={'class':'form-control'}))
    
   
   
   
    class Meta:
       model=User
       fields=['username', 'first_name','Last_name','email1','email2','password1','password2']
       
       labels={'email':'Email'}
       
       
       

#cusmoterregistrationformend

class LoginFrom(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    password = forms.CharField(label=('Password'), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','divisions','districts','thana','villorroad','zipcode','phone_number']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 'divisions':forms.Select(attrs={'class':'form-control'}), 'districts':forms.TextInput(attrs={'class':'form-control'}), 'thana':forms.TextInput(attrs={'class':'form-control'}), 'villorroad':forms.TextInput(attrs={'class':'form-control'}), 'zipcode':forms.NumberInput(attrs={'class':'form-control'}),'phone_number':forms.TextInput(attrs={'class':'form-control'})}

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus': True, 'class':'form-control'}))

    new_password1 = forms.CharField(label=_('New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())


    new_password2 = forms.CharField(label=_('Confirm New Password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('New password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm new password'), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))
