from rest_framework import serializers
from .models import Employee


def multiple_of_thousands(value):
    print('validation by validator attr')
    if value % 1000 != 0:
        raise serializers.ValidationError("Salary should be multiple of 1000")


class EmployeeSerializers(serializers.Serializer):
    no = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    salary = serializers.FloatField(validators=[multiple_of_thousands, ])
    address = serializers.CharField(max_length=100)

    def validate_salary(self, value):
        print("Field validation")
        if value < 5000:
            raise serializers.ValidationError("Minimun salary should be 5000")
        return value

    def validate(self, data):
        print("Object validation")
        name = data.get('name')
        salary = data.get('salary')
        if name == 'shetty':
            if salary < 50000:
                raise serializers.ValidationError("Shetty's minimum salary should be 50000")
        return data

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.no = validated_data.get('no', instance.no)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.salary = validated_data.get('salary', instance.salary)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
