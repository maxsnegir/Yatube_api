from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly

from .filters import IsOwnerFilterBackend
from .models import Post, Group, Follow
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, \
    GroupSerializer

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user,
                        post_id=self.kwargs['post_id'])

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    http_method_names = [u'get', u'post', ]
    queryset = Follow.objects.all()
    filter_backends = [filters.SearchFilter, IsOwnerFilterBackend]
    search_fields = ['user__username', ]
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = [u'get', u'post', ]
    permission_classes = (IsAuthenticatedOrReadOnly,)
