from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OwnerSerializer, RenterSerializer
from .models import owner,renter,flat_details,earning,remain
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
            owner_check = owner.objects.get(phone = p)
            if owner_check.password == request.data['password']:
                res["id"] = owner_check.owner_id
                res["response"] = True
                res["message"] = "Login Successful"
            else:
                res["id"] = None
                res["response"] = False
                res["message"] = "Password Incorrect"
        except:
            res["message"] = "Not Registered"
    elif type == "renter":
        p = request.data['emailOrphone']
        try:
            renter_check = renter.objects.get(phone = p)
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
    if type == "owner":
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
    elif type == "renter":
        print(request.data['owner_referal_id'])
        serializer = RenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
    return HttpResponse('Hello world')

def addflat(request):
    return HttpResponse('ok')



def register_as_renter(request):
    return HttpResponse('Hello world')


def owner_dashboard(request):
    return HttpResponse('ok')


def renter_dashboard(request):
    return HttpResponse('ok')


def owner_flatList(request):
    return HttpResponse('ok')

def renter_flatList(request):
    return HttpResponse('ok')

def renter_list(request):
    return HttpResponse('ok')


def earning_list(request):
    return HttpResponse('ok')

def flat_details(request):
    return HttpResponse('')