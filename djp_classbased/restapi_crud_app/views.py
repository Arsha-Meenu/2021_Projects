from django.shortcuts import render
from django.http import HttpResponse

# from restapi_crud_app.models import StudentsClass
from restapi_crud_app.serializers import StudentClassSerializer

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView

from restapi_crud_app.models import StudentsClass 

# sample function for the working of the project
class sample(APIView):
    def sample(request):
        return HttpResponse('hai')


# read and create methods for all objects from the StudentsClass table in db
class studentsList(APIView):

    def get(self,request):
        data = StudentsClass.objects.all() #get all table data in django
        serializer = StudentClassSerializer(data,many = True) #serializing instances
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentClassSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



            

class studentDetails(APIView):
    print('step 1')
    
    # def get(self,request):
    #     return HttpResponse('hai')
    # def post(self,request):
    #     return HttpResponse('hello')

    def get_object(self, pk):
        print('step 2')
        try:
            return StudentsClass.objects.get(pk=pk)
            print('step 3')
        except StudentsClass.DoesNotExist:
            print('error')
            raise Http404

            # return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        print('step 4')
        data = self.get_object(pk)
        # if data.full_clean():
        #     print('oio')
        # data = StudentsClass.objects.get(pk=3)
        serializer = StudentClassSerializer(data)
        return Response(serializer.data)

        
        
        
        
    # def get(self,request,pk,format=None):
    #     try:
    #         student_details = StudentsClass.objects.get(pk=pk)

    #     except StudentsClass.DoesNotExist:
    #         return Response(status = status.HTTP_404_NOT_FOUND)
        
    #     serializer = StudentClassSerializer(student_details)
    #     return Response(serializer.data)
    

    def put(self, request,pk,  format=None):
        # try:
        #     student_details = StudentsClass.objects.get(pk=pk)

        # except StudentsClass.DoesNotExist:
        #     return Response(status = status.HTTP_404_NOT_FOUND)

        # serializer = StudentClassSerializer(student_details, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        modify = self.get_object(pk)
        # modify = StudentsClass.objects.get(pk=3)
        serializer = StudentClassSerializer(modify, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # try:
        #     student_details = StudentsClass.objects.get(pk=pk)

        # except StudentsClass.DoesNotExist:
        #     return Response(status = status.HTTP_404_NOT_FOUND)
         
        # student_details.delete() 
        # return Response('error message', 
        #                     status=status.HTTP_200_OK)

        deletedata = self.get_object(pk)
        deletedata.delete()
        return Response('successfully deleted the single object',status=status.HTTP_200_OK)


