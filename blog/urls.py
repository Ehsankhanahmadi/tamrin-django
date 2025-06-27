from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("add", views.addblog),
    # dynamic urls => behtar ast paiin bashand te be error nakhorim
    # "<int:id>" => find one data ba type number int
    path("<nameblog>", views.blogp),
]