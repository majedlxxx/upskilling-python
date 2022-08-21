from django import forms
from account.models import Account

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
        return self.cleaned_data['username'].strip().lower()
    
    
    

class SignupForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #****
    confirm_your_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean_username(self):
        if Account.objects.filter(username = self.cleaned_data['username']).exists():
            raise forms.ValidationError("The user already exists")
        return self.cleaned_data['username'].strip().lower()
    
    def clean_confirm_your_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_your_password']:
            raise forms.ValidationError("The password and it's confirmation do not match")
        return self.cleaned_data['password']
    
