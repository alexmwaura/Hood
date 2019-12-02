from django.urls import path
from watch import views

urlpatterns = [
    path('', views.Index, name='index'),
    path (r'^search/',views.search_results,name= 'search_results'),
    # path (r'^search/security',views.search_security,name= 'search_security'),



    path('business/<int:pk>/',views.BusinessDetailView.as_view(), name ='business-detail'),   
    path('security/<int:pk>/',views.SecurityDetailView.as_view(), name ='security-detail'),   
    path('hospital/<int:pk>/',views.HospitalDetailView.as_view(), name ='hospital-detail'),   
   
    path('create/', views.BusinessCreateView.as_view(), name='create_post'),
    
]


