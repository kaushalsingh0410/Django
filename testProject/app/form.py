from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
        'name':forms.TextInput(attrs = {'class':'form-control'}),
        'email':forms.EmailInput(attrs = {'class':'form-control'}),
        'comment':forms.Textarea(attrs = {'class':'form-control','rows':3}),
         }

    # def __init__(self):
    #     super().__init__()
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control' 
      