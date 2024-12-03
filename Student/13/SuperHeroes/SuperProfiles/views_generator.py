import os
import re
from typing import Dict, Any

def sanitize_name(name: str) -> str:
   return ''.join(word.capitalize() for word in re.findall(r'\w+', name))

def generate_model(model_name: str, fields: Dict[str, str]) -> str:
    model_code = f"""from django.db import models
from django.utils import timezone
from django.urls import reverse

class {model_name}(models.Model):
    # Reporter foreign key (optional, can be removed if not needed)
    reporter = models.ForeignKey('reporter.Reporter', on_delete=models.CASCADE, related_name='{model_name.lower()}s', null=True, blank=True)
"""

    for field_name, field_type in fields.items():
        field_mapping = {
            'string': 'CharField(max_length=200)',
            'text': 'TextField()',
            'int': 'IntegerField()',
            'float': 'FloatField()',
            'boolean': 'BooleanField(default=False)',
            'datetime': 'DateTimeField(default=timezone.now)',
            'date': 'DateField()',
            'foreign_key': 'ForeignKey({related_model}, on_delete=models.CASCADE)'
        }
        
        if field_type.lower() in field_mapping:
            if field_type.lower() == 'string':
                model_code += f"    {field_name} = models.{field_mapping[field_type.lower()]}\n"
            else:
                model_code += f"    {field_name} = models.{field_mapping[field_type.lower()]}\n"
        else:
            model_code += f"    {field_name} = models.CharField(max_length=200)\n"

    model_code += """
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)  # Customize this based on your needs

    def get_absolute_url(self):
        return reverse('{model_name}_detail', kwargs={{'pk': self.pk}})

    class Meta:
        ordering = ['-created_at']
"""

    return model_code

def generate_views(model_name: str) -> str:
    views_code = f"""from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import {model_name}
from .views_reporter import get_reporter  # Adjust import as needed

class {model_name}ListView(ListView):
    template_name = '{model_name.lower()}/list.html'
    model = {model_name}
    context_object_name = '{model_name.lower()}s'

    def get_context_data(self, **kwargs):
        return {{
            'object_list': {model_name}.objects.all()
        }}

class {model_name}DetailView(DetailView):
    template_name = '{model_name.lower()}/detail.html'
    model = {model_name}
    context_object_name = '{model_name.lower()}'

class {model_name}CreateView(LoginRequiredMixin, CreateView):
    template_name = "{model_name.lower()}/add.html"
    model = {model_name}
    fields = '__all__'
    success_url = reverse_lazy('{model_name.lower()}_list')

    def form_valid(self, form):
        # Optional: set reporter if needed
        form.instance.reporter = get_reporter(self.request.user)
        return super().form_valid(form)

class {model_name}UpdateView(UpdateView):
    template_name = "{model_name.lower()}/edit.html"
    model = {model_name}
    fields = '__all__'
    success_url = reverse_lazy('{model_name.lower()}_list')

class {model_name}DeleteView(DeleteView):
    template_name = '{model_name.lower()}/delete.html'
    model = {model_name}
    success_url = reverse_lazy('{model_name.lower()}_list')
"""
    return views_code

def create_django_app_files(model_name: str, fields: Dict[str, str], output_dir: str = '.'):
    """
    Create Django model and views files.
    
    model_name: Name of the model
    fields: Dictionary of field names and types
    output_dir: Directory to save files
    """
    # Sanitize the model name
    safe_model_name = sanitize_name(model_name)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    model_filename = os.path.join(output_dir, f'models_{safe_model_name.lower()}.py')
    with open(model_filename, 'w') as f:
        f.write(generate_model(safe_model_name, fields))
    
    views_filename = os.path.join(output_dir, f'views_{safe_model_name.lower()}.py')
    with open(views_filename, 'w') as f:
        f.write(generate_views(safe_model_name))
    
    print(f"Generated model file: {model_filename}")
    print(f"Generated views file: {views_filename}")

def main():
    model_name = input("Enter model name (e.g., 'Ticket'): ")
    
    fields = {}
    while True:
        field_name = input("Enter field name (or press Enter to finish): ")
        if not field_name:
            break
        
        field_type = input(f"Enter type for {field_name} (string/text/int/float/boolean/datetime/date): ")
        fields[field_name] = field_type
    
    create_django_app_files(model_name, fields)

if __name__ == '__main__':
    main()