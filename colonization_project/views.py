from django.http.response import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.shortcuts import render

from colonization_project.serializers import (
    CompanySerializer, UserProfileSerializer, UserSerializer,
    FruitsSerializer, VegetableSerializer
)
from colonization_project.models import (
    Company, User, UserProfile, Fruits, Vegetable
)


class UserGetAPIView(ListAPIView, RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_single_user_info(self, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

        serializer = self.serializer_class(user)

        data = serializer.data
        response = {
            "username": serializer.data['username'],
            "age": "30", "fruits": [
                "banana", "apple"], "vegetables": ["beetroot", "lettuce"]}
        return response

    def get_multiple_user_info(self, **kwargs):
        first_person = kwargs['pk']
        second_person = kwargs['other_pk']

        try:
            first_user = User.objects.get(pk=first_person)
            second_user = User.objects.get(pk=second_person)

        except User.DoesNotExist:
            raise Http404

    def get_queryset(self):
        return super().get_queryset()


class CompanyGetAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
