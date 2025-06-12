from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    # dynamic urls => behtar ast paiin bashand te be error nakhorim
    path("<nameblog>", views.blog),
]