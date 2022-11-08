from django import template
from django.utils.safestring import make_safe

register = template.Library()


@register.filter
def email_link(email_str):
    return make_safe(f"<a href='mailto:{email_str}'>{email_str}</a>")
