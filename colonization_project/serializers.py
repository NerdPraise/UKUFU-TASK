from rest_framework import serializers

from colonization_project.models import Company, Fruits, Person, Vegetable


class FruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruits
        fields = '__all__'


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_employee(self, company):
        employees = company.employee.all()
        employees_id = (employee.id for employee in employees)
        return employees_id


class PersonSerializer(serializers.ModelSerializer):
    fruits = FruitsSerializer(many=True, read_only=True)
    vegetables = VegetableSerializer(many=True, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'
