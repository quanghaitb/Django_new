from django import forms



        
class contact_Forms(forms.Form):
    username = forms.CharField(max_length=25)
    email = forms.EmailField()
    body  = forms.CharField(widget=forms.Textarea)
    
        