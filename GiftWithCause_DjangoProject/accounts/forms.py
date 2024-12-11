from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

from GiftWithCause_DjangoProject.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2', 'is_creator')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = "Confirm password"

    def clean_username(self):
        email = self.cleaned_data.get("username")
        validator = EmailValidator("Enter a valid email address.")
        validator(email)

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters.")
        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        if password2 != self.cleaned_data.get("password1"):
            raise ValidationError("Passwords do not match.")
        return password2


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': "Invalid email or password. You can try again or create a new account",
        'inactive': "This account is inactive.",
    }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
