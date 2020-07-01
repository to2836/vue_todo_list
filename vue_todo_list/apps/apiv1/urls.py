from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from .views.task import TaskListCreateView, TaskDeleteUpdateView, RepositoryListCreateView
from .views.auth import LogoutView


urlpatterns = [
    #JWT 토큰을 발행할 때 사용
    path('login', obtain_jwt_token),
    url(r'^logout$', LogoutView.as_view()),
    #JWT 토큰이 유효한지 검증
    path('token/verify', verify_jwt_token),
    #JWT 토큰을 갱신할 때 사용
    path('token/refresh', refresh_jwt_token),
    
    # task api
    url(r'^task$', TaskListCreateView.as_view(), name='task_list_create'),
    url(r'^task/update$', TaskDeleteUpdateView.as_view(), name='task_update'),
    url(r'^task/remove/(?P<task_id>[0-9]+)$', TaskDeleteUpdateView.as_view(), name='task_delete'),
    
    #repository api
    url(r'^repository$', RepositoryListCreateView.as_view(), name='repository_list_create'),




    
]