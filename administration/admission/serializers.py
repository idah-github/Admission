from dataclasses import fields
from email.mime import application
from pyexpat import model
from colorama import Style
from django. contrib.auth.models import User, Group
from rest_framework import serializers
from admission.models import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = CustomUser
        fields = [ 'id', 'email','username','first_name','middle_name','last_name',]
    
    def get_isAdmin(self, obj):
        return obj.is_staff 

    def get_username(self,obj):
        name=str(obj.first_name) + str(obj.last_name)
        if name == '':
            name = obj.email

        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    # user_type = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'middle_name', 'last_name', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        exclude = ('user', 'Application_Status', 'message')

    def bulk_create(self, request):
        data = request.data
        application=Application()
        application.title = data['title']
        application.surname = data['surname']
        application.email = CustomUser.objects.get(name=data['email'])
        application.phone_no = data['phone_number']
        application.date_of_birth = data['date_of_birth']
        application.id_number = data['id_number']
        application.address = data['address']
        application.postal_code = data['postal_code']
        application.city = data['city']
        application.country = data['country']
        application.nationality = data['nationality']
        application.course = data['course']
        application.campus = data['campus']
        application.cohort= data['cohort']
        application.birth_certificate = data['birth_certificate']
        application.leaving_certificate = data['leaving_certificate']
        application.message = data['message'] 

        return application

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"   

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['name', 'age', 'course', 'date_joined']

  
