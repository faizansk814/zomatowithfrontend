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

def Update(request):
    if request.method=="PATCH":
        body=json.loads(request.body)
        id=body['id']
        for item in arr:
            if item['id']==id:
                item['available']="yes"
    else:
        return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Updated"}))

def Delete(request):
    if request.method=="DELETE":
        body=json.loads(request.body)
        id=body['id']
        for item in arr:
            if item['id']==id:
                arr.remove(item)
    else:
        return HttpResponse("Wrong route")
    return HttpResponse(json.dumps({"msg":"Deleted"}))



