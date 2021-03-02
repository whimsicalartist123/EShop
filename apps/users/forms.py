from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import SignupForm

from .models import CustomUser, CustomerModel

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', )

class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=50)

    # Create Customer Model on User Signup.
    def custom_signup(self, request, user):
        cd = self.cleaned_data
        _ = CustomerModel.objects.create(user=user, name=cd["name"])
        user.save()