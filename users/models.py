from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
 #Create your models here.
#class UserProfileManager(models.Manager):


class Profile(models.Model):
    bio = models.TextField()
    website_link = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.CharField(max_length=100, null=True, blank=True)
    insta_link = models.CharField(max_length=100, null=True, blank=True)
    twitter_link = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(default='BBMjGbv.jpg', blank=True)
    user = models.OneToOneField(User,models.CASCADE)
    def __str__(self):
        return str(self.user)


'''def createProfile(sender,**kwargs):
    if kwargs['created']:
        user_profile= Profile.objects.created(user=kwargs['instance'])
        post_save.connect(createProfile,sender=User)'''
