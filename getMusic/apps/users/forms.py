from django import forms
from django.utils import timezone
from models import User
from django.utils.translation import gettext_lazy as _



class UserForm(forms.ModelForm):
   class Meta:
      model = User
      fields = [
         'geek_name', 'email', 'gender',
         "country", "github_profile","date_of_birth"
      ]

   def clean_date_of_birth(self):
      date = self.cleaned_data["date_of_birth"]
      today = timezone.now().date()
      if date.year >= today.year:
            raise forms.ValidationError(_("Invalid Date"), code="invalid")
      return date

