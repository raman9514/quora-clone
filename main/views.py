from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self,request,*args, **kwargs):
        return redirect('question-list')
    


