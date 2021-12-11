from django.urls import path
from . import views

urlpatterns = [
    path('testing/',views.testing,name='testing'),
    path('register/<str:type>/',views.register,name='registerasowner'),
    path('login/<str:type>/',views.login,name='login'),
    path('addflat/',views.addflat,name='addflat'),
    path('ownerFlatList/',views.owner_flatList,name='ownerFlatList'), 
    path('renterList/',views.renter_list,name='renterList'), 
    path('earningAndRemain/',views.earning_and_remain,name='earningAndRemain'), 
]