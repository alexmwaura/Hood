from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from users.models import Location


class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    location = models.ForeignKey(Location,on_delete=models.CASCADE)   

    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to = 'media/images')
    date_posted = models.DateField(auto_now=True)
    details = models.TextField()


    def __str__(self):
        return self.title

    def save_business(self):
        self.save()

    def delete_business(self,pk):
        self.objects.filter(pk = pk).delete()

    def get_absolute_url(self):
        return reverse('index',kwargs={'date_posted':self.date_posted})

    @classmethod
    def get_location(cls,location):
        business = cls.objects.filter(location__city__icontains = location)
        return business


class Security(models.Model):
    station_name = models.CharField(max_length = 60)
    station_details = models.TextField(max_length=100)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media/images')


    def __str__(self):
        return self.station_name

    class Meta:
        ordering = ['station_name']

    def save_security(self):
        self.save()     

    @classmethod
    def get_security(cls,location):
        security = cls.objects.filter(location__city__icontains = location)
        return security     
        
              

class Hospital(models.Model):
    hospital_name = models.CharField(max_length = 60)
    hospital_details = models.TextField(max_length=100)

    location = models.ForeignKey(Location,on_delete=models.CASCADE,default =True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default =True)
    image = models.ImageField(upload_to = 'media/images')


    def __str__(self):
        return self.hospital_name

    class Meta:
        ordering = ['hospital_name']

    def save_hospital(self):
        self.save() 

    @classmethod
    def get_location(cls,location):
        hospital = cls.objects.filter(location__city__icontains = location)
        return Hospital