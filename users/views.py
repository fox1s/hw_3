from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class UserView(APIView):
    def get(self, *args, **kwargs):
        return Response('get')

    def post(self, *args, **kwargs):
        return Response('post')

    def put(self, *args, **kwargs):
        return Response('put')

    def patch(self, *args, **kwargs):
        return Response('patch')

    def delete(self, *args, **kwargs):
        return Response('delete')
