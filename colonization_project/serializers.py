from rest_framework import serializers

from colonization_project.models import Company, Fruits, Person, Vegetable


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = "__all__"


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        exclude = ("user",)


class CompanySerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = "__all__"

    def get_employee(self, company):
        employees = company.employee.all()
        employees_name = (employee.username for employee in employees)
        return employees_name


class PersonSerializer(serializers.ModelSerializer):
    fruits = serializers.SerializerMethodField()
    friends = serializers.PrimaryKeyRelatedField(queryset=Person.objects, many=True)
    vegetables = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = "__all__"

    def get_vegetables(self, person):
        user_vegetables = person.vegetables.all()
        vegetables = (vegetable.name for vegetable in user_vegetables)
        return vegetables

    def get_fruits(self, person):
        user_fruits = person.fruits.all()
        fruits = (fruit.name for fruit in user_fruits)
        return fruits
