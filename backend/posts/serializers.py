from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "user", "content", "created_at"]

    def get_user(self, obj):
        return {'username': obj.user.username}