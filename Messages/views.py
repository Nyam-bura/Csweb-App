from cgitb import text
from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from Messages import serializers



class MessageApiView(generics.ListAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        return Message.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ElementApiView(generics.ListAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
       id_param = self.kwargs.get('id')
       queryset = Message.objects.filter(pk=id_param)
       return queryset
   
    def message(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
   


# 
  

#     def get_Element_By_ID(self,pk):
#         message = Message.objects.get(id=pk)
#         serializer= MessageSerializer(message,many=False)
#         return Response({"message":serializer.data})
   
      
  
        
