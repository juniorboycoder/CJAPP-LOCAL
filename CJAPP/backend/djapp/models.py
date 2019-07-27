# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.

from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.contenttypes.models import ContentType

from django.db.models.signals import post_save

class UserProfile(models.Model):
        user = models.ForeignKey(User,related_name='userprofiled', on_delete=models.SET_NULL, null=True)
        notes = models.CharField(max_length=100, default='')
        career_interests = models.CharField(max_length=100, default='')
        phone = models.IntegerField(default=0)
        image = models.FileField()
        def __str__(self):
            return self.user.username

        def get_absolute_url(self):
            return reverse('djapp:image-update', kwargs={'pk': self.pk})

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])




post_save.connect(create_profile, sender=User)



class UserNotes(models.Model):
        user = models.ForeignKey(User,related_name='usernotes', on_delete=models.SET_NULL, null=True )
        notes = models.TextField()
           
    
        
        def __str__(self):
            return self.user.username

        

def create_profilenotes(sender, **kwargs):
    if kwargs['created']:
        user_notes= UserNotes.objects.create(user=kwargs['instance'])




post_save.connect(create_profilenotes, sender=User)

class carpentry(models.Model):
    """
    Model to hold data about articles
    """
    title = models.CharField(max_length=500)
    
    
    imagedailyupdate = models.FileField()
    latestcarpentryupdate = models.TextField()
    user = models.CharField(max_length=40)
    linktofurtherreading=models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('djapp:questiondetail', kwargs={'pk': self.id})

    

   
    


class tailoring(models.Model):
    """
    Model to hold data about articles
    """
    title = models.CharField(max_length=500)
    
    
    imagedailyupdate = models.FileField()
    latesttailoringupdate = models.TextField()
    linktofurtherreading=models.TextField()
    user = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('djapp:questiondetail2', kwargs={'pk': self.id})





class commenting(models.Model):

    
    posting= models.ForeignKey(carpentry,related_name='commention',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=40)
    email= models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved  = models.BooleanField(default= False)
    user =  models.CharField(max_length=40)
    def approved(self):
      self.approved= True
      self.save()    

    def __str__(self):
        return self.body


class tailorcommenting(models.Model):

    
    posting= models.ForeignKey(tailoring,related_name='commention',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=40)
    email= models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved  = models.BooleanField(default= False)
    user =  models.CharField(max_length=40)
    def approved(self):
      self.approved= True
      self.save()    

    def __str__(self):
        return self.body



