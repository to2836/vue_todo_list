from django.db import models
from users.models import User

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class SubTask(models.Model):
    name = models.CharField(max_length=255)
    task = models.ForeignKey(Task, blank=True, null=True, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


    

    


    
