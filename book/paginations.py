from rest_framework.pagination import PageNumberPagination


class BookListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class OrderListPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'