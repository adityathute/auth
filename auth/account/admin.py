# account/admin.py

# 📦 Import necessary modules and classes
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, GroupAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from .models import User
from django.conf import settings
from oidc_provider.models import Client, Code, RSAKey, Token, UserConsent
from oidc_provider.admin import ClientAdmin
from .forms import ClientCreationForm

# Define a custom admin site
class MyAdminSite(AdminSite):
    # Set custom site header, title, and index title
    site_header = f"{settings.PROJECT_NAME} Admin"
    site_title = f"{settings.PROJECT_NAME} Admin Portal"
    index_title = f"Welcome to the {settings.PROJECT_NAME} Admin Portal"

# Instantiate the custom admin site
admin_site = MyAdminSite(name='custom_admin')

# Define user creation form
class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

# Define user change form
class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

# Define user admin configuration
class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    # Configure list display, filter, fieldsets, add fieldsets, search fields, and ordering
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

# Define a custom ClientAdmin
class ClientAdminOverride(ClientAdmin):
    form = ClientCreationForm
    readonly_fields = ('client_id', 'client_secret', 'date_created')

# Register models
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.register(Code)
admin_site.register(RSAKey)
admin_site.register(Token)
admin_site.register(UserConsent)
admin_site.register(Client, ClientAdminOverride)
