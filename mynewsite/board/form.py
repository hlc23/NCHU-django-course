from django import forms
from captcha.fields import CaptchaField
from .models import Post, Mood, Contact

class ContactForm(forms.ModelForm):
    captcha = CaptchaField(label='不是機器人')
    class Meta:
        model = Contact
        fields = ['name', 'city', 'email', 'message']
        labels = {
            'name': '姓名',
            'city': '城市',
            'email': '電子郵件',
            'message': '訊息',
        }
        widgets = {
            'message': forms.Textarea(),
        }
    
class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Post
        fields = ['nickname', 'del_pass', 'mood', 'message', 'birth_year', 'topic']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'topic': forms.TextInput(attrs={'placeholder': '請用空白鍵分隔'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].queryset = Mood.objects.all()
        self.fields['mood'].empty_label = "請選擇心情"
        self.fields['nickname'].label = "暱稱"
        self.fields['del_pass'].label = "刪除密碼"
        self.fields['birth_year'].label = "出生年份"
        self.fields['captcha'].label = "不是機器人"