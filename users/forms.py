from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import SignupForm

from .models import CustomUser, CustomerModel, VendorModel

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'name',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'name',)

class CustomSignupForm(SignupForm):
    user_type = forms.ChoiceField(choices=[("CUSTOMER", "Customer"), ("VENDOR", "Vendor")])

    def custom_signup(self, request, user):
        user_type = self.cleaned_data["user_type"]
        if user_type == "CUSTOMER":
            user.is_customer = True
            _ = CustomerModel.objects.create(user=user)
        else:
            user.is_customer = False
            _ = VendorModel.objects.create(user=user)
        user.save()