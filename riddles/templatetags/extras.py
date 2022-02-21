from django import template
from saittofree import settings_local

register = template.Library()

# settings_local var
@register.simple_tag
def settings_local_var(name):
    return getattr(settings_local, name, "")