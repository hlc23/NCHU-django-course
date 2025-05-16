import django
from django.shortcuts import render

from django.http.request import HttpRequest
from .models import Post, Mood

def index(req: HttpRequest):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()
    years = range(1900, 2026)
    
    try:
        u_name = req.GET['name']
        u_pwd = req.GET['pwd']
        u_mood = req.GET['mood']
        u_message = req.GET['message']
        u_year = req.GET['birth_year']
        u_topic = req.GET['topic'].replace(',', ' ').split(' ')
        
        for i, v in enumerate(u_topic):
            v = v.strip()
            v = '#' + v
            u_topic[i] = v

        u_topic = ' '.join(i for i in u_topic if i != '')
        
        
    except Exception as e:
        u_name = None
        message = "欄位皆必填"
        
    if u_name != None:
        mood = Mood.objects.get(status=u_mood)
        post = Post.objects.create(
            nickname=u_name,
            del_pass=u_pwd,
            mood=mood,
            message=u_message,
            birth_year=u_year,
            topic=u_topic,
        )
        post.save()
        message = "已儲存留言"
    return render(req, 'board/index.html', locals())
