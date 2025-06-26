from django.shortcuts import render, HttpResponse, redirect
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
    # GET all and one
    # data = blog.objects.all() 
    # onedata = blog.objects.get(title=nameblog)
    # POST
    # blog.objects.create(title="test",desc="test desc",time='11:22:10')
    # PUT
    # blog.objects.update(id=1)
    # DELETE 
    # blog.objects.delete(id=3)
    for blogd in data:
        if blogd.title == nameblog:
            contextd = {"namelog":blogd}
            return render(req,"blog/blog.html",contextd)
    raise Http404("this blog not found")

def addblog(req):
    title = req.GET.get("title")
    desc = req.GET.get("desc")
    time = req.GET.get("time")
    if title and desc and time:
        blog.objects.create(title=title,desc=desc,time=time)
        return redirect("/blog")
    return render(req,"blog/addblog.html") 