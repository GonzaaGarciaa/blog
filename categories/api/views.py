from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdmindOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdmindOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.all()
    queryset = Category.objects.filter(published = True)
    lookup_field = 'slug'