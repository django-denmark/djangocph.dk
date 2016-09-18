from django import template  
from django.template.defaultfilters import stringfilter
from django.utils.html import mark_safe
import markdown

register = template.Library()


@register.filter('markdownify')
@stringfilter
def markdownify(value):
    """
    Renders the given value as Markdown.
    """
    return mark_safe(markdown.markdown(value))
