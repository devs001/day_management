from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    """a topic user is writen about"""
    """conecting loginform to topic model"""
    txt = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owns_it = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.txt



class Entry(models.Model):
    topic = models.ForeignKey(Topic, models.CASCADE)
    txt = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    #null-True dont
    image = models.ImageField(blank=True,default='billy-huynh-W8KTS-mhFUE-unsplash.jpg')

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.txt[:50]+'...'

