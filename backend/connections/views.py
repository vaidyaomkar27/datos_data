from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class DataSourceApiView(APIView):
    def get(self,request):
        return Response(
            data="Get method worked"
        )

    def post(self, request):
        return Response(
            data="Post method worked"
        )