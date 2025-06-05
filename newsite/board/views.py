import django
from django.shortcuts import redirect, render

from django.http.request import HttpRequest
from django.contrib.sessions.models import Session
from django.contrib import messages
from .models import Post, Mood, User
from .form import ContactForm, PostForm, LoginForm

def index(req: HttpRequest, pid=None, delete_pwd=None):
    if "user_name" in req.session and req.session['user_name'] is not None:
        user_name = req.session['user_name']
        message = f"歡迎 {user_name} 回來！"
    return render(req, 'board/index.html', locals())

def login(req: HttpRequest):
    
    if req.method == 'GET':
        login_form = LoginForm()
        return render(req, 'board/login.html', locals())

    if req.method == 'POST':
        redirect_url = req.POST.get('redirect_url', None)
        login_form = LoginForm(req.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['user_name']
            user_password = login_form.cleaned_data['user_pwd']
            try:
                user = User.objects.get(name=user_name, password=user_password, enabled=True)
                req.session['user_name'] = user.name
                
                if redirect_url:
                    return redirect(redirect_url)
                
                messages.add_message(req, messages.SUCCESS, f"歡迎 {user.name} 回來！")
                return redirect('/board')
            except:
                messages.add_message(req, messages.WARNING, "使用者名稱或密碼錯誤")
                message = "使用者名稱或密碼錯誤"
                login_form = LoginForm()
        else:
            messages.add_message(req, messages.WARNING, "請檢查輸入的資料是否正確")
            message = "請檢查輸入的資料是否正確"
            login_form = LoginForm(req.POST)
    else:
        login_form = LoginForm()

    return render(req, 'board/login.html', locals())

def logout(req: HttpRequest):
    if "user_name" in req.session:
        Session.objects.filter(session_key=req.session.session_key).delete()
    return redirect('/board')

def user_info(req: HttpRequest):
    if "user_name" in req.session:
        user_name = req.session['user_name']
        try:
            user = User.objects.get(name=user_name, enabled=True)
            return render(req, 'board/userinfo.html', locals())
        except User.DoesNotExist:
            messages.add_message(req, messages.WARNING, "使用者不存在或已被停用")
    else:
        messages.add_message(req, messages.WARNING, "請先登入")
    
    return redirect('/board/login')



def post_page(req: HttpRequest):
    if "user_name" in req.session:
        user_name = req.session['user_name']

    mood = Mood.objects.all()
    if req.method == 'POST':
        post_form = PostForm(req.POST)
        if post_form.is_valid():
            # 將表單資料儲存到 session 中
            if 'posts' not in req.session:
                req.session['posts'] = []
            
            post_data = {
                'nickname': post_form.cleaned_data['nickname'],
                'message': post_form.cleaned_data['message'],
                'birth_year': post_form.cleaned_data['birth_year'],
                'pub_time': django.utils.timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            req.session['posts'].append(post_data)
            
            return redirect('/board/list')
        else:
            message = "請檢查輸入的資料是否正確"
    else:
        post_form = PostForm()
        message = "欄位皆必填"
    
    return render(req, 'board/posting.html', locals())

def list_page(req: HttpRequest):
    if "user_name" in req.session:
        user_name = req.session['user_name']
    
    
    session_posts = req.session.get('posts', [])
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
