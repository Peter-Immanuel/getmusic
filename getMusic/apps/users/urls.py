from django.urls import path
from .views import (
   Project2DetailView, 
   UserView, 
   CustomTemplateView,
   ProjectDetailView,
)
from django.views.generic import TemplateView

urlpatterns = [
   path('user/', UserView.as_view(), name='users'),
   path('templates/', TemplateView.as_view(template_name="general/index.html"), name='templates'),
   path('view/', CustomTemplateView.as_view(), name='templates'),
   path("project/<uuid:pk>/",ProjectDetailView.as_view(), name="project-detail"),
   path("my-project/<uuid:pk>/", Project2DetailView.as_view(), name="project-detail-2")
]