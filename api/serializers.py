from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Review

# User Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user

# Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    book = serializers.ReadOnlyField(source='book.id')

    class Meta:
        model = Review
        fields = ('id', 'book', 'user', 'rating', 'comment', 'created_at')

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'