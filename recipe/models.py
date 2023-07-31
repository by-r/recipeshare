from django.db import models
from django.urls import reverse

def userpath(instance, filename):
    return 'user{0}/{1}'.format(instance.user.id, filename)

# Create your models here.
class Recipe(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    ingredients = models.CharField(max_length=255)
    images = models.ImageField(upload_to=userpath, height_field=None, width_field=None, blank=True, null=True)


    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.title

