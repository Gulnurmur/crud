from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
import json


# Create your views here.

class TestAPI(APIView):

    def get(self, request):


        employes = Employee.objects.all()
        print(employes)
        data = EmployeeSerializer(employes,many=True)
        

        return Response(data.data)

    def post(self,request):

        json_data = json.loads(request.body)
        
    
        print("the post method",json_data)


        return Response({"result":True})


class UpdateApi(APIView):
    
    def put(self,request, id):

        print("theid",id) 

        my = Employee.objects.filter(id=id).last()
        
        # print("the put method",request.data)
        update = EmployeeSerializer(my,data=request.data,partial=True)

        if update.is_valid():
            update.save()

            return Response(update.data)
        
        return Response(update.errors)

    

    def delete(self,request,id):
        print("the delete method",request.data)

        return Response({"result":True})
        



