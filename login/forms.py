from django import forms
from .models import login,Addfamilyphotos,signup

class LoginForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=login
        fields=('Username','Password')
class AddPhotoForm(forms.ModelForm):

    class Meta:
        model=Addfamilyphotos
        fields = ('Photo',)

class SignupForm(forms.Form):

    FirstName = forms.CharField(max_length=30)
    LastName = forms.CharField(max_length=30)
    DateOfBirth = forms.DateField(label='Date of Birth')
    EmailID = forms.EmailField()
    PhoneNumber = forms.CharField(max_length=10)
    Username = forms.CharField(max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput)

