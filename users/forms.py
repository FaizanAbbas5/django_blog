from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# a new form that inherits from the user creation form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() #default required = True

    # nested namespace for configurations
    class Meta:
        # The model that will be affected (form will besaved to the User model)
        model = User
        # The field that we want in the form and their order
        fields = ['username', 'email', 'password1', 'password2']

# A model form allows us to create a form that will work with a specific database model
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #default required = True

    # nested namespace for configurations
    class Meta:
        # The model that will be affected (form will besaved to the User model)
        model = User
        # The field that we want in the form and their order
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # nested namespace for configurations
    class Meta:
        # The model that will be affected (form will besaved to the User model)
        model = Profile
        # The field that we want in the form and their order
        fields = ['image']
