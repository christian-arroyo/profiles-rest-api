from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # Define serializer
    name = serializers.CharField(max_length=10)
    # Specify fields you want to accept

# ModelSerializer has more functionalities than Serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        # Point serializer to our custom UserProfile
        model = models.UserProfile
        # List all fields that you want to make accessible by the serializer
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Overrides create function and calls create_user function, used to call
    # set_password so a password is generated as a hash and not plain text
    def create(self, validated_data):
        """Create and return a new user"""
        # Create and return a new user
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    # Override ModelSerializer to hash users password when updating
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
