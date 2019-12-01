from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.generic import DetailView,CreateView
from users.models import Location


# Create your views here.


def Index(request):
    location = Location.objects.all()

    business = Business.objects.all()

    return render(request, 'watch/index.html',{'business':business,'location':location})


class BusinessCreateView(CreateView):
    model = Business
    fields = ['title','image','details']

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


