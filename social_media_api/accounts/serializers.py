from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

CustomUser = get_user_model()



# ---------Custom User Serializer ---------

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'following', 'token']
        read_only_fields = ['id', 'followers', 'following', 'token']
    
    def create(self, validated_data):
        password = validated_data.pop('password')

        # create user with proper password handling
        user = CustomUser.objects.create_user(**validated_data, password=password)

        # create toke  for the user
        token = Token.objects.create(user=user)

        # attach token to user instance for serialization
        user.token = token.key

        return user