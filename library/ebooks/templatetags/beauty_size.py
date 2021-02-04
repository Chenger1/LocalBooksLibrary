from django import template


register = template.Library()


@register.filter(name='round_size')
def round_size(size: int) -> int:
    return round(size, 2)
