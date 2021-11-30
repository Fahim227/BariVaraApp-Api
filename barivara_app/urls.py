from django.urls import path
from . import views

urlpatterns = [
    path('testing/',views.testing,name='testing'),
    path('register/<str:type>/',views.register,name='registerasowner'),
    path('login/<str:type>/',views.login,name='login'),
    path('addflat/',views.addflat,name='addflat'),
    
]