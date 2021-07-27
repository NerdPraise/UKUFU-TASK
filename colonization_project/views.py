from os import stat
from django.http.response import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from operator import attrgetter, itemgetter

from rest_framework.views import APIView

from colonization_project.serializers import (
    CompanySerializer, PersonSerializer,
    FruitsSerializer, VegetableSerializer
)
from colonization_project.models import (
    Company, Fruits, Person, Vegetable
)


def destructure(d, *keys):
    return [d[k] if k in d else None for k in keys]


class PersonGetAPIView(APIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self, pk):
        try:
            user = Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

        return self.serializer_class(user).data

    def get_single_user_info(self, pk):
        response = self.get_queryset(pk)

        return response

    def get_multiple_user_info(self, user_one, user_two):
        first_user = self.get_queryset(user_one)
        second_user = self.get_queryset(user_two)

        [username_o, age, address, phone] = destructure(
            first_user, ['username', 'age', 'address', 'phone'])

        # first_user_data = attrgetter(
        #     'name', 'age', 'address', 'phonenumber')(serializer_one.data)
        # second_user_data = attrgetter(
        #     'name', 'age', 'address', 'phonenumber')(serializer_two.data)

        response = {
            'user_one': ''
        }

    def post(self, *args, **kwargs):
        data = self.request.data
        user_one = data.get('user_one')
        user_two = data.get('user_two')
        if user_one and user_two:
            if user_one != user_two:
                response = self.get_multiple_user_info(user_one, user_two)
                return Response(response, status=status.HTTP_200_OK)
            return Response({'message': 'Specify different users please'}, status=status.HTTP_400_BAD_REQUEST)
        elif user_one or user_two:
            user = user_one or user_two
            response = self.get_single_user_info(user)
            return Response(response, status=status.HTTP_200_OK)


class CompanyGetAPIView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
