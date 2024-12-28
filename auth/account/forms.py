# account/forms.py

# 📦 Import modules and classes, and additional utilities
from django import forms
from oidc_provider.models import Client
import uuid, secrets

# Form for creating and updating Client instances. 
class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    # Save method overridden to generate client_id and client_secret if not provided.
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.client_id:
            instance.client_id = str(uuid.uuid4()).replace('-', '')
        if not instance.client_secret:
            instance.client_secret = secrets.token_urlsafe(64).replace('_', '').replace('-', '')
        if commit:
            instance.save()
        return instance
