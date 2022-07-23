

from django.shortcuts import render
from rest_framework.decorators import api_view
from api.models import Api
from api.serializers import ApiSerializers
from rest_framework.response import Response
from rest_framework import status



# Create your views here.


@api_view(['GET','PUT','DELETE'])
def apidetail(self,request,pk):
    try:
        api = Api.objects.get(id=pk)
    except Api.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializers(api,many = True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ApiSerializers(api, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request == 'DELETE':
        api.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def api_list(request):
    """
    List all free sites that render free courses online.
    e.g Udemy, Edx, Coursera, Pluralsight, Udacity etc.
    """
    if request.method == 'GET':
        api = Api.objects.all()
        serializer = ApiSerializers(api, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApiSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
