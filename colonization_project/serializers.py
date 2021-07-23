from rest_framework import serializers

from colonization_project.models import Company, Fruits, User, UserProfile, Vegetable


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'




class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):

    user = UserSerializer()


    class Meta:
        model = Company
        fields = '__all__'
