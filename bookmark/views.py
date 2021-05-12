from django.shortcuts import render

# Create your views here.
# List

# 클래스(제네릭 뷰 )  뷰, 함수형 뷰
# 웹페이지에 접속한다 -> 페이지를 본다
# URL 입력 -> 웹 서버가 뷰를 찾아서 동작 시킨다.  -> 응답을 한다.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic.detail import DetailView

from django.urls import  reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    #라우팅테이블이 불러오기 전에 이뤄지기 때문에 클래스에서는 lazy를 씀