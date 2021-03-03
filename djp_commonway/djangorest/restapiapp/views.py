from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt  
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import students
from .serializers import StudentsSerializer

@csrf_exempt
@api_view(['GET',]) 
def api_read(request):
    try:
        student_details = students.objects.all()

    except students.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentsSerializer(student_details,many=True)
        return Response(serializer.data)



@api_view(['PUT',]) 
def api_update(request,pk):
    try:
        student_details = students.objects.get(pk=pk)

    except students.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':        
        serializer = StudentsSerializer(student_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        


@api_view(['DELETE',]) 
def api_delete(request,pk):
    try:
        student_details = students.objects.get(pk=pk)

    except students.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE': 
        student_details.delete() 
        return JsonResponse({'message': 'student detail was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    # try:
    #     student_details = students.objects.all()

    # except students.DoesNotExist:
    #     return Response(status = status.HTTP_404_NOT_FOUND)

    # if request.method == 'DELETE':
    #     operation = student_details.delete()
    #     data = {}
    #     if operation:
    #         data['success'] = "delete successfull"
    #     else:
    #         data['failure'] = 'delete failure'
    #     return Response(data = data)
@api_view(['DELETE',])
def api_all_delete(request):
    try:
        student_details = students.objects.all()

    except students.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
   
    
    if request.method == 'DELETE':
        count = student_details.delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST',]) 
def api_create(request):
    

    if request.method == 'POST':
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# @csrf_exempt
# def student_list(request):
#     if request.method =='GET':
#         stud = students.objects.all()
#         serializer = StudentsSerializer(stud,many = True)
#         return JsonResponse(serializer.data, safe = False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = StudentsSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

    

