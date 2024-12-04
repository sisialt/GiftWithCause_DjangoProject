from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError

from GiftWithCause_DjangoProject.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2', 'is_creator')

        def clean_password1(self):
            password1 = self.cleaned_data.get("password1")
            # Add your custom password validation logic if needed
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


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )
