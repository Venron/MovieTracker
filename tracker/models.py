from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings

class Track(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=False) # so one user can have multiple tracks
    title = models.CharField(max_length=500)
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)
    started = models.DateTimeField()

    def get_absolute_url(self):
        return reverse("tracker:index")

    def __str__(self):
        return "Owner: " + self.user.username + ", Title: " + self.title


