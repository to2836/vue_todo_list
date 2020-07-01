
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from rest_framework.response import Response

class LogoutView(View):
    def post(self, request, *args, **kwargs):
        print(self.request.user.is_authenticated)
        if self.request.user.is_authenticated:
            logout(request)
            return Response({'detail':'로그아웃 되었습니다'}, status=200)
        else:
            return Response({'detail':'로그인되어 있지 않습니다'}, status=200)