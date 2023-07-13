from rest_framework.pagination import PageNumberPagination


class DoctorsListPagination(PageNumberPagination):
    page_size = 12
