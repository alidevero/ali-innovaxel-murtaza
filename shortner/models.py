from django.db import models
import string , random
from django.utils import timezone
# Create your models here.

def generate_shortcode():

    return ''.join(random.choices(string.ascii_letters + string.digits , k=6))


class ShortUrl(models.Model):

    url = models.URLField()
    short_url = models.CharField(max_length=10 , unique=True , default=generate_shortcode)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_url} -> {self.url}"