from rest_framework import serializers
from .models import Movie
# Create your views here.

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
    

# def function(value):
#     if len(value) >= 10:
#         raise serializers.ValidationError('Title must be less than 10 characters')
#     return value

# class MovieSerializer(serializers.Serializer):

#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     # title = serializers.CharField(required=False, allow_blank=True, max_length=100, validators=[function])
#     desc = serializers.CharField(required=False, allow_blank=True, max_length=200)
#     isActive = serializers.BooleanField(required=False, default=False)

#     def validate_title(self, value):
#         if len(value) <= 2:
#             raise serializers.ValidationError('Title must be more than 2 characters')
#         return value
    
#     def validate(self, data):
#         if data['title'] == data['desc']:
#             raise serializers.ValidationError('Title and description must be different')
#         return data

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.desc = validated_data.get('desc', instance.desc)
#         instance.isActive = validated_data.get('isActive', instance.isActive)
#         instance.save()
#         return instance