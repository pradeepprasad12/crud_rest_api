from enroll.models import User
from enroll.api.serializers import UserSerializer
from rest_framework import viewsets
####authentication #######
#from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import IsAuthenticated
########
import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.authentication import JWTAuthentication

class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #authentication######
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

################################ via 3rd party api use create read update delete

#create
@csrf_exempt
def crud_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = UserSerializer(data= pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data create'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data= JSONRenderer().render(serializer.errors)

#read
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = User.objects.get(id=id)
            serializer= UserSerializer(stu)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = User.objects.all()
        serializer = UserSerializer(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
#update
    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        stu = User.objects.get(id=id)
        serializer = UserSerializer(stu,data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data updated'}
            #json_data = JSONRenderer().render(res)
            #return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(res, safe=False)
        #json_data = JSONRenderer().render(serializer.errors)
        #return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)

    #delete

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        stu = User.objects.get(id=id)
        stu.delete()
        res = {'msg': 'data deleted'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res,safe=False)
