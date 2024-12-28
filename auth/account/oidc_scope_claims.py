# oidc_provider_settings.py
from django.utils.translation import gettext_lazy as _
from oidc_provider.lib.claims import ScopeClaims

class AuthMasterScopeClaims(ScopeClaims):
    # Redefine the description of the 'profile' scope
    info_profile = (
        _('Profile'),
        _('Access to your basic information. Includes names, gender, birthdate, picture and other information.'),
    )

    # Redefine the description of the 'email' scope
    info_email = (
        _('Email'),
        _('Access to your email address.'),
    )

    def scope_profile(self):
        dic = {
            'name': self.user.get_full_name(),
            # 'gender': self.user.gender,
            # Uncomment and add more claims as needed
            # 'birthdate': self.user.profile.birthdate.isoformat() if self.user.profile.birthdate else None,
            # 'picture': self.user.profile.picture.url if self.user.profile.picture else '',
        }
        return dic

    def scope_email(self):
        dic = {
            'email': self.user.email,
            # Uncomment and add more claims as needed
            # 'email_verified': self.user.profile.email_verified,
        }
        return dic
