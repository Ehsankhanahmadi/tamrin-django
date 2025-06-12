from django.shortcuts import render, HttpResponse

def home(req):
    return HttpResponse("this is home page section blog")

def blog(req,nameblog):
    # return HttpResponse(f"this is {nameblog} blog")
    context = {"namelog":nameblog}
    return render(req,"blog/blog.html",context)