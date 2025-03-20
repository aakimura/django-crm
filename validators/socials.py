import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_linkedin(value):
    is_linkedin = re.search(r'(linkedin\.com\/)(in|company)\/', value)
    if not is_linkedin:
        raise ValidationError(
            _("%(value)s is not a valid LinkedIn user URL"),
            params={"value": value},
        )


def validate_twitter(value):
    is_twitter = re.search(r'^@[a-zA-Z0-9_]{1,15}$')
    if not is_twitter:
        raise ValidationError(
            _("%(value)s is not a valid Twitter (X) user URL"),
            params={"value": value},
        )


def validate_github(value):
    is_github = re.search(r'(github\.com\/)', value)
    if not is_github:
        raise ValidationError(
            _("%(value)s is not a valid GitHub user URL"),
            params={"value": value},
        )
