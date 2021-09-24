from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = serializers.ImageField(required=False)
    group = serializers.PrimaryKeyRelatedField(required=False,
                                               queryset=Group.objects.all())

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author', 'pub_date', )


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True, )
    post = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username')
    following = serializers.SlugRelatedField(read_only=False,
                                             queryset=User.objects.all(),
                                             slug_field='username')

    def validate_following(self, value):
        if value == self.context.get('request').user:
            raise serializers.ValidationError('Подписка на самого себя!')
        return value

    class Meta:
        fields = ('user', 'following')
        model = Follow

        validators = [
            UniqueTogetherValidator(queryset=Follow.objects.all(),
                                    fields=('user', 'following'))]
