from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# # Create your models here.
class Location(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    city = models.CharField(max_length=60)
    estate = models.CharField(max_length=60)

    def __str__(self):
        return self.city

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,pk):
        cls.objects.filter(pk=pk).delete()


    def get_absolute_url(self):
        return reverse('index',kwargs={'city':self.city})

       










class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'download.png', upload_to ='profile_pics/')


 
@receiver(post_save,sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    
    instance.profile.save()        