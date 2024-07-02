from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    
    def post(self, data):
        return Student.objects.create(**data)
    
    def get(self, id):
        return Student.objects.get(id=id)
    
    def put(self, id, instance):
        instance.name = data.get('name', instance.name)
        instance.roll = data.get('roll', instance.roll)
        instance.city = data.get('city', instance.city)
        instance.grade = data.get('grade', instance.grade)
        instance.save()
        # return Student.objects.filter(id=id).update(**data)
    
    def delete(self, id):
        return Student.objects.filter(id=id).delete()
    
    class Meta:
        model = Student
        fields = '__all__'