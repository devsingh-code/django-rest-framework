from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedIdentityField(many=False,view_name ='owner-detail')
    class Meta:
        model = Post
        fields =(
            'title',
            'owner',
            'custom_id',
            'category',
            'publish_date',
            'last_updated'
        )
