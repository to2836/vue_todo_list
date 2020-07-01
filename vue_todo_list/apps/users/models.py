from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField( blank=True, max_length=255)
    is_member = models.BooleanField(default=False)


    def __unicode__(self):
        return self.username

#     # def get_absolute_url(self):
#     #     return reverse('users:detail', kwargs={'username': self.username})

#     # objects = UserManager() 