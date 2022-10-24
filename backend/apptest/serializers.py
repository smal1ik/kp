import email
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_staff']


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'
        
class CreateWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class OtherWorkerSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display')
    class Meta:
        model = OtherWorker
        fields = '__all__'   

class AppServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppService
        fields = ['url','name','description']

class UserSettingsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserSetting
        fields = '__all__'

class CreateUserSettingsSerializer(serializers.ModelSerializer):    
    class Meta:
        model = UserSetting
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CreatePostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class AppServiceSerializer(serializers.Serializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template': 'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
    url = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=False)
    description = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """
        Create and return a new `AppService` instance, given the validated data.
        """
        return AppService.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `AppService` instance, given the validated data.
        """
        instance.url = validated_data.get('url', instance.url)
        instance.name = validated_data.get('name', instance.name)
        instance.active = validated_data.get('active', instance.active)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance