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

    FirstName = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter First Name'
        }),
    )
    LastName = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Last Name'
        }),
    )
    EmailID = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email'
        }),
    )
    Username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Username'
        }),
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Password'
        }
            )
    )

