from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class RestaurantPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 10

class RestaurantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
