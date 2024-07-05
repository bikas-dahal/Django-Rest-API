from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    def vs(value):
        if value[0] == 'z':
            raise serializers.ValidationError('No name start with z')
        return value
    
    name = serializers.CharField(validators = [vs])
    class Meta:
        model = Student
        fields = ['name',  'roll', 'city', 'grade']


    def validate(self, data):
        if data.get('name') == data['city']:
            raise serializers.ValidationError('Name and City cannot be same')
        return data
    
    def validate_roll(self, data):
        if data < 0 or data > 100:
            raise serializers.ValidationError('Out of Range')
        return data

  



# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=50)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)
#     grade = serializers.IntegerField()
#     def create(self, data):
#         return Student.objects.create(**data)
    
#     def get(self, id):
#         return Student.objects.get(id=id)
    
#     def update(self, instance, data):
#         print(instance.name)
#         instance.name = data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = data.get('roll', instance.roll)
#         instance.city = data.get('city', instance.city)
#         instance.grade = data.get('grade', instance.grade)
#         instance.save()
#         return instance
#         # return Student.objects.filter(id=id).update(**data)
    
#     def validate(self, data):
#         if data['name'] == data['city']:
#             raise serializers.ValidationError('Name and City cannot be same')
#         return data
    
#     def validate_roll(self, data):
#         if data < 0 or data > 100:
#             raise serializers.ValidationError('Out of Range')
#         return data
    