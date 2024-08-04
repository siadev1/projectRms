from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Students
from .models import Items


class Register(UserCreationForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model= User
        fields = ["username", "email", "password1", "password2"]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

# STUDENTS=(
#     ("1","morning"),
#     ("2","afternoon"),
#     ("3","night")
# )
class ItemForm(forms.ModelForm):
   
    class Meta:
        model = Items
        fields = ['name','price']