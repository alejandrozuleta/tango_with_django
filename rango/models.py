from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pages = ListField(EmbeddedModelField("Page"))

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title