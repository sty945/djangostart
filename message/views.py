#-*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
#Django request 对象
def getform(request):
    return render(request, 'message_form.html')