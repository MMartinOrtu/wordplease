from rest_framework import serializers
from rest_framework.reverse import reverse

from blogs.models import Blog
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Post
        fields = ['title', 'image', 'intro', 'publication_date']


class BlogsList(serializers.ModelSerializer):
    user = serializers.CharField()
    title = serializers.CharField()
    url = serializers.HyperlinkedIdentityField(view_name='user_blog', lookup_field='username')
    number_of_posts = serializers.SerializerMethodField()

    def get_number_of_posts(self, obj):
        return Post.objects.all().filter(owner__username=obj.user).count()

    class Meta:
        model = Blog
        fields = ['user', 'title', 'url', 'number_of_posts']
