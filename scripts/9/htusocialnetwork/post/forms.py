from django import forms

class CreatePost(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    
    