from django.urls import path

from clients.views import BasePageView

urlpatterns = [
    path(route="", view=BasePageView.as_view(), name="base"),
]