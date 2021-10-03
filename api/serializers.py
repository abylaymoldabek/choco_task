from django.contrib.auth.models import Permission, Group, User
from rest_framework.serializers import ModelSerializer

from api.models import Task


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        password=validated_data['password'],
                                        first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])
        return user


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'deadline', 'user')
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        if not validated_data.get('user'):
            validated_data.update({'user': self.context.get('request').user})
        task = Task.objects.create(**validated_data)
        return task


