from django.urls import path
from django.shortcuts import redirect

from .views import (IndexViews,
                    CreatePostViews,
                    PostItemViews,
                    EditPostViews,
                    DeletePostViews,
                    RespondViews,
                    ResponsesViews,
                    response_accept,
                    response_delete)

urlpatterns = [
    path('index', IndexViews.as_view(), name='index'),
    path('post/<int:pk>', PostItemViews.as_view()),
    path('create_post', CreatePostViews.as_view(), name='create_post'),
    path('post/<int:pk>/edit', EditPostViews.as_view()),
    path('post/<int:pk>/delete', DeletePostViews.as_view()),
    path('responses', ResponsesViews.as_view(), name='responses'),
    path('responses/<int:pk>', ResponsesViews.as_view(), name='responses'),
    path('respond/<int:pk>', RespondViews.as_view(), name='respond'),
    path('respond/accept/<int:pk>', response_accept),
    path('respond/delete/<int:pk>', response_delete),
    path('', lambda request: redirect('index', permanent=False)),
]