from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Testnet, TestnetUserInfo
from .models import Notifications, UserInfo, CheckList
# from .forms import CommentForm
from django.template import loader
from django.views.generic.base import TemplateView

class TestnetList(generic.ListView):
    model = Testnet



    context_object_name = 'all_testnet'
    queryset = Testnet.objects.order_by("-created_on").all()
    # queryset = Post.objects.filter(status=1,comments__body__contains="fvsgfdgffd").order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        #context['comment_count'] = Comment.objects.all()
        context['all_testnet'] = Testnet.objects.all()
        # import pdb;pdb.set_trace()
        
        # context['post_count'] = Post.objects.all().count()
        return context

        