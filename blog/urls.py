from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("add", views.addblog),
    # dynamic urls => behtar ast paiin bashand te be error nakhorim
    path("<nameblog>", views.blogp),
]