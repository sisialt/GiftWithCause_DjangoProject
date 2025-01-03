from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from GiftWithCause_DjangoProject.accounts.forms import AppUserCreationForm, AppUserChangeForm
from GiftWithCause_DjangoProject.accounts.models import Profile


UserModel = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fields = ('first_name', 'last_name', 'profile_picture', 'bio')


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    model = UserModel
    add_form = AppUserCreationForm
    form = AppUserChangeForm

    list_display = ('pk', 'email', 'is_staff', 'is_superuser', 'is_creator', )
    search_fields = ('email', )
    ordering = ('pk', )

    fieldsets = (
        ('User Info', {'fields': ('email', 'password', 'is_creator')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_creator", ),
            },
        ),
    )

    inlines = [ProfileInline]
