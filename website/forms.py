from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small</span>'

        self.fields['password1'].widget.attrs['class'] = 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class=""><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class=""><small>Enter the same password as before, for verification.</small></span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "State", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Zipcode", "class": "p-2 focus:outline-none border-solid border-2 border-[#03346E] rounded-md"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)