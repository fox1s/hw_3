from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserModel
from users.serializers import UserSerializer


class ListCreateView(APIView):
    def get(self, *args, **kwargs):
        # qs = UserModel.objects.all()
        # users = UserSerializer(qs, many=True).data
        # print('ssssssssss')
        # return Response(users, status.HTTP_200_OK)

        qs = UserModel.objects.all()
        name = self.request.query_params.get('name')
        print(name)

        if name:
            qs = qs.filter(name__iexact=name)
        users = UserSerializer(qs, many=True).data
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        data = UserSerializer(instance).data
        return Response(data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(instance, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    @staticmethod
    def delete(*args, **kwargs):
        pk = kwargs.get('pk')
        instance = get_object_or_404(UserModel, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
