from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
# Create your views here.
arr=[]

def Create(request):
    if request.method=="POST":
        body=json.loads(request.body)
        arr.append(body)
        print(arr)
    else:
        return HttpResponse("Wrong request")
    return HttpResponse(json.dumps({"msg":"Data Posted succesfully"}))

def Get(req):
    return HttpResponse(json.dumps({"data":arr}))

