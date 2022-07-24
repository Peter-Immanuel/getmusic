from typing import Dict, Any, Optional
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import (
   TemplateView, RedirectView,
   DetailView, ListView
)

from .models.projects import ProgrammingLanguage, Project
from .forms import UserForm

class UserView(View):
   template_name = 'user/user.html'
   form = UserForm

   def get(self, request):
      form = self.form()
      return render(request, self.template_name, {'form': form})

   def post(self, request):
      form = self.form(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponse("Success!!!")
      return render(request, self.template_name, {'form': form})



class CustomTemplateView(TemplateView):
   template_name: str = 'general/index.html'
   extra_context: Optional[Dict[str, Any]] = {
      "my_name": "Bemshima",
      "source": "Custom View"
   }

   def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
      return super().get_context_data(**kwargs)


# django generic display views
class ProjectDetailView(DetailView):
   model = Project


class Project2DetailView(DetailView):
   model = Project
   template_name = "users/details.html"