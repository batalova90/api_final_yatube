from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import permissions
from rest_framework import filters

from posts.models import Group, Post
from .serializers import CommentSerializer, GroupSerializer
from .serializers import PostSerializer, FollowSerializer
from .permissions import AuthorSafeMethods


class MixinViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    pass


class PostViewSet(viewsets.ModelViewSet, MixinViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorSafeMethods, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet, MixinViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorSafeMethods, )

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post,
                                 id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_destroy(self, instance):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        if post is not None:
            super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(viewsets.ModelViewSet, MixinViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username', )

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
