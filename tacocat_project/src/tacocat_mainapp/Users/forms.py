from django.forms import ModelForm
from .models import User

# 'User' is being imported from the models.py file so we have access to the information inside of the class

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['handle', 'password', 'email']

