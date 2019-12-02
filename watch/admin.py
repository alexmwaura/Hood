from django.contrib import admin
from .models import Business,Security,Hospital
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

# Register your models here.

admin.site.register(Business)
admin.site.register(Security)
admin.site.register(Hospital)



class BusinessResource(ModelResource):
    """
     API Facet
     """
    class Meta:
        queryset = Business.objects.all()
        resource_name = 'business'
        allowed_methods = ['post', 'get', 'patch', 'delete']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True


        