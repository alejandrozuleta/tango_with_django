from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField, BlobField
from django.contrib.auth.models import User
from django_mongodb_engine.storage import GridFSStorage

gridfs_storage = GridFSStorage()

# Subclass EmbeddedModelField to make it wok with admin edit


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pages = ListField(EmbeddedModelField("Page"))
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.ForeignKey(User, unique=True)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.FileField(storage= gridfs_storage, upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
