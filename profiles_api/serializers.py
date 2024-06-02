from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # Define serializer
    name = serializers.CharField(max_length=10)
    # Specify fields you want to accept
