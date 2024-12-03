from pathlib import Path
from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .views_functions import IsArticleCreatorMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView

from .models import Message
from .views_reporter import get_reporter
    
class MessageListView(ListView):
    template_name = 'message/list.html'
    model = Message
    context_object_name = 'messages'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Message.objects.all()
        }

class MessageDetailView(DetailView):
    template_name = 'message/detail.html'
    model = Message
    context_object_name = 'message'

class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "message/add.html"
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('message_list')

    def form_valid(self, form):
        form.instance.reporter = get_reporter(self.request.user)
        return super().form_valid(form)
    
class MessageUpdateView(IsArticleCreatorMixin, UpdateView):
    template_name = "message/edit.html"
    model = Message
    fields = '__all__'
    success_url = reverse_lazy('message_list')

class MessageDeleteView(IsArticleCreatorMixin, DeleteView):
    template_name = 'message/delete.html'
    model = Message
    success_url = reverse_lazy('message_list')