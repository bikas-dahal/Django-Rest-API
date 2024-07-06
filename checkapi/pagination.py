from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'records'
    page_query_param = 'p'
    max_page_size = 10
    last_page_string = 'end'
    
    
class MyPaginationLimit(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10
    limit_query_param = 'records'
    offset_query_param = 'offset'
    
    
class MyPaginationCursor(CursorPagination):
    page_size = 3
    ordering = '-name'
    curser_query_param = 'cursor'
    
    
    