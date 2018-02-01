#-*- coding: utf-8 -*-
from django.shortcuts import render
from .models import UserMessage

# Create your views here.
#Django request 对象
def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name='sty945')
    if all_messages:
        message = all_messages[0]

    # 此处对应html中的method="post"，表示我们只处理post请求
    # if request.method == "POST":
    #     # 就是取字典里key对应value值而已。取name，取不到默认空
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #
    #     # 实例化对象
    #     user_message = UserMessage()
    #
    #     # 将html的值传入我们实例化的对象.
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "ijkl"
    #
    #     # 调用save方法进行保存
    #     user_message.save()

    return render(request, 'message_form.html', {
        'my_message': message
    })