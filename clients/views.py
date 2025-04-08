import logging

from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.utils import IntegrityError

from clients.models import Client

logger = logging.getLogger()

class BasePageView(View):
    """Базовый контроллер, потом его перепишем."""

    def get(self, request: HttpRequest) -> HttpResponse:
        """Просто заглушка пока что."""
        return HttpResponse(content=f"<h1>Здарова</h1>")
    
    def post(self, request: HttpRequest) -> HttpResponse:
        username = request.POST.get("username")
        email = request.POST.get("email")
        raw_password = request.POST.get("password")
        if len(raw_password) < 8:
            messages.error(request=request, message="Password is too short"
            )
            return render(request=request, template_name="reg.html")
        password = make_password(password=raw_password)
        # client = Client.objects.get(email=email, username=username)
        # if client:
        #     massage.error()
        #     return render()
        # if client:
        #     messages.info("Спасибо за регистрацию")
        # return render()
        try:
            client = Client.objects.create(
                email=email, username=username,
                password = make_password(raw_password)
            )
            messages.info(
                request=request, message="Success Registration"
            )
            return render(request=request, template_name="reg.html"
            )
        except IntegrityError as ie:
            logger.error(msg="Ошибка уникальности поля", exe_info=ie)
            messages.error(
                request=request, message="Wrong login or email"
            )
            return render(request=request, template_name="reg.html")
        except Exception as e:
            logger.error(msg="Something happend", exe_info=e)   
            messages.error(request=request, message=str(e))
            return render(request=request, template_name="reg.html")
        


        # massages.info(request=request, messages="Success Registration")
        
class RegistrationView(View):
    """"Registration controller,
    There will be only get & post methods."""

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="reg.html")
    
class LoginView(View):
    """Login Controller."""
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request=request, template_name="login.html")    
    
