from django.shortcuts import render, HttpResponse
from django.http import Http404

# database test
data = [
    {
        "name":"blog one",
        "disc":"disc one for blog one",
        "time":"2005/10/11"
    },
    {
        "name":"blog two",
        "disc":"disc two for blog twp",
        "time":"2005/10/01"
    },
    {
        "name":"blog three",
        "disc":"disc thee for blog thee",
        "time":"2005/05/11"
    },
]

def home(req):
    # return HttpResponse("this is home page section blog")
    contexthome = {"data":data}
    return render(req,"blog/home.html",contexthome)

def blog(req,nameblog):
    # return HttpResponse(f"this is {nameblog} blog")
    for blog in data:
        if blog["name"] == nameblog:
            context = {"namelog":blog}
            return render(req,"blog/blog.html",context)
    raise Http404("this blog not found")