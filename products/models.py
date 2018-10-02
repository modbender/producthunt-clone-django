from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50)
    url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='products/')
    product_date = models.DateTimeField(default=timezone.datetime.now())
    modified_date = models.DateTimeField(auto_now_add=True)
    desc = models.TextField()
    votes = models.IntegerField(default=1)
    voter = models.ManyToManyField(User, related_name="voting_user")
    icon = models.ImageField(upload_to='icons/')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="product_hunter")

    def __str__(self):
        return self.title

    def gdate(self):
        return self.product_date.strftime('%b %e %Y')

    def trim(self):
        if len(self.desc) > 40:
            return self.desc[:40]+"..."
        else:
            return self.desc

    def get_absolute_url(self):
        return reverse('info', kwargs={'slug': self.slug})
