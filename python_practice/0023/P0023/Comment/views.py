from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from .models import Comment
from django.urls import reverse
from datetime import datetime


class IndexView(generic.ListView):
    template_name = 'Comment/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        latest_question_list = Comment.objects.all()
        return latest_question_list if len(latest_question_list) != 0 else []


def CommentView(request):
    cmt = request.POST
    latest_question_list = Comment.objects.all()
    latest_question_list = latest_question_list if len(latest_question_list) != 0 else []
    c1 = Comment(name=cmt['uname'], comment=cmt['comment'], pub_date=datetime.now())
    c1.save()
    return render(request, 'Comment/index.html', {'latest_question_list': latest_question_list})
