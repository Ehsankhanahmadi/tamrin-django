from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import blog

# data = [
#     {
#         "name":"blog one",
#         "disc":"disc one for blog one",
#         "time":"2005/10/11"
#     },
#     {
#         "name":"blog two",
#         "disc":"disc two for blog twp",
#         "time":"2005/10/01"
#     },
#     {
#         "name":"blog three",
#         "disc":"disc thee for blog thee",
#         "time":"2005/05/11"
#     },
# ]

# using database really
data = blog.objects.all()
def home(req):
    # return HttpResponse("this is home page section blog")
    contexthome = {"data":data}
    return render(req,"blog/home.html",contexthome)

def blogp(req,nameblog):
    # return HttpResponse(f"this is {nameblog} blog")
    for blogd in data:
        if blogd.title == nameblog:
            contextd = {"namelog":blogd}
            return render(req,"blog/blog.html",contextd)
    raise Http404("this blog not found")