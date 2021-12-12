import json
import re
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OwnerSerializer, RenterSerializer, FlatDetailsSerializer
from .models import owner,renter,flat_details,earning,remain
import datetime
# Create your views here.
# request -> response
# request handler
@api_view(['POST'])
def testing(request):
    print(request.data['name'])
    res = {
        "name": "Fahim",
        "id": "18101501"
    }
    return JsonResponse(res)

def login_as_renter(request):
    return HttpResponse('Hwllo')

@api_view(['POST'])
def login(request,type):
    res = {
        "id" : None,
        "response" : False,
        "message" : ""
    }
    if type== "owner":
        p = request.data['emailOrphone']
        print(p)
        try:
            owner_check = owner.objects.get(email = p)
            if owner_check.password == request.data['password']:
                
                res["id"] = owner_check.owner_id
                res["response"] = True
                res["message"] = "Login Successful"
            else:
                res["id"] = None
                res["response"] = False
                res["message"] = "Password Incorrect"
        except Exception as e:
            print(e)
            res["message"] = "Not Registered"
    elif type == "renter":
        p = request.data['emailOrphone']
        try:
            renter_check = renter.objects.get(email = p)
            if renter_check.password == request.data['password']:
                res["id"] = renter_check.renter_id
                res["response"] = True
                res["message"] = "Login Successful"
            else:
                res["id"] = None
                res["response"] = False
                res["message"] = "Password Incorrect"
        except:
            res["message"] = "Not Registered"
    return JsonResponse(res)


@api_view(['POST'])
def register(request,type):
    res = {
        "id" : None,
        "response" : False,
        "message" : ""
    }
    if type == "owner":
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            owner_check = owner.objects.get(phone = request.data['phone'])
            owner_check.referal_id = owner_check.name+str(owner_check.owner_id)
            owner_check.save() 
            res["response"] = True
            res["message"] = "Registration Successful"
        else:
            res["response"] = False
            res["message"] = "Registration Unsuccessful"
            print(serializer.errors)
    elif type == "renter":
        serializer = RenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res["response"] = True
            res["message"] = "Registration Successful"
        else:
            res["response"] = False
            res["message"] = "Registration Unsuccessful"
            print(serializer.errors)
    return JsonResponse(res)

def addflat(request):
    return HttpResponse('ok')



def register_as_renter(request):
    return HttpResponse('Hello world')


def owner_dashboard(request):
    return HttpResponse('ok')


def renter_dashboard(request):
    return HttpResponse('ok')

@api_view(['POST'])
def owner_flatList(request):
    print(request.data['id'])
    owner_id = request.data['id']
    print(owner_id)
    flats = flat_details.objects.filter(flat_owner_id=owner_id)
    #print(len(flats))
    res = {
        "flats": flats
    }
    print(res)
    serializer = FlatDetailsSerializer(flats,many=True)
    print(serializer.data)
    return JsonResponse(serializer.data,safe=False)

def renter_flatList(request):
    return HttpResponse('ok')

@api_view(['POST'])
def renter_list(request):
    id = request.data['id']
    # flats = flat_details.objects.filter(flat_owner_id=id)
    flats = flat_details.objects.filter(flat_owner_id = id)
    idList = []
    for flat in flats:
        idList.append(flat.flat_renter_id.renter_id)
    renterInstances = []
    for i in idList:
        renterInstances.append(renter.objects.get(renter_id=i))
    # renters = renter.objects.filter(renter_id=flats.flat_renter_id)
    serializer = []
    # print(RenterSerializer(renterInstances[0],many=False).data)
    for each_renter in renterInstances:
        # print(RenterSerializer(each_renter, many= False).data)
        serializer.append(RenterSerializer(each_renter, many= False).data)
    return JsonResponse(serializer,safe=False)

@api_view(['GET'])
def earning_and_remain(request):
    id = request.data['id']
    month = request.data['month']
    earnings = earning.objects.filter(owner_id=id,earning_month=month)
    res = []
    for eachEarning in earnings:
        flat = flat_details.objects.get(flat_id=eachEarning.flat_id.flat_id)
        _remain = remain.objects.filter(remain_month=month)
        r = {
                "flat_id": eachEarning.flat_id.flat_id,
                "earning_id": eachEarning.earning_id,
                "flat_number": flat.flat_number,
                "rent_amount" : flat.rent_amount,
                "earning": eachEarning.earned_amount,
            }
        for eachRemain in _remain:
            year = datetime.date.today().strftime("%Y")
            if eachRemain.get_year() == int(year):
                r["remain"] = eachRemain.remained_amount
                r["remain_id"] = eachRemain.remaining_id
        res.append(r)
    print(res)
    return JsonResponse(res,safe=False)

def add_earning(request):
    id = request.data['id']
    month = request.data['month']
    flat_number = request.data['flat_number']
    flat = flat_details.objects.get(flat_owner_id=owner.object.get(owner_id = id),flat_number = flat_number)
    


def flatDetails(request):
    return HttpResponse('')