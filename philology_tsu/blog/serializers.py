from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_date', 'user']
        extra_kwargs = {
            'user': {'read_only': True}
        }
