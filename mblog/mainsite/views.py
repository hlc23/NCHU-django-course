import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post, Phone

def homepage(request):
    posts = Post.objects.all()
    phones = Phone.objects.all()
    now = datetime.datetime.now()
    return render(request, "index.html", locals())
    # post_list = list()
    # for c, p in enumerate(posts):
    #     post_list.append(f"No.{c}: {p}<hr>")
    #     post_list.append(f"<small>{p.body}</small><br><br>")
    # return HttpResponse(post_list)

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        now = datetime.datetime.now()
        if post != None:
            return render(request, "post.html", locals())
    except Exception as e:
        print(e)
        return redirect("/")
    
def showphone(request, name):
    try:
        phone = Phone.objects.get(name=name)
        now = datetime.datetime.now()
        if phone != None:
            return render(request, "phone.html", locals())
    except:
        return redirect("/")
