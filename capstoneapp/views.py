from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Capstoneapp
from .serializers import CapstoneappSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from rest_framework.views import APIView
import logging




# set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
@api_view(['GET', 'POST'])
def capstoneapi_list(request):

    if request.method == 'GET':
        capstoneapp = Capstoneapp.objects.all()
        serializer = CapstoneappSerializer(capstoneapp, many=True)
        #return JsonResponse({'capstoneapp': serializer.data})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CapstoneappSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def capstoneapi_detail(request,id):

    try:
        capstoneapp = Capstoneapp.objects.get( pk = id)
    except Capstoneapp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CapstoneappSerializer(capstoneapp)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CapstoneappSerializer(capstoneapp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        capstoneapp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    




# File Save API
@csrf_exempt
def SaveFile(request):
    if request.method == 'POST':
        file = request.FILES.get['uploadedFile', None]
        if file:
            file_name = default_storage.save(file.name, file)
            return JsonResponse({'message': 'File uploaded successfully', 'filen_name': file_name}, safe=False)
        else:
            return JsonResponse({'message' : 'No File Provided'}, status=400, safe=False)
    else:
        return JsonResponse({"message" : "Invalid request method"}, status=405, safe=False)
 
    # file = request.FILES['uploadedFile']
    # file_name = default_storage.save(file.name, file)
    #return JsonResponse(file_name, safe=False)
 
def home_capstone_view(request):
    #return HttpResponse('This is a hard Capstone project!!!')
    return render(request, 'home.html')

