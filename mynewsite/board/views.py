import django
from django.shortcuts import redirect, render

from django.http.request import HttpRequest
from .models import Post, Mood
from .form import ContactForm, PostForm

def index(req: HttpRequest, pid=None, delete_pwd=None):
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
    if pid and delete_pwd:
        try:
            post = Post.objects.get(id=pid)
        except:
            post = None
        
        if post and post.del_pass == delete_pwd:
            post.delete()
            message = "已刪除留言"
        else:
            message = "密碼錯誤或留言不存在"    
    elif u_name != None:
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


def post_page(req: HttpRequest):
    mood = Mood.objects.all()
    if req.method == 'POST':
        post_form = PostForm(req.POST)
        if post_form.is_valid():
            post_form.save()
            message = "已儲存留言"
            return redirect('/board/list')
        else:
            message = "請檢查輸入的資料是否正確"
    else:
        post_form = PostForm()
        message = "欄位皆必填"
    
    return render(req, 'board/posting.html', locals())

def list_page(req: HttpRequest):
    posts = Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    return render(req, 'board/list.html', locals())

def contact_page(req: HttpRequest):
    form = ContactForm()

    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()  # 直接保存 ModelForm
            message = "感謝您的來信，我們會儘快回覆您！"
        else:
            message = "請檢查輸入的資料是否正確"
    
    return render(req, 'board/contact.html', locals())
