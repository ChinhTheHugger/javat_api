from django.urls import path
from .views import StudentView
      
urlpattern = [  
    path('basic/', StudentView.as_view())  
]  