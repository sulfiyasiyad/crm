from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
  
    path('home',views.home,name='home'),
    path('view_Archeive',views.view_Archeive,name='view_Archeive'),

    
]