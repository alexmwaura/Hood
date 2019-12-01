from django.urls import path
from watch import views

urlpatterns = [
    path('', views.Index, name='index'),
    path (r'^search/',views.search_results,name= 'search_results'),

   
   
    path('create/', views.BusinessCreateView.as_view(), name='create_post'),
]


