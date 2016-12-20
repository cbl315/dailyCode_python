from django.shortcuts import render
from django.views import generic
from .models import Comment


class IndexView(generic.ListView):
    template_name = 'Comment/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        latest_question_list = Comment.objects.all()
        return latest_question_list if len(latest_question_list) != 0 else []
