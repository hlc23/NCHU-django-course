from django.contrib import admin

from .models import Post, Mood, Contact, User
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'enabled', 'pub_time')
    ordering = ('-pub_time',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'email', 'created_at')
    ordering = ('-created_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Mood)
admin.site.register(Contact, ContactAdmin)
admin.site.register(User)