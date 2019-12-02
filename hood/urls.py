"""hood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from watch import views as watch_views

from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static 

from tastypie.api import Api
from watch.admin import BusinessResource


v1_api = Api(api_name='v1')
v1_api.register(BusinessResource())
 



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/location',user_views.location,name = 'location'),
    path('api/', include(v1_api.urls)),

    path('register/',user_views.register,name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout'),
    path('profile/',user_views.profile,name = 'profile'),
    # path('location/',user_views.update_location,name = 'location'),
    path('location/new/', user_views.CreateLocation.as_view(), name='create-location'),
    path('security/new/', watch_views.SecurityCreateView.as_view(), name='create-security'),
    path('hospital/new/', watch_views.HospitalCreateView.as_view(), name='create-hospital'),
    # path('security/new/<int:pk>/',watch_views.get_security, name ='security'),


 

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'users/password_reset.html'),name = 'password_reset'),

    path('password-reset_done/',auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'),name = 'password_reset_done'),    

    path('password-reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_confirm.html'),name = 'password_reset_confirm'),    

    path('',include('watch.urls')),
    path('',include('users.urls'))


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

