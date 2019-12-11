from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    upvote = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    mod_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'User Inputs'

    def __str__(self):
        return self.user.username
