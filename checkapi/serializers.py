from rest_framework import serializers

from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    
    def post(self, data):
        return Student.objects.create(**data)
    
    def get(self, id):
        return Student.objects.get(id=id)
    
    def update(self, instance, data):
        print(instance.name)
        instance.name = data.get('name', instance.name)
        print(instance.name)
        instance.roll = data.get('roll', instance.roll)
        instance.city = data.get('city', instance.city)
        instance.grade = data.get('grade', instance.grade)
        instance.save()
        return instance
        # return Student.objects.filter(id=id).update(**data)
    
    def delete(self, id):
        return Student.objects.filter(id=id).delete()
    
    
    def validate(self, data):
        if data['name'] == data['city']:
            raise serializers.ValidationError('Name and City cannot be same')
        return data
    
    def validate_roll(self, data):
        if data < 0 or data > 100:
            raise serializers.ValidationError('Out of Range')
        return data
    
    class Meta:
        model = Student
        fields = '__all__'