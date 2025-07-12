from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Full Name ', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    phone = forms.CharField(label='Mobile Number', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}))
    designation = forms.CharField(label='Designation', required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}))
    message = forms.CharField(label='Your Message', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your Message'}))
