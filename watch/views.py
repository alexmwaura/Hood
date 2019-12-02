from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import DetailView,CreateView,DetailView
from users.models import Location
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def Index(request):
    location = Location.objects.all()
    security = Security.objects.all()
    hospital = Hospital.objects.all()
    business = Business.objects.all()
    
    context = {
        'location':location,
        'security':security,
        'hospital':hospital,
        'business':business
    }

    return render(request, 'watch/index.html',context)



class BusinessDetailView(DetailView):
    model = Business



class SecurityDetailView(DetailView):
    model = Security

class HospitalDetailView(DetailView):
    model = Hospital


class BusinessCreateView(CreateView):
    model = Business
    fields = ['location','title','image','details']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()   
        return redirect('index')

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.user:
            return True
        return False    



class SecurityCreateView(CreateView):
    model = Security
    fields = ('__all__')

    def form_valid(self, form):
        form.instance.user = self.request.user

        form.save()   
        return redirect('index')

    def test_func(self):
        security = self.get_object()
        if self.request.user == security.user:
            return True
        return False    






class HospitalCreateView(CreateView):
    model = Hospital
    fields = ('__all__')

    def form_valid(self, form):
        form.instance.user = self.request.user

        form.save()   
        return redirect('index')

    def test_func(self):
        hospital = self.get_object()
        if self.request.user == hospital.user:
            return True
        return False    





def search_results(request):
    if 'location' in request.GET and request.GET['location']:
        location = request.GET.get("location")
        searched_location = Business.get_location(location) 
        message = f'{location}'
        return render (request,'users/location.html',{"message":message,"location":searched_location})

    else:
        message = "You haven't searched for any name"

        return render(request,'users/location.html',{'message':message})

        


# def search_security(request):
#     if 'location' in request.GET and request.GET['location']:
#         location = request.GET.get("location")
#         searched_security = Security.get_security(location) 
#         message = f'{location}'
#         return render (request,'users/security.html',{"message":message,"security":searched_security}) 

#     else:
#         message = "You haven't searched for any security details"

#         return render(request,'users/security.html',{'message':message})