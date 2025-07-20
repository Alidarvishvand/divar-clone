import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    province = django_filters.CharFilter(field_name='province', lookup_expr='exact')
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Post
        fields = ['min_price', 'max_price', 'province', 'category']
