from rest_framework import serializers
from .models import Profile
from crafts_followers.models import Followers
from crafts_posts.serializers import PostSerializer
from .validators import username_validator
import cloudinary

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    follower_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    posts = PostSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            following = Followers.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None
    
    def get_following_count(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated:
            return Followers.objects.filter(owner=user).count()
        return 0
    
    def get_image_url(self, obj):
        if obj.image:
            if isinstance(obj.image, str):
                return obj.image
            else:
                return cloudinary.CloudinaryImage(obj.image.name).build_url()
        else:
            return cloudinary.CloudinaryImage('default_profile_vzpmyf').build_url()
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner', 'following_id',
            'posts_count', 'follower_count', 'following_count',
            'posts', 'image_url',
        ]
        
    def get_object(self):
        obj = super().get_object()
        obj.posts = obj.owner.post_set.all()  # Retrieve user's posts
        return obj

    def validate_username(self, value):
        username_validator(value)  # Validate username using custom validator
        return value
