from os import stat
from re import L
from django.http.response import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView


from rest_framework.views import APIView

from colonization_project.serializers import (
    CompanySerializer, PersonSerializer,
    FruitsSerializer, VegetableSerializer
)
from colonization_project.models import (
    Company, Fruits, Person, Vegetable
)


def destructure(d, keys):
    """Custom object destructuring """
    return [d[k] if k in d else None for k in keys]


class PersonGetAPIView(APIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self, user_id, **kwargs):
        if isinstance(user_id, list):
            return Person.objects.filter(pk__in=user_id)
        else:
            try:
                return Person.objects.get(pk=user_id)
            except Person.DoesNotExist:
                raise Http404

    def get_single_user_info(self, pk):
        response = self.get_queryset(pk)
        serialized_data = self.serializer_class(response).data

        [username, age, fruits, vegetable] = destructure(
            serialized_data, ['username', 'age', 'fruits', 'vegetables'])
        new_response = {
            'username': username,
            'age': age,
            'fruits': fruits,
            'vegetable': vegetable
        }

        return new_response

    def get_multiple_user_info(self, user_one, user_two):
        users_qs = self.get_queryset([user_one,user_two ])
        users = users_qs.annotate(friends="")
        print(users_qs)

        [username_one, age_one, address_one, phone_one] = destructure(
            users, ['username', 'age', 'address', 'phone'])

        [username_two, age_two, address_two] = destructure(user_two, ['username', 'age', 'address', 'phone'])

        response = {
            'user_one': {},
            'user_two': '',
            'common_friends': []
        }

        return response

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


class FruitsGetAPIView(APIView):
    serializer_class = FruitsSerializer
    queryset = Fruits.objects.all()

    def get(self, *args, **kwargs):
        pass 