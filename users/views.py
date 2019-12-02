from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import UserRegestrationForm,UserUpdateForm,ProfileUpdateForm,LocationRegestration,UpdateLocation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.db import transaction
from django.views.generic import DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegestrationForm(request.POST)


        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}! Your account has been created, Update your profile info')

            user = form.save()
            user.save()

            return redirect('create-location')

    else:
        form = UserRegestrationForm()

    return render(request, 'users/register.html',{'form':form,})




@login_required
def UpdatedLocation(request, pk):
    obj= get_object_or_404(Location, pk=pk)
    
    form = UpdateLocation(request.POST, instance= obj)
    context= {'form': form}
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully updated your location")
        return redirect('profile')


    else:
        
        form = UpdateLocation()


    context = {
        'form':form,
    }

    return render(request,'users/location.html',context) 



class LocationUpdateView(LoginRequiredMixin, UpdateView,UserPassesTestMixin):
    model = Location
    fields = ['city','estate']

    def form_valid(self, form):
        form.instance.user= self.request.user
              
        # print(form.instance.city)
        form.save()
        return redirect('index')

    def test_func(self):
        location = self.get_object()
        if self.request.user == location.user:
            return True
        return False    




class CreateLocation(LoginRequiredMixin, CreateView,UserPassesTestMixin):
    model = Location
    fields = ('__all__')
    def form_valid(self, form):
        form.instance.account_user= self.request.user
        form.instance.profile_user= Profile.objects.get(id=self.request.user.profile.id)
        form.save()
        return redirect('index')
  



@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance = request.user.profile)


        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
        
            messages.success(request,f'Your account has been updated!')
            return redirect('create-location')


    else:
        
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    return render(request,'users/profile.html',context,)        




 




