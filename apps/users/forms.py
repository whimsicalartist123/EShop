from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import SignupForm

from .models import CustomUser, CustomerModel

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'name',)

class CustomSignupForm(SignupForm):

    # Create Customer Model on User Signup.
    def custom_signup(self, request, user):
        print("Inside User Custom Signup")
        _ = CustomerModel.objects.create(user=user)
        user.save()