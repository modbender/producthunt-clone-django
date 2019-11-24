from django import template
from django.contrib.auth.models import User
from accounts.models import UserInput
from products.models import Product

register = template.Library()

@register.filter
def get_votes(product):
    return UserInput.objects.filter(product=product, upvote=True).count()

@register.simple_tag
def is_voted(product, user):
    if not user.is_authenticated:
        return False
    return UserInput.objects.filter(user=user, product=product).exists()

@register.simple_tag
def get_recent_votes(product):
    return UserInput.objects.filter(product=product, upvote=True).select_related('user').order_by('-mod_at')
