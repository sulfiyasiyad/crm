from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('add_card',views.add_card,name='add_card'),
    path('add_card1',views.add_card1,name='add_card1'),
    path('view_card',views.view_card,name='view_card'),
    path('Archeive<int:pk>',views.Archeive,name='Archeive'),
    path('view_Archeive',views.view_Archeive,name='view_Archeive'),

    
]