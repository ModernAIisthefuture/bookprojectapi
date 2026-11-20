
from django.contrib import admin
from django.urls import path, include

from books.auth_views import (
    LoginView,
    RefreshView
)


urlpatterns = [

    # Django Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Book CRUD APIs
    path(
        'api/',
        include('books.urls')
    ),

    # JWT Login
    path(
        'api/token/',
        LoginView.as_view(),
        name='token_obtain_pair'
    ),

    # JWT Refresh
    path(
        'api/token/refresh/',
        RefreshView.as_view(),
        name='token_refresh'
    ),

]
