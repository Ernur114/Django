from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages

from clients.models import Client

class BasePageView(View):
    """Базовый контроллер, потом его перепишем."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Просто заглушка пока что."""
        return HttpResponse(content=f"<h1>Здарова</h1>")