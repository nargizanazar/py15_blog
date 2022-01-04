from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Post
from main.permissions import IsAuthor
from main.serializers import CategorySerializer, PostSerializer, PostListSerializer


class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        if self.action == 'list':
            serializer_class = PostListSerializer
        return serializer_class

    def get_permissions(self):
        #создавать пост может залогиненный пользователь
        if self.action == 'create':
            return [IsAuthenticated()]
        # изменять и удалять только автор
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]
        # просматривать могут все
        return []

#TODO: список категорий
#TODO: CRUD постов
#TODO: изображения в постах
#TODO: комменты
#TODO: подключить twilio
#TODO: авторизация
#TODO: избранное, лайки
