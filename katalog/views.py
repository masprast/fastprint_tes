# from django.shortcuts import render
# from typing import Any
from django.http import HttpResponse, HttpRequest
# from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Produk
from .serializer import ProdukSerializer

# Create your views here.
# class JSONRespon(HttpResponse):
#     def __init__(self, data, **kwargs: Any):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONRespon,self).__init__(content, **kwargs)


# def daftar_produk(req:HttpRequest):
#     if req.method == 'GET':
#         produk = Produk.objects.all()
#         serializer = ProdukSerializer(produk, many=True)
#         return JSONRespon(serializer.data)


# class ListProduk(APIView):
#     def get(self,req:HttpResponse,format=None):
#         produk = Produk.objects.all()
#         serializer = ProdukSerializer(produk, many=True)
#         return Response(serializer.data)

class ListProduk(generics.ListAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer()