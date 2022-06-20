from rest_framework import serializers

from ..models import WatchList, StreamingPlatform, Review

class WatchlistSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['watchlist']
        

class StreamingPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = StreamingPlatform
        fields = "__all__"

# # MODEL SERIALIZER
# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()    # custom field method name
#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ['name', 'description']
#         # exclude = ['id', 'is_active']
    
#     # CUSTOME FIELD
        
#     def get_len_name(self, movie):
#         return len(movie.name)
        
#     # OBJECT LEVEL VALIDATOR
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 'Name and description should be different')
#         else:
#             return data

#     # FIELD LEVEL VALIDATION
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value

# EXTERNAL VALIDATION

# def validate_length(value):
#     if len(value) < 3:
#         raise serializers.ValidationError('Name is too short')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     # name = serializers.CharField(validators=[validate_length])
#     name = serializers.CharField()
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get(
#             "description", instance.description)
#         instance.is_active = validated_data.get(
#             "is_active", instance.is_active)
#         instance.save()
#         return instance

#     # OBJECT LEVEL VALIDATOR
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 'Name and description should be different')
#         else:
#             return data

#     # FIELD LEVEL VALIDATION
#     def validate_name(self, value):
#         if len(value) < 3:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value
