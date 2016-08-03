from rest_framework.pagination import PageNumberPagination

class MachinePagination(PageNumberPagination):
    page_size = 20
