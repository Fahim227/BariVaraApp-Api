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
    path('currentMonthEarning/',views.current_month_earning,name='currentMonthEarning'), 
    path('flats_by_referal/',views.flats_by_referal,name='flats_by_referal'), 
    path('request_to_rent/',views.request_to_rent,name='request_to_rent'), 
    path('renter_flats/',views.renter_flats,name='renter_flats'),
    path('renter_profile/',views.renter_profile,name='renter_profile'),
    
]